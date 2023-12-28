from entegywrapper.errors import EntegyFailedRequestError
from entegywrapper.schemas.profile import CustomProfileField


def get_profile_custom(self, key: str) -> CustomProfileField:
    """
    Returns the custom field specified by the given key.

    Parameters
    ----------
        `key` (`str`): the key of the custom field to return

    Raises
    ------
        `EntegyFailedRequestError`: if the API request fails

    Returns
    -------
        `CustomProfileField`: the custom field specified by the given key
    """
    data = {"key": key}

    response = self.post(self.api_endpoint + "/v2/ProfileCustomField", data=data)

    match response["response"]:
        case 200:
            return response["customField"]
        case 401:
            raise EntegyFailedRequestError("Key doesn't exist")


def create_profile_custom(self, custom_field: CustomProfileField):
    """
    Creates a new custom field for profiles.

    Parameters
    ----------
        `custom_field` (`CustomProfileField`): the custom field to create

    Raises
    ------
        `EntegyFailedRequestError`: if the API request fails
    """
    data = {"customField": custom_field}

    response = self.post(self.api_endpoint + "/v2/ProfileCustomField/Create", data=data)

    match response["response"]:
        case 200:
            return
        case 402:
            raise EntegyFailedRequestError("Malformed field input")
        case 404:
            raise EntegyFailedRequestError("Invalid name")
        case 405:
            raise EntegyFailedRequestError("Key is not unique")
        case 406:
            raise EntegyFailedRequestError("Key is not valid")
        case 407:
            raise EntegyFailedRequestError("Exhausted number of text fields allowed")


def update_profile_custom(self, key: str, custom_field: CustomProfileField):
    """
    Updates the custom profile field specified by the given key with data from
    the given custom field.

    Parameters
    ----------
        `key` (`str`): the key of the custom field to update

        `custom_field` (`CustomProfileField`): the fields to update

    Raises
    ------
        `EntegyFailedRequestError`: if the API request fails
    """
    data = {"key": key, "customField": custom_field}

    response = self.post(self.api_endpoint + "/v2/ProfileCustomField/Update", data=data)

    match response["response"]:
        case 200:
            return
        case 401:
            raise EntegyFailedRequestError("Key doesn't exist")
        case 402:
            raise EntegyFailedRequestError("Invalid name")
        case 404:
            raise EntegyFailedRequestError("Key is not unique")
        case 405:
            raise EntegyFailedRequestError("Key is not valid")
        case 406:
            raise EntegyFailedRequestError("Exhausted number of text fields allowed")
        case _:
            raise EntegyFailedRequestError(
                f"{response['response']}: {response.get('message', 'Unknown error')}"
            )


def delete_profile_custom(self, key: str):
    """
    Deletes a custom field.

    Parameters
    ----------
        `key` (`str`): the key of the custom field to delete

    Raises
    ------
        `EntegyFailedRequestError`: if the API request fails
    """
    data = {"key": key}

    response = self.delete(
        self.api_endpoint + "/v2/ProfileCustomField/Delete", data=data
    )

    match response["response"]:
        case 200:
            return
        case 401:
            raise EntegyFailedRequestError("Key doesn't exist")
        case _:
            raise EntegyFailedRequestError(
                f"{response['response']}: {response.get('message', 'Unknown error')}"
            )


def all_profile_custom(self) -> list[CustomProfileField]:
    """
    Returns a list all custom fields.

    Returns
    -------
        `list[CustomProfileField]`: all custom fields
    """
    data = {}

    response = self.post(self.api_endpoint + "/v2/ProfileCustomField/All", data=data)

    return response["customFields"]
