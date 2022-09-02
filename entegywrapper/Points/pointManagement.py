import json


def awardPoints(
    self,
    pointEvent: str,
    points: int,
    userID="",
    externalReference=None,
    badgeReference=None,
    internalReference=None,
):
    """
    Give points to a profile

    Arguments:
        pointEvent -- The types of points you're assigning (https://situ.entegysuite.com.au/Docs/Api/point-constants#pointtypes)
        points -- The amount of points you're assigning
        userID -- User profile ID

    Returns:
        Base response object
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "profileId": userID,
        "pointEvent": pointEvent,
        "points": points,
    }

    if externalReference != None:
        data.update({"externalReference": userID})
    if badgeReference != None:
        data.update({"badgeReference": userID})
    if internalReference != None:
        data.update({"internalReference": userID})

    resp = self.post(
        self.APIEndpoint + "/v2/Point/Award",
        data=json.dumps(data)
    )
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output


def getPoints(
    self, userID="", externalReference=None, badgeReference=None, internalReference=None
):
    """
    Get the amount of points a profile has

    Arguments:
        userID -- User profile ID

    Returns:
        Base response object
    """
    data = {"projectId": self.projectID,
            "apiKey": self.getKey(), "profileId": userID}

    if externalReference != None:
        data.update({"externalReference": userID})
    if badgeReference != None:
        data.update({"badgeReference": userID})
    if internalReference != None:
        data.update({"internalReference": userID})

    resp = self.post(
        self.APIEndpoint + "/v2/Point/Earned",
        data=json.dumps(data)
    )
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output


def getPointLeaderboard(self):
    """
    Get the entire leaderboard for the given project

    Returns:
        Leaderboard object
    """
    data = {"projectId": self.projectID, "apiKey": self.getKey()}

    resp = self.post(
        self.APIEndpoint + "/v2/Point/Leaderboard",
        data=json.dumps(data)
    )
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output
