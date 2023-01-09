from typing import Generator

from src.entegywrapper.errors import EntegyFailedRequestError
from src.entegywrapper.schemas.content import Link, TemplateType
from src.entegywrapper.schemas.profile import Profile


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
        `internal_reference` (`str`, optional): the internalReference of the profile to get; defaults to `None`
        `badge_reference` (`str`, optional): the badgeReference of the profile to get; defaults to `None`

    Raises
    ------
        `ValueError`: if no identifier is specified
        `EntegyFailedRequestError`: if the API request fails

    Yields
    -------
        `Generator[list[Link], None, None]`: paginated blocks of selected links
    """
    data = {"pagination": {"start": 0, "limit": 1000}}

    if profile_id is not None:
        data["profileId"] = profile_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    elif internal_reference is not None:
        data["internalReference"] = internal_reference
    elif badge_reference is not None:
        data["badgeReference"] = badge_reference
    else:
        raise ValueError("Please specify an identifier")

    response = self.post(self.api_endpoint + "/v2/ProfileLink/Selected/", data=data)
    yield response["links"]

    while (
        response["pagination"]["start"] + response["pagination"]["limit"]
        < response["pagination"]["count"]
    ):
        data["pagination"]["start"] += data["pagination"]["limit"]

        response = self.post(self.api_endpoint + "/v2/ProfileLink/Selected/", data=data)

        match response["response"]:
            case 200:
                yield response["links"]
            case 401:
                raise EntegyFailedRequestError("Profile not found")
            case _:
                raise EntegyFailedRequestError("Unknown error")


def page_profile_links(
    self,
    template_type: TemplateType,
    *,
    module_id: int | None = None,
    external_reference: str | None = None
) -> Generator[list[Profile], None, None]:
    """
    Yields all the profiles linked to a content page.

    Parameters
    ----------
        `template_type` (`TemplateType`): the templateType of the page
        `module_id` (`int`, optional): the moduleId of the page; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the page; defaults to `None`

    Raises
    ------
        `ValueError`: if no identifier is specified
        `EntegyFailedRequestError`: if the API request fails

    Yields
    -------
        `Generator[list[Profile], None, None]`: paginated blocks of linked profiles
    """
    data = {"templateType": template_type, "pagination": {"index": 0, "limit": 1000}}

    if module_id is not None:
        data["moduleId"] = module_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    else:
        raise ValueError("Please specify an identifier")

    response = self.post(self.api_endpoint + "/v2/ProfileLink/Page/", data=data)
    yield response["profiles"]

    while (
        response["pagination"]["index"] + response["pagination"]["limit"]
        < response["pagination"]["count"]
    ):
        data["pagination"]["index"] += data["pagination"]["limit"]

        response = self.post(self.api_endpoint + "/v2/ProfileLink/Page/", data=data)

        match response["response"]:
            case 200:
                yield response["profiles"]
            case 401:
                raise EntegyFailedRequestError("Profile not found")
            case 402:
                raise EntegyFailedRequestError("Linked content not found")
            case _:
                raise EntegyFailedRequestError("Unknown error")


def select_profile_link(
    self,
    link: Link,
    *,
    profile_id: str | None = None,
    external_reference: str | None = None,
    internal_reference: str | None = None,
    badge_reference: str | None = None
):
    """
    Selects the specified link for the specified profile.

    Parameters
    ----------
        `link` (`Link`): the link to select
        `profile_id` (`str`, optional): the profileId of the profile; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the profile; defaults to `None`
        `internal_reference` (`str`, optional): the internalReference of the profile; defaults to `None`
        `badge_reference` (`str`, optional): the badgeReference of the profile; defaults to `None`

    Raises
    ------
        `ValueError`: if no identifier is specified
    """
    data = {"link": link}

    if profile_id is not None:
        data["profileId"] = profile_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    elif internal_reference is not None:
        data["internalReference"] = internal_reference
    elif badge_reference is not None:
        data["badgeReference"] = badge_reference
    else:
        raise ValueError("Please specify an identifier")

    response = self.post(self.api_endpoint + "/v2/ProfileLink/Select/", data=data)

    match response["response"]:
        case 200:
            return
        case 401:
            raise EntegyFailedRequestError("Profile not found")
        case 402:
            raise EntegyFailedRequestError("Linked content not found")
        case _:
            raise EntegyFailedRequestError("Unknown error")


def multi_select_profile_links(self, profiles: list[dict[str, str | list[Link]]]):
    """
    Selects multiple pages on multiple profiles.

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
    data = {"profiles": profiles}

    response = self.post(self.api_endpoint + "/v2/ProfileLink/MultiSelect/", data=data)

    match response["response"]:
        case 401:
            raise EntegyFailedRequestError("Profile doesn't exist")
        case 402:
            raise EntegyFailedRequestError("Invalid templateType")
        case 404:
            raise EntegyFailedRequestError("Invalid moduleId or externalReference")
        case _:
            raise EntegyFailedRequestError("Unknown error")


def deselect_profile_links(
    self,
    link: Link,
    *,
    profile_id: str | None = None,
    external_reference: str | None = None,
    internal_reference: str | None = None,
    badge_reference: str | None = None
):
    """
    Deselects a link for a profile.

    Parameters
    ----------
        `link` (`Link`): the link to deselect
        `profile_id` (`str`, optional): the profileId of the profile; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the profile; defaults to `None`
        `internal_reference` (`str`, optional): the internalReference of the profile; defaults to `None`
        `badge_reference` (`str`, optional): the badgeReference of the profile; defaults to `None`

    Raises
    ------
        `ValueError`: if no identifier is specified
    """
    data = {"link": link}

    if profile_id is not None:
        data["profileId"] = profile_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    elif internal_reference is not None:
        data["internalReference"] = internal_reference
    elif badge_reference is not None:
        data["badgeReference"] = badge_reference
    else:
        raise ValueError("Please specify an identifier")

    response = self.post(self.api_endpoint + "/v2/ProfileLink/Deselect/", data=data)

    match response["response"]:
        case 401:
            raise EntegyFailedRequestError("Profile doesn't exist")
        case 402:
            raise EntegyFailedRequestError("Linked content not found")
        case _:
            raise EntegyFailedRequestError("Unknown error")


def clear_profile_links(
    self,
    template_type: TemplateType,
    *,
    profile_id: str | None = None,
    external_reference: str | None = None,
    internal_reference: str | None = None,
    badge_reference: str | None = None
):
    """
    Clears all the selected links of a template type on the specified profile.

    Parameters
    ----------
        `template_type` (`TemplateType`): the templateType of links to clear
        `profile_id` (`str`, optional): the profileId of the profile; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the profile; defaults to `None`
        `internal_reference` (`str`, optional): the internalReference of the profile; defaults to `None`
        `badge_reference` (`str`, optional): the badgeReference of the profile; defaults to `None`

    Raises
    ------
        `ValueError`: if no identifier is specified
    """
    data = {"templateType": template_type}

    if profile_id is not None:
        data["profileId"] = profile_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    elif internal_reference is not None:
        data["internalReference"] = internal_reference
    elif badge_reference is not None:
        data["badgeReference"] = badge_reference
    else:
        raise ValueError("Please specify an identifier")

    response = self.post(self.api_endpoint + "/v2/ProfileLink/Clear/", data=data)

    match response["response"]:
        case 401:
            raise EntegyFailedRequestError("Profile doesn't exist")
        case 402:
            raise EntegyFailedRequestError("Template type doesn't exist")
        case _:
            raise EntegyFailedRequestError("Unknown error")
