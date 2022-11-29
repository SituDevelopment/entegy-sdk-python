from typing import Any

Profile: type = dict[str, any]


def all_profiles(self, *, params: dict = {}) -> dict[str, Any]:
    """
    Return all user profiles

    Parameters
    ----------
        `params` (`dict`, optional): any parameters to filter the returned profile by; defaults to `{}`

    Returns
    -------
        `dict[str, Any]`: all user profiles
    """
    profiles: list[Profile] = []

    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "pagination": {
            "start": 0,
            "limit": 1000
        },
    }

    data.update(params)

    response = self.post(
        self.api_endpoint + "/v2/Profile/All",
        headers=self.headers,
        data=data
    )
    profiles.extend(response["profiles"])

    while response["pagination"]["start"] + response["pagination"]["limit"] \
            < response["pagination"]["count"]:
        data["pagination"]["start"] += data["pagination"]["limit"]

        response = self.post(
            self.api_endpoint + "/v2/Profile/All",
            headers=self.headers,
            data=data
        )
        profiles.extend(response["profiles"])

    return {"profiles": profiles}


def get_profile(
    self,
    *,
    profile_id: str = "",
    external_reference: str = None,
    badge_reference: str = None,
    internal_reference: str = None,
    params: dict = {},
) -> dict[str, Any]:
    """
    Get user profile from ID

    Parameters
    ----------
        `profile_id` (`str`, optional): the profileId of the profile; defaults to `""`
        `external_reference` (`str`, optional): the externalReference of the profile; defaults to `None`
        `badgeReference` (`str`, optional): the badgeReference of the profile; defaults to `None`
        `internalReference` (`str`, optional): the internalReference of the profile; defaults to `None`
        `params` (`dict`, optional): any parameters to filter the returned profile by; defaults to `{}`

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "profileId": profile_id
    }

    if external_reference is not None:
        data.update({"externalReference": external_reference})
    if badge_reference is not None:
        data.update({"badgeReference": badge_reference})
    if internal_reference is not None:
        data.update({"internalReference": internal_reference})

    data.update(params)

    return self.post(
        self.api_endpoint + "/v2/Profile/",
        headers=self.headers,
        data=data
    )


def delete_profile(self, profile_id: str) -> dict[str, Any]:
    """
    Deletes a profile. Once deleted this data is unrecoverable. Any data
    associated with the profile such as profile links will also be deleted.

    Parameters
    ----------
        `profile_id` (`str`): the profileId of the profile

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "profileId": profile_id
    }

    return self.delete(
        self.api_endpoint + "/v2/Profile/Delete",
        headers=self.headers,
        data=data
    )


def create_profile(self, profile_object: Profile) -> dict[str, Any]:
    """
    Creates a profile in the Entegy system.

    Parameters
    ----------
        `profile_object` (`Profile`): a profile object representing the profile you want to create

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "profile": profile_object,
    }

    return self.post(
        self.api_endpoint + "/v2/Profile/Create",
        headers=self.headers,
        data=data
    )


def update_profile(
    self,
    profile_id: str,
    profile_object: Profile
) -> dict[str, Any]:
    """
    Update (modify) an existing profile in the system. To update an existing
    profile, you must provide one valid reference to a profile and a Profile
    Object.

    All fields in the profile object are optional, and are only updated if the
    key is present and the value is non null. Providing an empty string for a
    key will try to set it to an empty string for all fields except firstName and lastName

    Parameters
    ----------
        `profile_id` (`str`): the profileId of the profile to update
        `profile_object` (`Profile`): the profile containing the fields you want to update

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "profileID": profile_id,
        "profile": profile_object,
    }

    return self.post(
        self.api_endpoint + "/v2/Profile/Update",
        headers=self.headers,
        data=data
    )


def sync_profiles(
    self,
    update_reference_type: str,
    profiles: list[Profile],
    *,
    group_by_first_profile: bool = False
) -> dict[str, Any]:
    """
    Allows you to update (modify) or create 100 or less profiles in the system.

    For updating all fields in the profile object are optional, and are only
    updated if the key is present and the value is non null. Providing an empty
    string for a key will try to set it to an empty string for all fields except
    firstName and lastName

    For creating, `firstName`, `lastName` and `type` are required. All other
    fields are optional.

    Parameters
    ----------
        `update_reference_type` (`str`): the identifier to use to match profiles for updating. `profileId`, `internalReference`, `external_reference` or `badgeReference`
        `profiles` (`list[Profile]`): the list of profiles you want to create or update
        `group_by_first_profile` (`bool`, optional): if true the parent profile of all profiles in this sync will be set to the first profile in the profiles list (except the first profile itself, which will be set to have no parent); defaults to `False`

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "updateReferenceType": update_reference_type,
        "profiles": profiles,
    }

    return self.post(
        self.api_endpoint + "/v2/Profile/Sync",
        headers=self.headers,
        data=data
    )


def send_welcome_email(self, profile_id: str) -> dict[str, Any]:
    """
    Re-sends the welcome email for a given profile on a given project.

    Parameters
    ----------
        `profile_iD` (`str`): the profileId of the profile you want to update

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "profileID": profile_id,
    }

    return self.post(
        self.api_endpoint + "/v2/Profile/SendWelcomeEmail",
        headers=self.headers,
        data=data
    )
