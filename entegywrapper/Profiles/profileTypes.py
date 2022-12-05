from entegywrapper.schemas.profile import ProfileType


def get_profile_type(
    self,
    *,
    name: str | None = None,
    external_reference: str | None = None
) -> ProfileType:
    """
    Returns the profile type specified by the given identifier.

    Parameters
    ----------
        `name` (`str`, optional): the name of the profile type; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the profile type; defaults to `None`

    Raises
    ------
        `ValueError`: if no identifier is specified

    Returns
    -------
        `ProfileType`: the profile type specified by the given identifier
    """
    data = {}

    if name is not None:
        data["name"] = name
    elif external_reference is not None:
        data["externalReference"] = external_reference
    else:
        raise ValueError("Please specify an identifier")

    response = self.post(
        self.api_endpoint + "/v2/ProfileType",
        data=data
    )

    return response["profileType"]


def create_profile_type(self, profile_type: ProfileType):
    """
    Creates a profile type from the given data.

    Parameters
    ----------
        `profile_type` (`ProfileType`): the data for the profile type to create
    """
    data = {
        "profileType": profile_type
    }

    self.post(
        self.api_endpoint + "/v2/ProfileType/Create",
        data=data
    )


def update_profile_type(
    self,
    profile_type: ProfileType,
    *,
    name: str | None = None,
    external_reference: str | None = None
):
    """
    Updates the profile type with the data passed in the profileType

    Parameters
    ----------
        `profile_type` (`ProfileType`): the data to update
        `name` (`str`, optional): the name of the profile type; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the profile type; defaults to `None`

    Raises
    ------
        `ValueError`: if no identifier is specified
    """
    data = {
        "profileType": profile_type
    }

    if name is not None:
        data["name"] = name
    elif external_reference is not None:
        data["externalReference"] = external_reference
    else:
        raise ValueError("Please specify an identifier")

    self.post(
        self.api_endpoint + "/v2/ProfileType/Update",
        data=data
    )


def delete_profile_type(
    self,
    *,
    name: str | None = None,
    external_reference: str | None = None
):
    """
    Deletes a profile type. The type cannot be in use.

    Parameters
    ----------
        `name` (`str`, optional): the name of the profile type; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the profile type; defaults to `None`

    Raises
    ------
        `ValueError`: if no identifier is specified
    """
    data = {}

    if name is not None:
        data["name"] = name
    elif external_reference is not None:
        data["externalReference"] = external_reference
    else:
        raise ValueError("Please specify an identifier")

    self.delete(
        self.api_endpoint + "/v2/ProfileType/Delete",
        data=data
    )


def all_profile_types(self) -> list[ProfileType]:
    """
    Returns a list of all profile types.

    Returns
    -------
        `list[ProfileType]`: all profile types
    """
    data = {}

    response = self.post(
        self.api_endpoint + "/v2/ProfileType/All",
        data=data
    )

    return response["profileTypes"]
