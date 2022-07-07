import requests, json


def getProfileType(self, name):
    """
    This request will get a single profile type

    Arguments:
        name -- The name of the profile type

    Returns:
        The requested profile"""

    data = {"projectId": self.projectID, "apiKey": self.getKey(), "name": name}
    print(data)
    resp = requests.post(
        self.APIEndpoint + "/v2/ProfileType",
        headers=self.headers,
        data=json.dumps(data),
    )
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output


def createProfileType(self, profileType):
    """
    Creates a ProfileType with the data passed in the profileType

    Arguments:
        profileType -- The data for the profile type you're creating

        e.g.
        {
            "name":"Exhibitor",
            "externalReference":"au-ref-tickettype-564545"
        }

    Returns:
        Base response object"""

    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "profileType": profileType,
    }
    print(data)
    resp = requests.post(
        self.APIEndpoint + "/v2/ProfileType/Create",
        headers=self.headers,
        data=json.dumps(data),
    )
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output


def updateProfileType(self, name, profileType):
    """
    Updates the ProfileType with the data passed in the profileType

    Arguments:
        name -- The name of the profile type

        profileType -- The data you wish to update

        e.g.

        {
            "externalReference":"au-ref-tickettype-564545"
        }

    Returns:
        Base response object"""

    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "name": name,
        "profileType": profileType,
    }
    print(data)
    resp = requests.post(
        self.APIEndpoint + "/v2/ProfileType/Update",
        headers=self.headers,
        data=json.dumps(data),
    )
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output


def deleteProfileType(self, name):
    """
    Deletes a profile type. The type cannot be in use.

    Arguments:
        name -- The name of the profile type

    Returns:
        Base response object"""

    data = {"projectId": self.projectID, "apiKey": self.getKey(), "name": name}
    print(data)
    resp = requests.delete(
        self.APIEndpoint + "/v2/ProfileType/Delete",
        headers=self.headers,
        data=json.dumps(data),
    )
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output


def allProfileTypes(self):
    """
    This request will get all profile types

    Returns:
        All profileTypes"""

    data = {"projectId": self.projectID, "apiKey": self.getKey()}
    print(data)
    resp = requests.post(
        self.APIEndpoint + "/v2/ProfileType/All",
        headers=self.headers,
        data=json.dumps(data),
    )
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output
