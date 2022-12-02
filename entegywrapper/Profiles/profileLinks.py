from typing import Generator

from entegywrapper.entegySchemas.content import Link, TemplateType
from entegywrapper.entegySchemas.profile import Profile


def selected_profile_links(
    self,
    *,
    profile_id: str | None = None,
    external_reference: str | None = None,
    internal_reference: str | None = None,
    badge_reference: str | None = None
) -> Generator[list[Link], None, None]:
    """
    Yields all the profile links the specified profile has in blocks generated
    by the Entegy API's pagination.

    Parameters
    ----------
        `profile_id` (`str`, optional): the profileId of the profile to get; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the profile to get; defaults to `None`
        `badgeReference` (`str`, optional): the badgeReference of the profile to get; defaults to `None`
        `internalReference` (`str`, optional): the internalReference of the profile to get; defaults to `None`

    Yields
    -------
        `Generator[list[Link], None, None]`: paginated blocks of selected links
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "pagination": {
            "start": 0,
            "limit": 1000
        }
    }

    if profile_id is not None:
        data["profileId"] = profile_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    elif internal_reference is not None:
        data["internalReference"] = internal_reference
    elif badge_reference is not None:
        data["badgeReference"] = badge_reference
    else:
        raise ValueError("You must provide a profile identifier")

    response = self.post(
        self.api_endpoint + "/v2/ProfileLink/Selected/",
        headers=self.headers,
        data=data
    )
    yield response["links"]

    while response["pagination"]["start"] + response["pagination"]["limit"] \
            < response["pagination"]["count"]:
        data["pagination"]["start"] += data["pagination"]["limit"]

        response = self.post(
            self.api_endpoint + "/v2/ProfileLink/Selected/",
            headers=self.headers,
            data=data
        )
        yield response["links"]


def page_profile_links(
    self,
    template_type: TemplateType,
    *,
    module_id: str | None = None,
    external_reference: str | None = None
) -> Generator[list[Profile], None, None]:
    """
    Gets all the profiles linked to a content page.

    Parameters
    ----------
        `template_type` (`TemplateType`): the templateType of the page
        `module_id` (`int`): the moduleId of the page
        `return_limit` (`int`): the maximum number of results to return; defaults to 100

    Yields
    -------
        `Generator[list[Profile], None, None]`: paginated blocks of linked profiles
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "templateType":template_type,
        "pagination": {
            "index": 0,
            "limit": 1000
        }
    }

    if module_id is not None:
        data["moduleId"] = module_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    else:
        raise ValueError("You must provide a page identifier")

    response = self.post(
        self.api_endpoint + "/v2/ProfileLink/Page/",
        headers=self.headers,
        data=data
    )
    yield response["profiles"]

    while response["pagination"]["index"] + response["pagination"]["limit"] \
            < response["pagination"]["count"]:
        data["pagination"]["index"] += data["pagination"]["limit"]

        response = self.post(
            self.api_endpoint + "/v2/ProfileLink/Page/",
            headers=self.headers,
            data=data
        )
        yield response["profiles"]


def select_profile_link(
    self,
    link: Link,
    *,
    profile_id: str | None = None,
    internal_reference: str | None = None,
    external_reference: str | None = None,
    badge_reference: str | None = None
):
    """
    Selects the specified link for the specified profile.

    Parameters
    ----------
        `link` (`Link`): the link you wish to select
        `profile_id` (`str`, optional): the profileId of the profile; defaults to `None`
        `internal_reference` (`str`, optional): the internalReference of the profile; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the profile; defaults to `None`
        `badge_reference` (`str`, optional): the badgeReference of the profile; defaults to `None`
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "link": link
    }

    if profile_id is not None:
        data["profileId"] = profile_id
    elif internal_reference is not None:
        data["internalReference"] = internal_reference
    elif external_reference is not None:
        data["externalReference"] = external_reference
    elif badge_reference is not None:
        data["badgeReference"] = badge_reference
    else:
        raise ValueError("You must provide a profile identifier")

    self.post(
        self.api_endpoint + "/v2/ProfileLink/Select/",
        headers=self.headers,
        data=data
    )


def multi_select_profile_links(
    self,
    profiles: list[dict[str, str | list[Link]]]
):
    """
    Allows you to select multiple pages on multiple profiles at once

    Parameters
    ----------
        `profiles` (`list[dict[str, str | list[Link]]]`): list of profile references with link objects within

    The format of `profiles` is as follows:
    ```python
        [
            {
                "profileId": "ff11c742-346e-4874-9e24-efe6980a7453",
                "links": [
                    {
                        "template_type": "session",
                        "moduleId":1
                    },
                    {
                        "template_type": "session",
                        "moduleId":2
                    },
                    {
                        "template_type": "session",
                        "moduleId":3
                    }
                ]
            },
            ...
        ]
    ```
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "profiles": profiles
    }

    self.post(
        self.api_endpoint + "/v2/ProfileLink/MultiSelect/",
        headers=self.headers,
        data=data
    )


def deselect_profile_links(
    self,
    link: Link,
    *,
    profile_id: str | None = None,
    internal_reference: str | None = None,
    external_reference: str | None = None,
    badge_reference: str | None = None
):
    """
    Allows you to deselect a link for a profile.

    Parameters
    ----------
        `link` (`Link`): the link you wish to deselect
        `profile_id` (`str`, optional): the profileId of the profile; defaults to `None`
        `internal_reference` (`str`, optional): the internalReference of the profile; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the profile; defaults to `None`
        `badge_reference` (`str`, optional): the badgeReference of the profile; defaults to `None`
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "link": link
    }

    if profile_id is not None:
        data["profileId"] = profile_id
    elif internal_reference is not None:
        data["internalReference"] = internal_reference
    elif external_reference is not None:
        data["externalReference"] = external_reference
    elif badge_reference is not None:
        data["badgeReference"] = badge_reference
    else:
        raise ValueError("You must provide a profile identifier")

    self.post(
        self.api_endpoint + "/v2/ProfileLink/Deselect/",
        headers=self.headers,
        data=data
    )


def clear_profile_links(
    self,
    template_type: TemplateType,
    *,
    profile_id: str | None = None,
    internal_reference: str | None = None,
    external_reference: str | None = None,
    badge_reference: str | None = None
):
    """
    Clears all the selected links of a template type on the specified profile.

    Parameters
    ----------
        `template_type` (`TemplateType`): the templateType of links to clear
        `profile_id` (`str`, optional): the profileId of the profile; defaults to `None`
        `internal_reference` (`str`, optional): the internalReference of the profile; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the profile; defaults to `None`
        `badge_reference` (`str`, optional): the badgeReference of the profile; defaults to `None`
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "templateType":template_type
    }

    if profile_id is not None:
        data["profileId"] = profile_id
    elif internal_reference is not None:
        data["internalReference"] = internal_reference
    elif external_reference is not None:
        data["externalReference"] = external_reference
    elif badge_reference is not None:
        data["badgeReference"] = badge_reference
    else:
        raise ValueError("You must provide a profile identifier")

    self.post(
        self.api_endpoint + "/v2/ProfileLink/Clear/",
        headers=self.headers,
        data=data
    )
