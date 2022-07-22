import requests, json


def externalAuthentication(self, profileID: str, deviceID: str, requestVersion: int = 1):
    """
    Authenticate a user's login via an external system

    Arguments:
        profileID -- The profile ID of the user

        deviceID -- The device ID of the user's device

        requestVersion -- The version of the request (default 1)
    Returns:
        firstLogin (bool) -- Indicates whether this is the first time this profile has logged into the Entegy system
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "profileId": profileID,
        "deviceId": deviceID,
        "requestVersion": requestVersion,
    }
    resp = requests.post(
        self.APIEndpoint + "/v2/Authentication/ExternalProfile",
        headers=self.headers,
        data=json.dumps(data),
    )
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output
