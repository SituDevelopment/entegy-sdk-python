import json

from typing import Any

CustomField: type = dict[str, str | int | bool]


def get_profile_custom(self, key: str) -> dict[str, Any]:
    """
    Returns a single custom field.

    Parameters
    ----------
        `key` (`str`): the key of the custom field to return

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {"projectId": self.project_id, "apiKey": self.get_key(), "key": key}

    return self.post(
        self.api_endpoint + "/v2/ProfileCustomField",
        headers=self.headers,
        data=json.dumps(data)
    )


def create_profile_custom(self, custom_field: CustomField) -> dict[str, Any]:
    """
    Creates a new Custom Field for Profiles.

    There is a limited number of text custom fields allowed per project. Once a
    custom field is created, it's type cannot be modified.

    Parameters
    ----------
        `custom_field` (`CustomField`): the custom field you wish to create

    The format of `custom_field` is as follows:
    ```python
        {
            "key": "dietary-requirements",
            "name": "Dietary requirements",
            "type": "MultiChoice",
            "options":[
                {
                    "name": "Halal"
                },
                {
                    "name": "Vegan"
                },
                {
                    "name": "Lactose Intolerant"
                },
                {
                    "name": "Gluten Intolerant"
                }
            ]
        }
    ```

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "customField": custom_field,
    }

    return self.post(
        self.api_endpoint + "/v2/ProfileCustomField/Create",
        headers=self.headers,
        data=json.dumps(data)
    )


def update_profile_custom(
    self,
    key: str,
    custom_field: CustomField
) -> dict[str, Any]:
    """
    Updates custom profile field `key` with `customField`'s data.

    Fields are optional, not including them omits them from being updated. You
    can update the field's key by setting a different valid key within the
    ProfileField object you pass in. You can delete multi choice options by
    providing an empty or whitespace only `name` along with it's optionId. A
    null `name` will omit the name from being updated. You can create new
    options by not including an `optionId`. Unlike most endpoints that will
    completely fail when invalid data is input, this endpoint will skip over any
    invalid input and continue to create anything that is valid.

    Parameters
    ----------
        `key` (`str`): the key of the custom field to return
        `custom_field` (`CustomField`): the data to update the field with

    The format of `custom_field` is as follows:
    ```python
        {
            "options": [
                {
                    "optionId": 6,
                    "name": ""
                },
                {
                    "optionId": 7,
                    "name": "Halal"
                },
                {
                    "optionId": 8,
                    "name": "Vegan"
                },
                {
                    "name": "Lactose Intolerant"
                },
                {
                    "name": "Gluten Intolerant"
                }
            ]
        }
    ```

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """

    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "key": key,
        "customField": custom_field
    }

    return self.post(
        self.api_endpoint + "/v2/ProfileCustomField/Update",
        headers=self.headers,
        data=json.dumps(data)
    )


def delete_profile_custom(self, key: str) -> dict[str, Any]:
    """
    Deletes a custom field.

    Parameters
    ----------
        `key` (`str`): the key of the custom field to delete

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "key": key
    }

    return self.delete(
        self.api_endpoint + "/v2/ProfileCustomField/Delete",
        headers=self.headers,
        data=json.dumps(data)
    )


def all_profile_custom(self) -> dict[str, Any]:
    """
    Returns all custom fields.

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key()
    }

    return self.post(
        self.api_endpoint + "/v2/ProfileCustomField/All",
        headers=self.headers,
        data=json.dumps(data)
    )
