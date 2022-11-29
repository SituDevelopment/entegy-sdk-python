from typing import Any


def external_authentication(
    self,
    profile_id: str,
    device_id: str,
    *,
    request_version: int = 1
) -> dict[str, Any]:
    """
    Authenticate a user's login via an external system.

    Parameters
    ----------
        `profile_id` (`str`): the profile ID that is logging in
        `device_id` (`int`): the device ID that is logging in
        `request_version` (`int`, optional): the version of the request; defaults to `1`

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "profileId": profile_id,
        "deviceId": device_id,
        "requestVersion": request_version,
    }

    return self.post(
        self.api_endpoint + "/v2/Authentication/ExternalProfile",
        headers=self.headers,
        data=data
    )
