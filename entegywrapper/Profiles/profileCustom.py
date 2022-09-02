import requests
import json


def getProfileCustom(self, key):
    """
    This request will get a single custom field

    Arguments:
        key -- The key of the custom field to return

    Returns:
        The requested customField object"""

    data = {"projectId": self.projectID, "apiKey": self.getKey(), "key": key}
    print(data)
    resp = self.post(
        self.APIEndpoint + "/v2/ProfileCustomField",
        data=json.dumps(data)
    )
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output


def createProfileCustom(self, customField):
    """
    Creates a new Custom Field for Profiles.

    There is a limited number of text custom fields allowed per project. Once a custom field is created, it's type cannot be modified.

    Arguments:
        customField -- The custom field you wish to create

        e.g.

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

    Returns:
        Base response object"""

    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "customField": customField,
    }
    print(data)
    resp = self.post(
        self.APIEndpoint + "/v2/ProfileCustomField/Create",
        data=json.dumps(data)
    )
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output


def updateProfileCustom(self, key, customField):
    """
    Update custom profile 'key' with 'customField' data

    Arguments:
        key -- The key of the custom field to return

        customField -- The data to update the field with

        e.g.

        {
            "options":[
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

    Returns:
        The requested customField object"""

    data = {"projectId": self.projectID, "apiKey": self.getKey(), "key": key}
    print(data)
    resp = self.post(
        self.APIEndpoint + "/v2/ProfileCustomField/Update",
        data=json.dumps(data)
    )
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output


def deleteProfileCustom(self, key):
    """
    This request will delete a single custom field

    Arguments:
        key -- The key of the custom field to delete

    Returns:
        Base response object"""

    data = {"projectId": self.projectID, "apiKey": self.getKey(), "key": key}
    print(data)
    resp = requests.delete(
        self.APIEndpoint + "/v2/ProfileCustomField/Delete",
        data=json.dumps(data)
    )
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output


def allProfileCustom(self):
    """
    This request will return all custom fields

    Returns:
        List of all customFields"""

    data = {"projectId": self.projectID, "apiKey": self.getKey()}
    print(data)
    resp = self.post(
        self.APIEndpoint + "/v2/ProfileCustomField/All",
        data=json.dumps(data)
    )
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output
