import json


def awardPoints(
    self,
    pointEvent: str,
    points: int,
    profileId: str = "",
    externalReference: str = None,
    badgeReference: str = None,
    internalReference: str = None,
):
    """
    Allows you to give points to a profile.

    Parameters
    ----------
        `pointEvent` (`str`): the types of points you're assigning
        `points` (`int`): the amount of points you're assigning
        `profileId` (`str`): the profileId for the profile
        `externalReference` (`str`): the externalReference of the profile
        `badgeReference` (`str`): the badgeReference of the profile
        `internalReference` (`str`): the internalReference of the profile

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "profileId": profileId,
        "pointEvent": pointEvent,
        "points": points,
    }

    if externalReference != None:
        data.update({"externalReference": profileId})
    if badgeReference != None:
        data.update({"badgeReference": profileId})
    if internalReference != None:
        data.update({"internalReference": profileId})

    resp = self.post(
        self.APIEndpoint + "/v2/Point/Award",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No reponse received from API")

    output = resp.json()
    return output


def getPoints(
    self,
    profileId: str = "",
    externalReference: str = None,
    badgeReference: str = None,
    internalReference: str = None
):
    """
    Returns the amount of points a profile has.

    Parameters
    ----------
        `profileId` (`str`): the profileId for the profile
        `externalReference` (`str`): the externalReference of the profile
        `badgeReference` (`str`): the badgeReference of the profile
        `internalReference` (`str`): the internalReference of the profile

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
        data.update({"externalReference": profileId})
    if badgeReference != None:
        data.update({"badgeReference": profileId})
    if internalReference != None:
        data.update({"internalReference": profileId})

    resp = self.post(
        self.APIEndpoint + "/v2/Point/Earned",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No reponse received from API")

    output = resp.json()
    return output


def getPointLeaderboard(
    self
):
    """
    Allows you to see the leaderboard for the project. The response is sorted
    by the profiles response and includes their position with ties correctly
    handled.

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey()
    }

    resp = self.post(
        self.APIEndpoint + "/v2/Point/Leaderboard",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No reponse received from API")

    output = resp.json()
    return output
