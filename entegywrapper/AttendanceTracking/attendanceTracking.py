from entegywrapper.schemas.attendanceTracking import Attendee, Attended


def add_check_in(
    self,
    *,
    profile_id: str | None = None,
    profile_external_reference: str | None = None,
    profile_internal_reference: str | None = None,
    profile_badge_reference: str | None = None,
    session_module_id: str | None = None,
    session_external_reference: str | None = None,
):
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

    self.post(self.api_endpoint + "/Track/AddCheckIn", data=data)


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

    return response["sessions"]
