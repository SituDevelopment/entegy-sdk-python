import json

from Content.content import updateContent

Link: type = dict[str, str | int]


def getMultiLinks(
    self,
    templateType: str,
    moduleId: int = None,
    externalReference: str = None
):
    """
    Returns all the multi links associated with the content page.

    Parameters
    ----------
        `templateType` (`str`): the template type of the page you want
        `moduleId` (`int`): the moduleId of the page you want
        `externalReference` (`str`): the externalReference of the page you want

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "templateType": templateType,
    }

    if moduleId != None:
        data.update({"moduleId": moduleId})
    if externalReference != None:
        data.update({"externalReference": externalReference})

    resp = self.post(
        self.APIEndpoint + "/v2/MultiLink", headers=self.headers, data=json.dumps(data)
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    if isinstance(resp, dict):
        return resp
    output = resp.json()
    return output


def addMultiLinks(
    self,
    templateType: str,
    multiLinks: list[Link],
    moduleId: int = None,
    externalReference: str = None
):
    """
    Add multi links to a content page.

    Parameters
    ----------
        `templateType` (`str`): the template type of the page you want to add links to
        `moduleId` (`int`): the moduleId of the page you want to add links to
        `multiLinks` (`list[Link]`): the links you want to add
        `externalReference` (`str`): the externalReference of the page you want

    The format of `multiLinks` is as follows:
    ```python
        [
            {
                "templateType":"Speaker",
                "moduleId":1
            },
            {
                "templateType":"Speaker",
                "externalReference":"au-speaker-1546895"
            }
        ]
    ```

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "templateType": templateType,
        "multiLinks": multiLinks,
    }

    if moduleId != None:
        data.update({"moduleId": moduleId})
    if externalReference != None:
        data.update({"externalReference": externalReference})

    resp = self.post(
        self.APIEndpoint + "/v2/MultiLink/Add",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    if isinstance(resp, dict):
        return resp
    output = resp.json()
    return output


def removeMultiLink(
    self,
    templateType: str,
    targetTemplateType: str,
    moduleId: int = None,
    externalReference: str = None,
    targetModuleId: int = None,
    targetExternalReference: str = None,
):
    """
    Removes a single multi link from a page.

    Parameters
    ----------
        `templateType` (`str`): the template type of the page you want to remove links from
        `targetTemplateType` (`str`): the template type of the multi link you want to remove
        `moduleId` (`int`): the moduleId of the page you want to remove links from
        `externalReference` (`str`): the externalReference of the page you want to remove links from
        `targetModuleId` (`int`): the moduleId of the multi link you want to remove
        `targetExternalReference` (`str`): the externalReference of the multi link you want to remove

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "templateType": templateType,
        "targetTemplateType": targetTemplateType,
    }

    if moduleId != None:
        data.update({"moduleId": moduleId})
    if externalReference != None:
        data.update({"externalReference": externalReference})
    if targetExternalReference != None:
        data.update({"targetExternalReference": targetExternalReference})
    if targetModuleId != None:
        data.update({"targetModuleId": targetModuleId})

    resp = self.post(
        self.APIEndpoint + "/v2/MultiLink/Remove",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    if isinstance(resp, dict):
        return resp
    output = resp.json()
    return output


def removeAllMultiLinks(
    self,
    templateType: str,
    moduleId: int = None,
    externalReference: str = None,
    linkTemplateType: str = None
):
    """
    Removes all the multi links from a page.

    Parameters
    ----------
        `templateType` (`str`): the template type of the page you want
        `moduleId` (`int`): the moduleId of the page you want
        `externalReference` (`str`): the externalReference of the page you want
        `linkTemplateType` (`str`): the template type of the page you want

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "templateType": templateType,
    }

    if moduleId != None:
        data.update({"moduleId": moduleId})
    if externalReference != None:
        data.update({"externalReference": externalReference})

    if linkTemplateType != None:
        updateData = {"linkTemplateType": linkTemplateType}
        data.update(updateData)

    resp = self.post(
        self.APIEndpoint + "/v2/MultiLink/RemoveAll",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    if isinstance(resp, dict):
        return resp
    output = resp.json()
    return output
