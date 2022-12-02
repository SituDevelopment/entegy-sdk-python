from entegywrapper.entegySchemas.profile import CustomProfileField


def get_profile_custom(self, key: str) -> CustomProfileField:
    """
    Returns the custom field specified by the given key.

    Parameters
    ----------
        `key` (`str`): the key of the custom field to return

    Returns
    -------
        `CustomProfileField`: the custom field specified by the given key
    """
    data = {
        "key": key
    }

    response = self.post(
        self.api_endpoint + "/v2/ProfileCustomField",
        headers=self.headers,
        data=data
    )

    return response["customField"]


def create_profile_custom(
    self,
    custom_field: CustomProfileField
):
    """
    Creates a new custom field for profiles.

    Parameters
    ----------
        `custom_field` (`CustomProfileField`): the custom field to create
    """
    data = {
        "customField": custom_field
    }

    self.post(
        self.api_endpoint + "/v2/ProfileCustomField/Create",
        headers=self.headers,
        data=data
    )


def update_profile_custom(
    self,
    key: str,
    custom_field: CustomProfileField
):
    """
    Updates the custom profile field specified by the given key with data from
    the given custom field.

    Parameters
    ----------
        `key` (`str`): the key of the custom field to update
        `custom_field` (`CustomProfileField`): the fields to update
    """
    data = {
        "key": key,
        "customField": custom_field
    }

    self.post(
        self.api_endpoint + "/v2/ProfileCustomField/Update",
        headers=self.headers,
        data=data
    )


def delete_profile_custom(self, key: str):
    """
    Deletes a custom field.

    Parameters
    ----------
        `key` (`str`): the key of the custom field to delete
    """
    data = {
        "key": key
    }

    self.delete(
        self.api_endpoint + "/v2/ProfileCustomField/Delete",
        headers=self.headers,
        data=data
    )


def all_profile_custom(self) -> list[CustomProfileField]:
    """
    Returns a list all custom fields.

    Returns
    -------
        `list[CustomProfileField]`: all custom fields
    """
    data = {}

    response = self.post(
        self.api_endpoint + "/v2/ProfileCustomField/All",
        headers=self.headers,
        data=data
    )

    return response["customFields"]
