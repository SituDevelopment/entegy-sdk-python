from typing import Any

Link: type = dict
"""
The format of a `Link` is as follows:
    ```python
        {
            "template_type": "session",
            "moduleId":1
        }
    ```
"""


def selected_profile_links(
    self,
    profile_id: str,
    *,
    return_limit: int = 100
) -> dict[str, Any]:
    """
    Return all the profile links the profile has.

    Parameters
    ----------
        `profile_id` (`str`): the profileId of the profile
        `return_limit` (`int`): the index and amount of results to return; defaults to 100

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "profileID": profile_id,
        "pagination": {
            "index": 0,
            "limit": return_limit
        },
    }

    return self.post(
        self.api_endpoint + "/v2/ProfileLink/Selected/",
        headers=self.headers,
        data=data
    )


def page_profile_links(
    self,
    template_type: str,
    module_id: str,
    *,
    return_limit: int = 100
) -> dict[str, Any]:
    """
    Gets all the profiles linked to a Content Page.

    Parameters
    ----------
        `template_type` (`str`): the template_type of the page
        `module_id` (`int`): the moduleId of the page
        `return_limit` (`int`): the maximum number of results to return; defaults to 100

    Returns
    -------
        Pagination response and list of profile objects
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "templateType":template_type,
        "moduleId": module_id,
        "pagination": {
            "index": 0,
            "limit": return_limit
        },
    }

    return self.post(
        self.api_endpoint + "/v2/ProfileLink/Page/",
        headers=self.headers,
        data=data
    )


def select_profile_link(self, profile_id: str, link: Link) -> dict[str, Any]:
    """
    Allows you to select a link for a profile

    Parameters
    ----------
        `profile_id` (`str`): the profileId of the profile
        `link` (`Link`): the link you wish to select
    ```

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "profileID": profile_id,
        "link": link,
    }

    return self.post(
        self.api_endpoint + "/v2/ProfileLink/Select/",
        headers=self.headers,
        data=data
    )


def multi_select_profile_links(
    self,
    profiles: list[str, str | list[Link]]
) -> dict[str, Any]:
    """
    Allows you to select multiple pages on multiple profiles at once

    Parameters
    ----------
        `profiles` (`list[str, str | list[Link]]`): list of profile references with link objects within

    The format of `profiles` is as follows:
    ```python
        [
            {
                "profileId": "ff11c742-346e-4874-9e24-efe6980a7453",
                "links": [
                    {
                        "template_type": "sesSiOn",
                        "moduleId":1
                    },
                    {
                        "template_type": "sesSiOn",
                        "moduleId":2
                    },
                    {
                        "template_type": "sesSiOn",
                        "moduleId":3
                    }
                ]
            },
        ]
    ```

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "profiles": profiles
    }

    return self.post(
        self.api_endpoint + "/v2/ProfileLink/MultiSelect/",
        headers=self.headers,
        data=data
    )


def deselect_profile_links(self, profile_id: str, link: Link) -> dict[str, Any]:
    """
    Allows you to deselect a link for a profile.

    Parameters
    ----------
        `profile_id` (`str`): the profileId of the profile
        `link` (`Link`): the link you wish to deselect

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "profileId": profile_id,
        "link": link,
    }

    return self.post(
        self.api_endpoint + "/v2/ProfileLink/Deselect/",
        headers=self.headers,
        data=data
    )


def clear_profile_links(
    self,
    profile_id: str,
    template_type: str
) -> dict[str, Any]:
    """
    Allows you to clear all the selected links of a template_type on a single profile

    Parameters
    ----------
        `profile_id` (`str`): the profileId of the profile
        `template_type` (`str`): the template_type to clear links of

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "profileId": profile_id,
        "templateType":template_type,
    }

    return self.post(
        self.api_endpoint + "/v2/ProfileLink/Clear/",
        headers=self.headers,
        data=data
    )
