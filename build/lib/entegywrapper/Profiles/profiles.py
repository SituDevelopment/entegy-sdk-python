import json
import requests

Profile: type = dict[str, any]


def allProfiles(self, returnLimit: int = 100, params: dict = {}):
    """
    Return all user profiles

    Parameters
    ----------
        `returnLimit` (`int`): the maximum number of results to return; defaults to 100
        `params` (`dict`): any parameters to filter the returned profile by

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "pagination": {
            "start": 0,
            "limit": returnLimit
        },
    }

    data.update(params)

    resp = self.post(
        self.APIEndpoint + "/v2/Profile/All",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output


def getProfile(
    self,
    profileId: str = "",
    externalReference: str = None,
    badgeReference: str = None,
    internalReference: str = None,
    params: dict = {},
):
    """
    Get user profile from ID

    Parameters
    ----------
        `profileId` (`str`): the profileId of the profile
        `externalReference` (`str`): the externalReference of the profile
        `badgeReference` (`str`): the badgeReference of the profile
        `internalReference` (`str`): the internalReference of the profile
        `params` (`dict`): any parameters to filter the returned profile by

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "profileId": profileId
    }

    if externalReference != None:
        data.update({"externalReference": externalReference})
    if badgeReference != None:
        data.update({"badgeReference": badgeReference})
    if internalReference != None:
        data.update({"internalReference": internalReference})

    data.update(params)

    resp = self.post(
        self.APIEndpoint + "/v2/Profile/",
        headers=self.headers,
        data=json.dumps(data)
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output


def deleteProfile(self, profileId: str):
    """
    Deletes a profile. Once deleted this data is unrecoverable. Any data
    associated with the profile such as profile links will also be deleted.

    Parameters
    ----------
        `profileId` (`str`): the profileId of the profile

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "profileId": profileId
    }

    resp = requests.delete(
        self.APIEndpoint + "/v2/Profile/Delete",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output


def createProfile(self, profileObject: Profile):
    """
    Creates a profile in the Entegy system.

    Parameters
    ----------
        `profileObject` (`Profile`): a profile object representing the profile you want to create

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "profile": profileObject,
    }

    resp = self.post(
        self.APIEndpoint + "/v2/Profile/Create",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output


def updateProfile(self, profileID: str, profileObject: Profile):
    """
    Update (modify) an existing profile in the system. To update an existing
    profile, you must provide one valid reference to a profile and a Profile
    Object.

    All fields in the profile object are optional, and are only updated if the
    key is present and the value is non null. Providing an empty string for a
    key will try to set it to an empty string for all fields except firstName and lastName

    Parameters
    ----------
        `profileId` (`str`): the profileId of the profile to update
        `profileObject` (`Profile`): the profile containing the fields you want to update

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "profileID": profileID,
        "profile": profileObject,
    }

    resp = self.post(
        self.APIEndpoint + "/v2/Profile/Update",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output


def syncProfiles(
    self,
    updateReferenceType: str,
    profiles: list[Profile],
    groupByFirstProfile: bool = False
):
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
        `updateReferenceType` (`str`): the identifier to use to match profiles for updating. `profileId`, `internalReference`, `externalReference` or `badgeReference`
        `profiles` (`list[Profile]`): the list of profiles you want to create or update
        `groupByFirstProfile` (`bool`): if true the parent profile of all profiles in this sync will be set to the first profile in the profiles list (except the first profile itself, which will be set to have no parent)

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "updateReferenceType": updateReferenceType,
        "profiles": profiles,
    }

    resp = self.post(
        self.APIEndpoint + "/v2/Profile/Sync",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output


def sendWelcomeEmail(self, profileID):
    """
    Re-sends the welcome email for a given profile on a given project.

    Parameters
    ----------
        `profileID` (`str`): the profileId of the profile you want to update

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "profileID": profileID,
    }

    resp = self.post(
        self.APIEndpoint + "/v2/Profile/SendWelcomeEmail",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output
