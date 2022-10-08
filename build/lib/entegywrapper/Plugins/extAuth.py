import requests
import json


def externalAuthentication(
    self, profileID: str, deviceID: str, requestVersion: int = 1
):
    """
    Authenticate a user's login via an external system.

    Parameters
    ----------
        `profileID` (`str`): the profile ID that is logging in
        `deviceID` (`int`): the device ID that is logging in
        `requestVersion` (`int`): the version of the request; defaults to 1

    Returns
    -------
        `bool`: indicates whether this is the first time this profile has logged into the Entegy system
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "profileId": profileID,
        "deviceId": deviceID,
        "requestVersion": requestVersion,
    }

    resp = self.post(
        self.APIEndpoint + "/v2/Authentication/ExternalProfile",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output
