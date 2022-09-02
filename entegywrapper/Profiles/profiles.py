import requests, json


def allProfiles(self, returnLimit=100, params={}):
    """
    Return all user profiles

    Arguments:
        returnLimit -- The index and amount of results to return, if not provided is defaulted to 0 and 100

        params -- Any parameters to filter the returned profile by

    Returns:
        Base response object
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "pagination": {"start": 0, "limit": returnLimit},
    }

    data.update(params)

    resp = self.post(
        self.APIEndpoint + "/v2/Profile/All",
        headers=self.headers,
        data=json.dumps(data),
    )
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output


def getProfile(
    self,
    userID="",
    externalReference=None,
    badgeReference=None,
    internalReference=None,
    params={},
):
    """
    Get user profile from ID

    Arguments:
        userID -- User profile ID

        params -- Any parameters to filter the returned profile by

    Returns:
        User profile JSON output
    """
    data = {"projectId": self.projectID, "apiKey": self.getKey(), "profileId": userID}
    if externalReference != None:
        data.update({"externalReference": externalReference})
    if badgeReference != None:
        data.update({"badgeReference": badgeReference})
    if internalReference != None:
        data.update({"internalReference": internalReference})

    data.update(params)

    resp = self.post(
        self.APIEndpoint + "/v2/Profile/", headers=self.headers, data=json.dumps(data)
    )
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output


def deleteProfile(self, userID):
    """
    Delete user profile from ID

    Arguments:
        userID -- User profile ID

    Returns:
        Base response object
    """
    data = {"projectId": self.projectID, "apiKey": self.getKey(), "profileId": userID}

    resp = requests.delete(
        self.APIEndpoint + "/v2/Profile/Delete",
        headers=self.headers,
        data=json.dumps(data),
    )
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output


def createProfile(self, profileObject):
    """
    Create user profile from profile JSON object

    Arguments:
        profileObject -- User profile JSON object
        e.g.
        {
            "externalReference":"au-prf-31242354253",
            "firstName":"John",
            "lastName":"Smith",
            "type":"Attendee"
            /* rest of profile object (all extra fields are optional)*/
        }

    Returns:
        Reponse code, success/error message, and profileID in JSON format"""

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
        raise Exception("No reponse received from API")
    output = resp.json()
    return output


def updateProfile(self, profileID, profileObject):
    """
    Update user profile from profile JSON object

    Arguments:
        profileID -- User profile ID to update

        profileObject -- User profile JSON object
        e.g.
        {
            "firstName":"Fred",
            "imageUrl":"https://images.example.org/profileimages/fredsmith/image.png"
        }

    Returns:
        Base response object"""

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
        raise Exception("No reponse received from API")
    output = resp.json()
    return output


def syncProfiles(self, updateReferenceType, profiles, groupByFirstProfile=False):
    """
    Sync user profiles with reference to updateReferenceType

    Arguments:
        updateReferenceType -- The identifier to use to match profiles for updating. profileId, internalReference, externalReference, badgeReference

        profiles -- The list of profiles you want to create or update
        e.g.
        [
            {
                "profileId": "ff11c742-346e-4874-9e24-efe6980a7453",
                "customFields":
                {
                    "favourite-Food": "Pizza",
                    "water-Preference": "Cold Water"
                }
            },
            {
                "profileId": "4255a414-d95c-4106-a988-d0e10947ede5",
                "customFields":
                {
                    "favourite-Food": "Pizza",
                    "water-Preference": "Cold Water"
                }
            },
            {
                "firstName": "Test",
                "lastName": "User",
                "type": "attendee",
                "customFields":
                {
                    "favourite-Food": "Pizza",
                    "water-Preference": "Cold Water"
                }
            }
        ]

    groupByFirstProfile	-- If true the parent profile of all profiles in this sync will be set to the first profile in the profiles list (except the first profile itself, which will be set to have no parent)

    Returns:
        This endpoint returns a base response with an array of specific profile results in the same input order as the request"""

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
        raise Exception("No reponse received from API")
    output = resp.json()
    return output


def sendWelcomeEmail(self, profileID):
    """
    Re-sends the welcome email for a given profile on a given project

    Arguments:
        profileID -- The profileId of the profile you want to update

    Returns:
        Base response object"""

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
        raise Exception("No reponse received from API")
    output = resp.json()
    return output
