def external_authentication(self, profile_id: str, device_id: str) -> bool:
    """
    Authenticates a user's login via an external system.

    Parameters
    ----------
        `profile_id` (`str`): the profileId that is logging in
        `device_id` (`int`): the deviceId that is logging in

    Returns
    -------
        `bool`: whether this is the user's first login
    """
    data = {
        "profileId": profile_id,
        "deviceId": device_id,
        "requestVersion": 1
    }

    response = self.post(
        self.api_endpoint + "/v2/Authentication/ExternalProfile",
        headers=self.headers,
        data=data
    )

    return response["firstLogin"]
