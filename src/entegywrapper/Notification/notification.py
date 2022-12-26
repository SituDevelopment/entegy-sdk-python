from entegywrapper.schemas.profile import ProfileIdentifier


def send_notification(
    self,
    title: str,
    message: str,
    *,
    profile_id: str | None = None,
    external_reference: str | None = None,
    internal_reference: str | None = None,
    badge_reference: str | None = None,
    target_page: dict[str, str | int] | None = None
) -> str:
    """
    Sends a notification to the specified profile.

    Parameters
    ----------
        `title` (`str`): the title of the notification
        `message` (`str`): the message of the notification
        `profile_id` (`str`): the profileId of the profile to send the notification to
        `external_reference` (`str`, optional): the externalReference of the profile to send the ; defaults to `None`notification to
        `internal_reference` (`str`, optional): the internalReference of the profile to send the ; defaults to `None`notification to
        `badge_reference` (`str`, optional): the badgeReference of the profile to send the notification to; defaults to `None`
        `target_page` (`dict[str, str | int]`, optional): the page to view when the notification is clicked; defaults to `None`

    The format of `target_page` is as follows:
    ```python
        {
            "templateType": "Exhibitors",
            "moduleId": 1  # could be externalReference instead
        }
    ```

    Raises
    ------
        `ValueError`: if no identifier is specified

    Returns
    -------
        `str`: API response message
    """
    data = {
        "title": title,
        "message": message,
        "alertMessage": "This is an alert message",
    }

    if profile_id is not None:
        data["profileReferences"] = {"profileId": profile_id}
    elif external_reference is not None:
        data["profileReferences"] = {"externalReference": external_reference}
    elif internal_reference is not None:
        data["profileReferences"] = {"internalReference": internal_reference}
    elif badge_reference is not None:
        data["profileReferences"] = {"badgeReference": badge_reference}
    else:
        raise ValueError("Please specify an identifier")

    if target_page is not None:
        data["viewTargetPage"] = target_page

    response = self.post(self.api_endpoint + "/v2/Notification/SendBulk", data=data)

    return response["message"]


def send_bulk_notification(
    self,
    title: str,
    message: str,
    profile_references: list[dict[ProfileIdentifier, str]],
    *,
    target_page: dict[str, str | int] | None = None
) -> str:
    """
    Sends a notification to the specified profiles.

    Parameters
    ----------
        `title` (`str`): the title of the notification
        `message` (`str`): the message of the notification
        `profile_references` (`list[dict[str, str]]`): the profile references to send the notification to
        `target_page` (`dict[str, str | int]`, optional): the page to view when the notification is clicked; defaults to `None`

    The format of `profile_references` is as follows:
    ```python
        [
            { "profileId": "1234567890" },
            { "externalReference": "1234567890" },
            { "badgeReference": "1234567890" },
            { "internalReference": "1234567890" }
        ]
    ```

    The format of `target_page` is as follows:
    ```python
        {
            "templateType": "Exhibitors",
            "moduleId": 1  # could be externalReference instead
        }
    ```

    Returns
    -------
        `str`: API response message
    """
    data = {
        "profileReferences": profile_references,
        "title": title,
        "message": message,
        "alertMessage": "This is an alert message -- it is not shown anywhere"
        " or documented in the API docs, but it is required.",
    }

    if target_page is not None:
        data["viewTargetPage"] = target_page

    response = self.post(self.api_endpoint + "/v2/Notification/SendBulk", data=data)

    return response["message"]
