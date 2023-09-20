from typing import Generator

from entegywrapper.errors import EntegyFailedRequestError, EntegyServerError
from entegywrapper.schemas.profile import (
    Profile,
    ProfileCreate,
    ProfileIdentifier,
    ProfileType,
    ProfileUpdate,
)


def all_profiles(
    self,
    *,
    include_custom_fields: bool = False,
    include_permissions: bool = False,
    status: str | None = None,
    profile_type: ProfileType | None = None,
    updated_after: str | None = None,
    created_after: str | None = None,
) -> Generator[list[Profile], None, None]:
    """
    Yields all user profiles in blocks generated by the Entegy API's pagination.

    Parameters
    ----------
        `include_custom_fields` (`bool`, optional): whether to include custom fields for each profile; defaults to `False`
        `include_permissions` (`bool`, optional): whether to include permissions for each profile; defaults to `False`
        `status` (`str`, optional): only select profiles with this status; defaults to `None`
        `profile_type` (`ProfileType`, optional): only select profiles of this type; defaults to `None`
        `updated_after` (`str`, optional): only select profiles updated after this time; defaults to `None`
        `created_after` (`str`, optional): only select profiles created after this time; defaults to `None`

    Yields
    ------
        `Generator[list[Profile], None, None]`: paginated blocks of user profiles
    """
    data = {
        "pagination": {"start": 0, "limit": 1000},
        "includeCustomFields": include_custom_fields,
        "includePermissions": include_permissions,
    }

    if status is not None:
        data["status"] = status
    if profile_type is not None:
        data["profileType"] = profile_type
    if updated_after is not None:
        data["updatedAfter"] = updated_after
    if created_after is not None:
        data["createdAfter"] = created_after

    response = self.post(self.api_endpoint + "/v2/Profile/All", data=data)
    yield response["profiles"]

    while (
        response["pagination"]["start"] + response["pagination"]["limit"]
        < response["pagination"]["count"]
    ):
        data["pagination"]["start"] += data["pagination"]["limit"]

        response = self.post(self.api_endpoint + "/v2/Profile/All", data=data)

        yield response["profiles"]


def get_profile(
    self,
    *,
    profile_id: str | None = None,
    external_reference: str | None = None,
    internal_reference: str | None = None,
    badge_reference: str | None = None,
    include_custom_fields: bool = False,
    include_permissions: bool = False,
) -> Profile:
    """
    Returns the user profile specified by the given identifier

    Parameters
    ----------
        `profile_id` (`str`, optional): the profileId of the profile; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the profile; defaults to `None`
        `internal_reference` (`str`, optional): the internalReference of the profile; defaults to `None`
        `badge_reference` (`str`, optional): the badgeReference of the profile; defaults to `None`
        `include_custom_fields` (`bool`, optional): whether to include custom fields for each profile; defaults to `False`
        `include_permissions` (`bool`, optional): whether to include permissions for each profile; defaults to `False`

    Raises
    ------
        `ValueError`: if no identifier is specified
        `EntegyFailedRequestError`: if the API request fails

    Returns
    -------
        `Profile`: the user profile specified by the given identifier
    """
    data = {
        "includeCustomFields": include_custom_fields,
        "includePermissions": include_permissions,
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
        raise ValueError("Please specify an identifier")

    response = self.post(self.api_endpoint + "/v2/Profile/", data=data)

    match response["response"]:
        case 200:
            return response["profile"]
        case 400:
            raise EntegyFailedRequestError("Profile doesn't exist")
        case _:
            raise EntegyFailedRequestError(
                f"{response['response']}: {response.get('message', 'Unknown error')}"
            )


def delete_profile(
    self,
    *,
    profile_id: str | None = None,
    external_reference: str | None = None,
    internal_reference: str | None = None,
    badge_reference: str | None = None,
):
    """
    Deletes the user profile specified by the given identifier.

    Parameters
    ----------
        `profile_id` (`str`, optional): the profileId of the profile; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the profile; defaults to `None`
        `internal_reference` (`str`, optional): the internalReference of the profile; defaults to `None`
        `badge_reference` (`str`, optional): the badgeReference of the profile; defaults to `None`

    Raises
    ------
        `ValueError`: if no identifier is specified
        `EntegyFailedRequestError`: if the API request fails
    """
    data = {}

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

    response = self.delete(self.api_endpoint + "/v2/Profile/Delete", data=data)

    match response["response"]:
        case 200:
            return
        case 401:
            raise EntegyFailedRequestError("No profile found")
        case _:
            raise EntegyFailedRequestError(
                f"{response['response']}: {response.get('message', 'Unknown error')}"
            )


def create_profile(self, profile_object: ProfileCreate) -> str:
    """
    Creates the given profile within the Entegy project, returning the newly
    created profileId.

    Parameters
    ----------
        `profile_object` (`ProfileCreate`): a profile object representing the profile to create

    Raises
    ------
        `EntegyFailedRequestError`: if the API request fails

    Returns
    -------
        `str`: profileId of the newly created profile
    """
    data = {"profile": profile_object}

    response = self.post(self.api_endpoint + "/v2/Profile/Create", data=data)

    match response["response"]:
        case 200:
            return response["profileId"]
        case 400:
            raise EntegyFailedRequestError("Invalid custom field key or value")
        case 401:
            raise EntegyFailedRequestError("Missing required Field")
        case 402:
            raise EntegyFailedRequestError("Missing profile type")
        case 404:
            raise EntegyFailedRequestError("Profile has duplicate email")
        case 405:
            raise EntegyFailedRequestError("Badge reference is not unique")
        case 406:
            raise EntegyFailedRequestError("External reference is not unique")
        case 407:
            raise EntegyFailedRequestError("Access code is invalid or not unique")
        case 408:
            raise EntegyFailedRequestError("Project not set to use Profile Passwords")
        case 409:
            raise EntegyFailedRequestError(
                "Profile password doesn't meet password requirements"
            )
        case 410:
            raise EntegyFailedRequestError(
                "Parent profile already has a parent - profile hierarchy is limited to one level"
            )
        case _:
            raise EntegyFailedRequestError(
                f"{response['response']}: {response.get('message', 'Unknown error')}"
            )


def update_profile(
    self,
    profile_object: ProfileUpdate,
    *,
    profile_id: str | None = None,
    external_reference: str | None = None,
    internal_reference: str | None = None,
    badge_reference: str | None = None,
):
    """
    Updates the user profile specified by the given identifier using the fields
    in the given profile object.

    Parameters
    ----------
        `profile_object` (`ProfileUpdate`): the profile fields to update
        `profile_id` (`str`, optional): the profileId of the profile; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the profile; defaults to `None`
        `internal_reference` (`str`, optional): the internalReference of the profile; defaults to `None`
        `badge_reference` (`str`, optional): the badgeReference of the profile; defaults to `None`

    Raises
    ------
        `ValueError`: if no identifier is specified
        `EntegyFailedRequestError`: if the API request fails
    """
    data = {"profile": profile_object}

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

    response = self.post(self.api_endpoint + "/v2/Profile/Update", data=data)

    match response["response"]:
        case 200:
            return
        case 401:
            raise EntegyFailedRequestError("No profile found")
        case 402:
            raise EntegyFailedRequestError("Nothing given to change")
        case 404:
            raise EntegyFailedRequestError("Profile has duplicate email")
        case 405:
            raise EntegyFailedRequestError("Badge reference is not unique")
        case 406:
            raise EntegyFailedRequestError("External reference is not unique")
        case 408:
            raise EntegyFailedRequestError("Project not set to use Profile Passwords")
        case 409:
            raise EntegyFailedRequestError(
                "Profile password doesn't meet password requirements"
            )
        case 410:
            raise EntegyFailedRequestError(
                "Parent profile already has a parent - profile hierarchy is limited to one level"
            )
        case _:
            raise EntegyFailedRequestError(
                f"{response['response']}: {response.get('message', 'Unknown error')}"
            )


def sync_profiles(
    self,
    update_reference_type: ProfileIdentifier,
    profiles: list[Profile],
    *,
    group_by_first_profile: bool = False,
) -> list[dict[str, str | bool]]:
    """
    Updates or creates profiles in bulk.

    Parameters
    ----------
        `update_reference_type` (`Identifier`): the identifier to use to match profiles for updating
        `profiles` (`list[Profile]`): the list of profiles to create or update
        `group_by_first_profile` (`bool`, optional): whether the parent profile of all profiles in this sync should be set to the first profile in the profiles list (except the first profile itself, which will be set to have no parent); defaults to `False`

    Raises
    ------
        `EntegyFailedRequestError`: if the API request fails

    Returns
    -------
        `dict[str, list]`: a dictionary containing the results of the sync and any errors
    """
    data = {
        "updateReferenceType": update_reference_type,
        "profiles": profiles,
        "groupByFirstProfile": group_by_first_profile,
    }

    response = self.post(self.api_endpoint + "/v2/Profile/Sync", data=data)

    match response["response"]:
        case 200:
            return {"results": response["results"]}
        case 201:
            return {"results": response["results"], "errors": response["errors"]}
        case 400:
            raise EntegyFailedRequestError("Multiple errors detected")
        case 401:
            raise EntegyFailedRequestError("Nothing given to update")
        case 402:
            raise EntegyFailedRequestError("Exceeded maximum profile update limit")
        case 404:
            raise EntegyFailedRequestError("Invalid updateReferenceType")
        case 500:
            raise EntegyServerError("Internal server error")
        case _:
            raise EntegyFailedRequestError(
                f"{response['response']}: {response.get('message', 'Unknown error')}"
            )


def send_welcome_email(
    self,
    *,
    profile_id: str | None = None,
    external_reference: str | None = None,
    internal_reference: str | None = None,
    badge_reference: str | None = None,
):
    """
    Re-sends the welcome email for a given profile on a given project.

    Parameters
    ----------
        `profile_id` (`str`, optional): the profileId of the profile; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the profile; defaults to `None`
        `internal_reference` (`str`, optional): the internalReference of the profile; defaults to `None`
        `badge_reference` (`str`, optional): the badgeReference of the profile; defaults to `None`

    Raises
    ------
        `ValueError`: if no identifier is specified
    """
    data = {"profileId": profile_id}

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

    response = self.post(self.api_endpoint + "/v2/Profile/SendWelcomeEmail", data=data)

    match response["response"]:
        case 200:
            return
        case 401:
            raise EntegyFailedRequestError("No profile found")
        case _:
            raise EntegyFailedRequestError(
                f"{response['response']}: {response.get('message', 'Unknown error')}"
            )