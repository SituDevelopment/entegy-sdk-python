import json
import os
import requests
import sys
import time

from requests.structures import CaseInsensitiveDict
from typing import Any, Literal

sys.path.append(os.path.dirname(__file__))

api_endpoints = {
    "AU": "https://api.entegy.com.au",
    "US": "https://api-us.entegy.com.au",
    "EU": "https://api-eu.entegy.com.au",
}

Identifier: type = Literal["externalReference", "moduleId", "name"]


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
    from .Profiles.profilePayments import (
        add_profile_payment
    )
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
        update_categories,
        delete_categories,
    )
    from .Content.documents import (
        add_documents,
        add_external_content_documents
    )
    from .Content.multiLink import (
        get_multi_links,
        add_multi_links,
        remove_multi_link,
        remove_all_multi_links,
    )
    from .Points.pointManagement import (
        award_points,
        get_point_leaderboard,
        get_points
    )
    from .Plugins.extAuth import (
        external_authentication
    )
    from .Notification.notification import (
        send_notification,
        send_bulk_notification
    )

    def __init__(
        self,
        api_key: str | list[str],
        api_secret: str | list[str],
        project_id: str,
        region: str = "AU"
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
        # if multiple API keys were given, ensure that the number of keys and
        # secrets match
        assert type(api_key) == type(api_secret)
        if type(api_key) == list:
            assert len(api_key) == len(api_secret)
        assert type(project_id) == str
        assert type(region) == str
        assert region in api_endpoints.keys()

        self.api_key = api_key
        self.api_secret = api_secret
        self.current_key_pair = 0
        self.project_id = project_id

        self.headers = CaseInsensitiveDict()
        self.headers["Content-Type"] = "application/json"
        self.get_key()

        self.api_endpoint = api_endpoints[region]

    def get_key(self) -> str:
        """
        Returns the API Key. If a list of keys was provided, the current key is
        returned.

        Returns
        -------
            `str`: API Key
        """
        if isinstance(self.api_key, list):
            self.headers["Authorization"] = f"ApiKey {self.api_secret[self.current_key_pair]}"
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

    def post(
        self,
        endpoint: str,
        data: dict[str, Any],
        headers: list = []
    ) -> dict[str, Any]:
        """
        Post the given `data` to the given `endpoint` of the Entegy API.

        Parameters
        ----------
            `endpoint` (`str`): API endpoint to which to post
            `data` (`dict[str, Any]`): data to post
            `headers` (`list`): request headers; defaults to the empty list

        Returns
        -------
            `dict[str, Any]`: response data
        """
        resp = None
        retry_count = 0
        permission_error_count = 0

        while resp is None:
            resp = requests.post(endpoint, headers=headers, data=data)

            if resp is None:
                raise Exception("No reponse received from API")

            # try catch used here as sometimes the resp object comes through as
            # a blank JSON object
            try:
                if resp.json()['response'] == 403:
                    time.sleep(0.5)
                    permission_error_count += 1
                    if permission_error_count >= 5:
                        raise Exception("Invalid API Key")
                    resp = None
            except:
                resp = None
                continue

            if resp.json()['response'] == 489:
                # if there is a rate limit issue, wait the remaining time and try again
                if retry_count >= len(self.api_key):
                    print("Rate limit reached, waiting " +
                          str(resp.json()['resetDuration']) + " seconds")
                    time.sleep(resp.json()["resetDuration"] + 2)
                    print("Continuing...")
                    resp = None
                else:
                    # update API key
                    self.cycle_key()
                    data = json.loads(data)
                    data["apiKey"] = self.get_key()
                    headers = self.headers
                    print(f"Rate limit reached, trying alternate key: {data['apiKey']}")
                    data = json.dumps(data)
                    retry_count += 1
                    resp = None

        return resp.json()

    def delete(
        self,
        endpoint: str,
        data: dict[str, Any],
        headers: list = []
    ) -> dict[str, Any]:
        """
        Delete the given `data` from the given `endpoint` of the Entegy API.

        Parameters
        ----------
            `endpoint` (`str`): API endpoint from which to delete
            `data` (`dict[str, Any]`): data to delete
            `headers` (`list`): request headers; defaults to the empty list

        Returns
        -------
            `dict[str, Any]`: response data
        """
        resp = None
        retry_count = 0
        permission_error_count = 0

        while resp is None:
            resp = requests.delete(endpoint, headers=headers, data=data)

            if resp is None:
                raise Exception("No reponse received from API")

            # try catch used here as sometimes the resp object comes through as
            # a blank JSON object
            try:
                if resp.json()['response'] == 403:
                    time.sleep(0.5)
                    permission_error_count += 1
                    if permission_error_count >= 5:
                        raise Exception("Invalid API Key")
                    resp = None
            except:
                resp = None
                continue

            if resp.json()['response'] == 489:
                # if there is a rate limit issue, wait the remaining time and try again
                if retry_count >= len(self.api_key):
                    print("Rate limit reached, waiting " +
                          str(resp.json()['resetDuration']) + " seconds")
                    time.sleep(resp.json()["resetDuration"] + 2)
                    print("Continuing...")
                    resp = None
                else:
                    # update API key
                    self.cycle_key()
                    data = json.loads(data)
                    data["apiKey"] = self.get_key()
                    headers = self.headers
                    print(f"Rate limit reached, trying alternate key: {data['apiKey']}")
                    data = json.dumps(data)
                    retry_count += 1
                    resp = None

        return resp.json()
