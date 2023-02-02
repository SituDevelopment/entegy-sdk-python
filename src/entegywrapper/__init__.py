import json
import os
import requests
import sys
import time

from requests.structures import CaseInsensitiveDict
from typing import Callable

from entegywrapper.errors import EntegyInvalidAPIKeyError

sys.path.append(os.path.dirname(__file__))

API_ENDPOINTS = {
    "AU": "https://api.entegy.com.au",
    "US": "https://api-us.entegy.com.au",
    "EU": "https://api-eu.entegy.com.au",
}


class EntegyAPI:
    from .Profiles.profiles import (
        all_profiles,
        create_profile,
        get_profile,
        delete_profile,
        update_profile,
        sync_profiles,
        send_welcome_email,
    )
    from .Profiles.profileTypes import (
        get_profile_type,
        create_profile_type,
        update_profile_type,
        delete_profile_type,
        all_profile_types,
    )
    from .Profiles.profileCustom import (
        get_profile_custom,
        create_profile_custom,
        update_profile_custom,
        delete_profile_custom,
        all_profile_custom,
    )
    from .Profiles.profileLinks import (
        selected_profile_links,
        page_profile_links,
        select_profile_link,
        multi_select_profile_links,
        deselect_profile_links,
        clear_profile_links,
    )
    from .Profiles.profilePayments import add_profile_payment
    from .Content.content import (
        get_content,
        get_schedule_content,
        create_content,
        add_children_content,
        update_content,
        delete_content,
    )
    from .Content.categories import (
        available_categories,
        select_categories,
        deselect_categories,
        create_categories,
        create_child_categories,
        update_category,
        delete_categories,
    )
    from .Content.documents import add_documents, add_external_content_documents
    from .Content.multiLink import (
        get_multi_links,
        add_multi_links,
        remove_multi_link,
        remove_all_multi_links,
    )
    from .Points.pointManagement import award_points, get_point_leaderboard, get_points
    from .Plugins.extAuth import external_authentication
    from .Notification.notification import send_notification, send_bulk_notification
    from .AttendanceTracking.attendanceTracking import (
        add_check_in,
        get_attendees,
        get_attended,
    )

    def __init__(
        self,
        api_key: str | list[str],
        api_secret: str | list[str],
        project_id: str,
        region: str = "AU",
    ):
        """
        Creates an Entegy API wrapper to interact with the specified project.

        Parameters
        ----------
            `api_key` (`str | list[str]`): Entegy API key(s)
            `api_secret` (`str | list[str]`): Entegy API secret key(s)
            `project_id` (`str`): Entegy project ID
            `region` (`str`, optional): project region: one of "AU", "US", "EU"; defaults to "AU"
        """
        if isinstance(api_key, list):
            assert isinstance(api_secret, list)
            assert len(api_key) == len(api_secret)
            assert all(isinstance(key, str) for key in api_key)
            assert all(isinstance(secret, str) for secret in api_secret)
        else:
            assert isinstance(api_key, str)
            assert isinstance(api_secret, str)
        assert isinstance(project_id, str)
        assert isinstance(region, str)
        assert region in API_ENDPOINTS.keys()

        if isinstance(api_key, list):
            self.api_key = list(map(lambda x: x.strip(), api_key))
            self.api_secret = list(map(lambda x: x.strip(), api_secret))
        else:
            self.api_key = api_key.strip()
            self.api_secret = api_secret.strip()

        self.current_key_pair = 0
        self.project_id = project_id.strip()

        self.headers = CaseInsensitiveDict()
        self.headers["Content-Type"] = "application/json"
        self.get_key()

        self.api_endpoint = API_ENDPOINTS[region]

    def get_key(self) -> str:
        """
        Returns the API Key. If a list of keys was provided, the current key is
        returned.

        Returns
        -------
            `str`: API Key
        """
        if isinstance(self.api_key, list):
            self.headers[
                "Authorization"
            ] = f"ApiKey {self.api_secret[self.current_key_pair]}"
            return self.api_key[self.current_key_pair]

        self.headers["Authorization"] = f"ApiKey {self.api_secret}"
        return self.api_key

    def cycle_key(self):
        """
        Cycles to the next API keypair, wrapping to the first where necessary.
        """
        self.current_key_pair = (self.current_key_pair + 1) % len(self.api_key)

    def get_endpoint(self) -> str:
        """
        Returns the endpoint URL.

        Returns
        -------
            `str`: API endpoint URL
        """
        return self.api_endpoint

    def request(self, method: Callable, endpoint: str, data: dict) -> dict:
        """
        Sends the given data to the given endpoint of the Entegy API, using the given
        method. Internalised to allow for automatic key cycling and error handling.

        Parameters
        ----------
            `method` (`Callable`): method to use to send the request
            `endpoint` (`str`): API endpoint to which to post
            `data` (`dict`): data to post

        Raises
        ------
            `EntegyInvalidAPIKeyError`: if the API keys are invalid

        Returns
        -------
            `dict`: response data
        """
        retry_count = 0
        permission_error_count = 0

        data |= {"apiKey": self.get_key(), "projectId": self.project_id}

        response = None
        while response is None:
            response = method(endpoint, headers=self.headers, data=json.dumps(data))

            try:
                data = response.json()
            except:
                response = None
                continue

            match data["response"]:
                case 403:  # invalid API key
                    if (permission_error_count := permission_error_count + 1) >= 5:
                        raise EntegyInvalidAPIKeyError()

                    response = None
                case 489:  # rate-limit
                    if retry_count >= len(self.api_key):
                        duration = data["resetDuration"]
                        print(f"Rate limit reached, waiting {duration} seconds")
                        time.sleep(duration + 2)
                        print("Continuing...")
                        response = None
                    else:
                        self.cycle_key()
                        key = self.get_key()
                        data["apiKey"] = key
                        print(f"Rate limit reached, trying alternate key: {key}")
                        retry_count += 1
                        response = None

        return data

    def post(self, endpoint: str, data: dict) -> dict:
        """
        Posts the given data to the given endpoint of the Entegy API.

        Parameters
        ----------
            `endpoint` (`str`): API endpoint to which to post
            `data` (`dict`): data to post

        Returns
        -------
            `dict`: response data
        """
        return self.request(requests.post, endpoint, data)

    def delete(self, endpoint: str, data: dict) -> dict:
        """
        Deletes the given data from the given endpoint of the Entegy API.

        Parameters
        ----------
            `endpoint` (`str`): API endpoint from which to delete
            `data` (`dict`): data to delete

        Returns
        -------
            `dict`: response data
        """
        return self.request(requests.delete, endpoint, data)
