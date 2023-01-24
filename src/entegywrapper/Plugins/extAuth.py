from entegywrapper.errors import EntegyFailedRequestError


def external_authentication(self, profile_id: str, device_id: str) -> dict:
    """
    Authenticates a user's login via an external system.

    Parameters
    ----------
        `profile_id` (`str`): the profileId that is logging in
        `device_id` (`int`): the deviceId that is logging in

    Returns
    -------
        `dict`: the response from the API
    """
    data = {"profileId": profile_id, "deviceId": device_id, "requestVersion": 1}

    response = self.post(
        self.api_endpoint + "/v2/Authentication/ExternalProfile", data=data
    )

    match response["response"]:
        case 200:
            return response
        case 401:
            raise EntegyFailedRequestError("Profile Doesn't Exist")
        case 406:
            raise EntegyFailedRequestError("Invalid Device Id")
        case 407:
            raise EntegyFailedRequestError("Profile is Banned")
        case 408:
            raise EntegyFailedRequestError("Profile is not Active")
        case _:
            raise EntegyFailedRequestError(
                f"{response['response']}: {response.get('message', 'Unknown error')}"
            )
