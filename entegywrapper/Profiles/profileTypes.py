import json

from typing import Any

ProfileType: type = dict[str, str | int | bool]


def get_profile_type(self, name: str) -> dict[str, Any]:
    """
    Returns a single profile type.

    Parameters
    ----------
        `name` (`str`): the name of the profile type

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "name": name
    }

    return self.post(
        self.api_endpoint + "/v2/ProfileType",
        headers=self.headers,
        data=json.dumps(data)
    )


def create_profile_type(self, profile_type: ProfileType) -> dict[str, Any]:
    """
    Creates a ProfileType with the data passed in the profileType.

    Parameters
    ----------
        `profile_type` (`ProfileType`): the data for the profile type you're creating

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "profileType": profile_type,
    }

    return self.post(
        self.api_endpoint + "/v2/ProfileType/Create",
        headers=self.headers,
        data=json.dumps(data)
    )


def update_profile_type(
    self,
    name: str,
    profile_type: ProfileType
) -> dict[str, Any]:
    """
    Updates the ProfileType with the data passed in the profileType

    Parameters
    ----------
        `name` (`str`): the name of the profile type
        `profile_type` (`ProfileType`): the data you wish to update

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "name": name,
        "profileType": profile_type,
    }

    return self.post(
        self.api_endpoint + "/v2/ProfileType/Update",
        headers=self.headers,
        data=json.dumps(data)
    )


def delete_profile_type(self, name: str) -> dict[str, Any]:
    """
    Deletes a profile type. The type cannot be in use.

    Parameters
    ----------
        `name` (`str`): the name of the profile type

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "name": name
    }

    return self.delete(
        self.api_endpoint + "/v2/ProfileType/Delete",
        headers=self.headers,
        data=json.dumps(data)
    )


def all_profile_types(self) -> dict[str, Any]:
    """
    Returns all profile types.

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key()
    }

    return self.post(
        self.api_endpoint + "/v2/ProfileType/All",
        headers=self.headers,
        data=json.dumps(data)
    )
