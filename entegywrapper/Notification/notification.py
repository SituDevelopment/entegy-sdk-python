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
    Sends a notification to the specified profile. Only one of the profile
    references: profileId, externalReference, badgeReference, internalReference;
    will be used. if none are specified, an `Exception` is raised; otherwise,
    the first (in the previous list) specified is used.

    Arguments:
        title -- The title of the notification

        message -- The message of the notification

        profileId: -- The profile ID of the profile to send the notification to
        externalReference -- The external reference of the profile to send the notification to
        badgeReference -- The badge reference of the profile to send the notification to
        internalReference -- The internal reference of the profile to send the notification to

        targetPage -- The page to view when the notification is clicked

        e.g. NOTE: can use either `moduleId` or `externalReference`

        {
            "templateType": "Exhibitors",
            "moduleId": 1
        }

    Raises:
        `Exception` -- If no profile reference is specified

    Returns:
        The response from the API
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
        data=json.dumps(data)
    )
    if resp == None:
        raise Exception("No reponse received from API")
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

    Arguments:
        title -- The title of the notification

        message -- The message of the notification

        profileReferences -- The profile references to send the notification to

        e.g.

        [
            { "profileId": "1234567890" },
            { "externalReference": "1234567890" },
            { "badgeReference": "1234567890" },
            { "internalReference": "1234567890" }
        ]

        targetPage -- The page to view when the notification is clicked

        e.g. NOTE: can use either `moduleId` or `externalReference`

        {
            "templateType": "Exhibitors",
            "moduleId": 1
        }

    Returns:
        The response from the API
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
        data=json.dumps(data)
    )
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output
