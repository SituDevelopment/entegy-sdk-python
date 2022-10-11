import requests
import json


def sendNotification(
    self,
    title: str,
    message: str,
    profileId: str = None,
    externalReference: str = None,
    badgeReference: str = None,
    internalReference: str = None,
    targetPage: dict[str, str | int] = None
):
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
        `profileId` (`str`): the profile ID of the profile to send the notification to
        `externalReference` (`str`): the external reference of the profile to send the notification to
        `badgeReference` (`str`): the badge reference of the profile to send the notification to
        `internalReference` (`str`): the internal reference of the profile to send the notification to
        `targetPage` (`dict[str, str | int]`): the page to view when the notification is clicked


    The format of `targetPage` is as follows:
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
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "title": title,
        "message": message,
        "alertMessage": "This is an alert message"
    }

    if profileId != None:
        data.update({"profileReferences": [{"profileId": profileId}]})
    elif externalReference != None:
        data.update({"profileReferences": [{"profileId": externalReference}]})
    elif badgeReference != None:
        data.update({"profileReferences": [{"profileId": badgeReference}]})
    elif internalReference != None:
        data.update({"profileReferences": [{"profileId": internalReference}]})
    else:
        raise Exception("No profile reference specified")

    if targetPage != None:
        data.update({"targetPage": targetPage})

    resp = self.post(
        self.APIEndpoint + "/v2/Notification/SendBulk",
        headers=self.headers,
        data=json.dumps(data)
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output


def sendBulkNotification(
    self,
    title: str,
    message: str,
    profileReferences: list[dict[str, str]],
    targetPage: dict[str, str | int] = None
):
    """
    Sends a notification to the specified profiles.

    Parameters
    ----------
        `title` (`str`): the title of the notification
        `message` (`str`): the message of the notification
        `profileReferences` (`list[dict[str, str]]`): the profile references to send the notification to
        `targetPage` (`dict[str, str | int]`): the page to view when the notification is clicked

    The format of `` is as follows:
    ```python
        [
            { "profileId": "1234567890" },
            { "externalReference": "1234567890" },
            { "badgeReference": "1234567890" },
            { "internalReference": "1234567890" }
        ]
    ```

    The format of `` is as follows:
    ```python
        {
            "templateType": "Exhibitors",
            "moduleId": 1
        }
    ```
    NOTE: can use either `moduleId` or `externalReference`

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "profileReferences": profileReferences,
        "title": title,
        "message": message,
        "alertMessage": "This is an alert message"
    }

    if targetPage != None:
        data.update({"targetPage": targetPage})

    resp = self.post(
        self.APIEndpoint + "/v2/Notification/SendBulk",
        headers=self.headers,
        data=json.dumps(data)
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output
