import json

from typing import Any


def send_notification(
    self,
    title: str,
    message: str,
    *,
    profile_id: str = None,
    external_reference: str = None,
    badge_reference: str = None,
    internal_reference: str = None,
    target_page: dict[str, str | int] = None
) -> dict[str, Any]:
    """
    Send a direct notification to all the devices registered to a list of
    profiles. This does not record a view or display in the core. An array of
    profile references must be specified.

    By default the popup only shows a close button, however an optional page can
    be specified in the input which will add a View button to the dialog, which
    will take you to the page. As per all content references, the `templateType`
    is required and you can provide either the `externalReference` or
    `moduleId`.

    Parameters
    ----------
        `title` (`str`): the title of the notification
        `message` (`str`): the message of the notification
        `profile_id` (`str`): the profile ID of the profile to send the notification to
        `external_reference` (`str`, optional): the external reference of the profile to send the ; defaults to `None`notification to
        `badge_reference` (`str`, optional): the badge reference of the profile to send the notification to; defaults to `None`
        `internal_reference` (`str`, optional): the internal reference of the profile to send the ; defaults to `None`notification to
        `target_page` (`dict[str, str | int]`, optional): the page to view when the notification is clicked; defaults to `None`


    The format of `target_page` is as follows:
    ```python
        {
            "templateType": "Exhibitors",
            "moduleId": 1
        }
    ```
    NOTE: can use either `moduleId` or `externalReference`

    Raises
    ------
        `Exception`: if no profile reference is specified

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "title": title,
        "message": message,
        "alertMessage": "This is an alert message"
    }

    if profile_id is not None:
        data.update({"profileReferences": [{"profileId": profile_id}]})
    elif external_reference is not None:
        data.update({"profileReferences": [{"profileId": external_reference}]})
    elif badge_reference is not None:
        data.update({"profileReferences": [{"profileId": badge_reference}]})
    elif internal_reference is not None:
        data.update({"profileReferences": [{"profileId": internal_reference}]})
    else:
        raise Exception("No profile reference specified")

    if target_page is not None:
        data.update({"targetPage": target_page})

    return self.post(
        self.api_endpoint + "/v2/Notification/SendBulk",
        headers=self.headers,
        data=json.dumps(data)
    )


def send_bulk_notification(
    self,
    title: str,
    message: str,
    profile_references: list[dict[str, str]],
    *,
    target_page: dict[str, str | int] = None
) -> dict[str, Any]:
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
            "moduleId": 1
        }
    ```
    NOTE: can use either `moduleId` or `externalReference`

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "profileReferences": profile_references,
        "title": title,
        "message": message,
        "alertMessage": "This is an alert message"
    }

    if target_page is not None:
        data.update({"targetPage": target_page})

    return self.post(
        self.api_endpoint + "/v2/Notification/SendBulk",
        headers=self.headers,
        data=json.dumps(data)
    )
