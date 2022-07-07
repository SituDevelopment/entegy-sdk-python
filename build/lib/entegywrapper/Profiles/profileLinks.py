import requests, json


def selectedProfileLinks(self, profileId, returnLimit=100):
    """
    Return all the profile links the profile ha

    Arguments:
        profileId -- User profile ID

        returnLimit -- The index and amount of results to return, if not provided is defaulted to 0 and 100

    Returns:
        Base response object
    """
    data = {"projectId": self.projectID, "apiKey": self.getKey(), "profileID": profileId}

    resp = requests.post(
        self.APIEndpoint + "/v2/ProfileLink/Selected/",
        headers=self.headers,
        data=json.dumps(data),
    )
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output


def pageProfileLinks(self, templateType, moduleId, returnLimit=100):
    """
    Gets all the profiles linked to a Content Page

    Arguments:
        templateType -- The templateType of the page

        moduleId -- The moduleId of the page

        returnLimit -- The index and amount of results to return, if not provided is defaulted to 0 and 100

    Returns:
        Pagination response and list of profile objects
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "templateType": templateType,
        "moduleId": moduleId,
    }

    resp = requests.post(
        self.APIEndpoint + "/v2/ProfileLink/Page/",
        headers=self.headers,
        data=json.dumps(data),
    )
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output


def selectProfileLink(self, profileId, link):
    """
    Allows you to select a link for a profile

    Arguments:
        profileId -- User profile ID

        link -- The link you wish to select

        e.g.

        {
            "templateType":"session",
            "moduleId":1
        }

    Returns:
        Base response object
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "profileID": profileId,
        "link": link,
    }

    resp = requests.post(
        self.APIEndpoint + "/v2/ProfileLink/Select/",
        headers=self.headers,
        data=json.dumps(data),
    )
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output


def multiSelectProfileLinks(self, profiles):
    """
    Allows you to select multiple pages on multiple profiles at once

    Arguments:
        profiles-- 	A list of profile references with link objects within. Refer to the example JSON

        e.g.

        [{
            "profileId":"ff11c742-346e-4874-9e24-efe6980a7453",
            "links":[
            {
                "templateType":"sesSiOn",
                "moduleId":1
            },
            {
                "templateType":"sesSiOn",
                "moduleId":2
            },
            {
                "templateType":"sesSiOn",
                "moduleId":3
            }]
        },
        {
            "profileId":"3e7026f6-cb67-452b-b962-125731807855",
            "links":[
            {
                "templateType":"sesSiOn",
                "moduleId":4
            },
            {
                "templateType":"sesSiOn",
                "moduleId":2
            },
            {
                "templateType":"sesSiOn",
                "moduleId":3
            }]
        }]

    Returns:
        Base response object
    """
    data = {"projectId": self.projectID, "apiKey": self.getKey(), "profiles": profiles}

    resp = requests.post(
        self.APIEndpoint + "/v2/ProfileLink/MultiSelect/",
        headers=self.headers,
        data=json.dumps(data),
    )
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output


def deSelectProfileLinks(self, profileId, link):
    """
    Allows you to deselect a link for a profile

    Arguments:
        profileId -- The profileId of the profile

        link -- The link you wish to select

        e.g.

        {
            "templateType":"session",
            "moduleId":1
        }

    Returns:
        Base response object
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "profileId": profileId,
        "link": link,
    }

    resp = requests.post(
        self.APIEndpoint + "/v2/ProfileLink/Deselect/",
        headers=self.headers,
        data=json.dumps(data),
    )
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output


def clearProfileLinks(self, profileId, templateType):
    """
    Allows you to clear all the selected links of a templateType on a single profile

    Arguments:
        profileId -- The profileId of the profile

        templateType -- The templateType to clear links of

    Returns:
        Base response object
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "profileId": profileId,
        "templateType": templateType,
    }

    resp = requests.post(
        self.APIEndpoint + "/v2/ProfileLink/Clear/",
        headers=self.headers,
        data=json.dumps(data),
    )
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output
