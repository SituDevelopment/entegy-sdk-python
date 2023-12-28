import json
import os
import sys
import time
from typing import Callable

import requests
from requests.structures import CaseInsensitiveDict

from entegywrapper.errors import EntegyInvalidAPIKeyError, EntegyNoDataError

sys.path.append(os.path.dirname(__file__))

API_ENDPOINTS = {
    "AU": "https://api.entegy.com.au",
    "US": "https://api-us.entegy.com.au",
    "EU": "https://api-eu.entegy.com.au",
}


class EntegyAPI:
    from .attendance_tracking.attendance_tracking import (
        add_check_in,
        get_attended,
        get_attendees,
    )
    from .content.categories import (
        available_categories,
        create_categories,
        create_child_categories,
        delete_categories,
        deselect_categories,
        select_categories,
        update_category,
    )
    from .content.content import (
        add_children_content,
        create_content,
        delete_content,
        get_content,
        get_schedule_content,
        update_content,
    )
    from .content.documents import add_documents, add_external_content_documents
    from .content.multi_link import (
        add_multi_links,
        get_multi_links,
        remove_all_multi_links,
        remove_multi_link,
    )
    from .notification.notification import send_bulk_notification, send_notification
    from .plugins.ext_auth import external_authentication
    from .points.point_management import award_points, get_point_leaderboard, get_points
    from .profiles.profile_custom import (
        all_profile_custom,
        create_profile_custom,
        delete_profile_custom,
        get_profile_custom,
        update_profile_custom,
    )
    from .profiles.profile_links import (
        clear_profile_links,
        deselect_profile_links,
        multi_select_profile_links,
        page_profile_links,
        select_profile_link,
        selected_profile_links,
    )
    from .profiles.profile_payments import add_profile_payment
    from .profiles.profile_types import (
        all_profile_types,
        create_profile_type,
        delete_profile_type,
        get_profile_type,
        update_profile_type,
    )
    from .profiles.profiles import (
        all_profiles,
        create_profile,
        delete_profile,
        get_profile,
        send_welcome_email,
        sync_profile_block,
        sync_profiles,
        update_profile,
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
        keys_attempted = 0
        failed_requests = 0

        data |= {"apiKey": self.get_key(), "projectId": self.project_id}

        response = None
        while response is None:
            response = method(endpoint, headers=self.headers, data=json.dumps(data))

            try:
                response = response.json()
            except:
                failed_requests += 1
                if failed_requests >= 5:
                    raise EntegyNoDataError()

                response = None
                continue

            match response["response"]:
                case 403:  # invalid API key
                    failed_requests += 1
                    if failed_requests >= 5:
                        raise EntegyInvalidAPIKeyError()

                    response = None
                case 489:  # rate-limit
                    if keys_attempted >= len(self.api_key):
                        duration = response["resetDuration"]
                        print(f"Rate limit reached, waiting {duration} seconds")
                        time.sleep(duration + 2)
                        print("Continuing...")
                        keys_attempted = 0
                        response = None
                    else:
                        self.cycle_key()
                        key = self.get_key()
                        data["apiKey"] = key
                        print(f"Rate limit reached, trying alternate key: {key}")
                        keys_attempted += 1
                        response = None

        return response

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
