import json
import requests

ProfileType: type = dict[str, str | int | bool]


def getProfileType(self, name: str):
    """
    Returns a single profile type.

    Parameters
    ----------
        `name` (`str`): the name of the profile type

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "name": name
    }

    resp = self.post(
        self.APIEndpoint + "/v2/ProfileType",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output


def createProfileType(self, profileType: ProfileType):
    """
    Creates a ProfileType with the data passed in the profileType

    Parameters
    ----------
        `profileType` (`ProfileType`): the data for the profile type you're creating

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "profileType": profileType,
    }

    resp = self.post(
        self.APIEndpoint + "/v2/ProfileType/Create",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output


def updateProfileType(self, name: str, profileType: ProfileType):
    """
    Updates the ProfileType with the data passed in the profileType

    Parameters
    ----------
        `name` (`str`): the name of the profile type
        `profileType` (`ProfileType`): the data you wish to update

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "name": name,
        "profileType": profileType,
    }

    resp = self.post(
        self.APIEndpoint + "/v2/ProfileType/Update",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output


def deleteProfileType(self, name):
    """
    Deletes a profile type. The type cannot be in use.

    Parameters
    ----------
        `name` (`str`): the name of the profile type

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "name": name
    }

    resp = requests.delete(
        self.APIEndpoint + "/v2/ProfileType/Delete",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output


def allProfileTypes(self):
    """
    Returns all profile types.

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey()
    }

    resp = self.post(
        self.APIEndpoint + "/v2/ProfileType/All",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output
