import requests
import json

CustomField: type = dict[str, str | int | bool]


def getProfileCustom(self, key: str):
    """
    Returns a single custom field.

    Parameters
    ----------
        `key` (`str`): the key of the custom field to return

    Returns
    -------
        `dict`: API response JSON
    """
    data = {"projectId": self.projectID, "apiKey": self.getKey(), "key": key}

    resp = self.post(
        self.APIEndpoint + "/v2/ProfileCustomField",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No reponse received from API")

    output = resp.json()
    return output


def createProfileCustom(self, customField: CustomField):
    """
    Creates a new Custom Field for Profiles.

    There is a limited number of text custom fields allowed per project. Once a
    custom field is created, it's type cannot be modified.

    Parameters
    ----------
        `customField` (`CustomField`): the custom field you wish to create

    The format of `` is as follows:
    ```python
        {
            "key":"dietary-requirements",
            "name":"Dietary requirements",
            "type":"MultiChoice",
            "options":[
                {
                    "name":"Halal"
                },
                {
                    "name":"Vegan"
                },
                {
                    "name":"Lactose Intolerant"
                },
                {
                    "name":"Gluten Intolerant"
                }
            ]
        }
    ```

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "customField": customField,
    }

    resp = self.post(
        self.APIEndpoint + "/v2/ProfileCustomField/Create",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()

    return output


def updateProfileCustom(self, key: str, customField: CustomField):
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
        `customField` (`CustomField`): the data to update the field with

    The format of `customField` is as follows:
    ```python
        {
            "options": [
                {
                    "optionId": 6,
                    "name":""
                },
                {
                    "optionId": 7,
                    "name":"Halal"
                },
                {
                    "optionId": 8,
                    "name":"Vegan"
                },
                {
                    "name":"Lactose Intolerant"
                },
                {
                    "name":"Gluten Intolerant"
                }
            ]
        }
    ```

    Returns
    -------
        `dict`: API response JSON
    """

    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "key": key,
        "customField": customField
    }

    resp = self.post(
        self.APIEndpoint + "/v2/ProfileCustomField/Update",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()

    return output


def deleteProfileCustom(self, key: str):
    """
    Deletes a custom field.

    Parameters
    ----------
        `key` (`str`): the key of the custom field to delete

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "key": key
    }

    resp = requests.delete(
        self.APIEndpoint + "/v2/ProfileCustomField/Delete",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output


def allProfileCustom(self):
    """
    Returns all custom fields.

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey()
    }

    resp = self.post(
        self.APIEndpoint + "/v2/ProfileCustomField/All",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output
