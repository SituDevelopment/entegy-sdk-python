from entegywrapper.errors import EntegyFailedRequestError
from entegywrapper.schemas.attendance_tracking import Attended, Attendee


def add_check_in(
    self,
    *,
    profile_id: str | None = None,
    profile_external_reference: str | None = None,
    profile_internal_reference: str | None = None,
    profile_badge_reference: str | None = None,
    session_module_id: str | None = None,
    session_external_reference: str | None = None,
) -> bool:
    """
    Checks the specified profile into the specified session.

    Parameters
    ----------
        `profile_id` (`str`, optional): the profileId of the profile; defaults to `None`

        `profile_external_reference` (`str`, optional): the externalReference of the profile; defaults to `None`

        `profile_badge_reference` (`str`, optional): the badgeReference of the profile; defaults to `None`

        `profile_internal_reference` (`str`, optional): the internalReference of the profile; defaults to `None`

        `session_module_id` (`str`, optional): the moduleId of the session; defaults to `None`

        `session_external_reference` (`str`, optional): the externalReference of the session; defaults to `None`

    Raises
    ------
        `ValueError`: if the profile or session identifier is not specified

        `EntegyFailedRequestError`: if the API request fails

    Returns
    -------
        `bool`: whether the check-in was successful
    """
    data = {}

    if profile_id is not None:
        data["profileReference"] = {"profileId": profile_id}
    elif profile_external_reference is not None:
        data["profileReference"] = {"externalReference": profile_external_reference}
    elif profile_badge_reference is not None:
        data["profileReference"] = {"badgeReference": profile_badge_reference}
    elif profile_internal_reference is not None:
        data["profileReference"] = {"internalReference": profile_internal_reference}
    else:
        raise ValueError("Please specify a profile identifier")

    if session_module_id is not None:
        data["contentReference"] = {"moduleId": session_module_id}
    elif session_external_reference is not None:
        data["contentReference"] = {"externalReference": session_external_reference}
    else:
        raise ValueError("Please specify a session identifier")

    response = self.post(self.api_endpoint + "/Track/AddCheckIn", data=data)

    match response["response"]:
        case 200:
            return True
        case 401:
            raise EntegyFailedRequestError("Missing content reference")
        case 402:
            raise EntegyFailedRequestError("Missing profile reference")
        case _:
            raise EntegyFailedRequestError(
                f"{response['response']}: {response.get('message', 'Unknown error')}"
            )


def get_attendees(
    self,
    *,
    module_id: str | None = None,
    external_reference: str | None = None,
) -> list[Attendee]:
    """
    Returns the attendees who attended the session specified by the given
    identifier.

    Parameters
    ----------
        `module_id` (`str`, optional): the moduleId of the session; defaults to `None`

        `external_reference` (`str`, optional): the externalReference of the session; defaults to `None`

    Raises
    ------
        `EntegyFailedRequestError`: if the API request fails

    Returns
    -------
        `list[Attendee]`: the attendees who attended the session
    """
    data = {}

    if module_id is not None:
        data["moduleId"] = module_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    else:
        raise ValueError("Please specify an identifier")

    response = self.post(self.api_endpoint + "/v2/Track/Attendees", data=data)

    if response["response"] == 401:
        raise EntegyFailedRequestError("Missing profile reference")

    return response["attendees"]


def get_attended(
    self,
    *,
    profile_id: str | None = None,
    external_reference: str | None = None,
    badge_reference: str | None = None,
    internal_reference: str | None = None,
) -> list[Attended]:
    """
    Returns the sessions attended by the profile specified by the given
    identifier.

    Parameters
    ----------
        `profile_id` (`str`, optional): the profileId of the profile; defaults to `None`

        `external_reference` (`str`, optional): the externalReference of the profile; defaults to `None`

        `badge_reference` (`str`, optional): the badgeReference of the profile; defaults to `None`

        `internal_reference` (`str`, optional): the internalReference of the profile; defaults to `None`

    Raises
    ------
        `EntegyFailedRequestError`: if the API request fails

    Returns
    -------
        `list[Attended`: the sessions attended by the specified user
    """
    data = {}

    if profile_id is not None:
        data["profileId"] = profile_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    elif badge_reference is not None:
        data["badgeReference"] = badge_reference
    elif internal_reference is not None:
        data["internalReference"] = internal_reference
    else:
        raise ValueError("Please specify an identifier")

    response = self.post(self.api_endpoint + "/v2/Track/Attended", data=data)

    if response["response"] == 401:
        raise EntegyFailedRequestError("Missing profile reference")

    return response["sessions"]
