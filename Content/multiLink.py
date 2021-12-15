import requests, json

from Content.content import updateContent

def getMultiLinks(self, templateType, moduleId):
    """
    Returns all the multi links associated with the content page

    Arguments:
        templateType -- The template type of the page you want

        moduleId -- The moduleId of the page you want

    Returns:
        The multi links the content page has
    """
    data = {
        "projectId":self.projectID,
        "apiKey": self.apiKey,
        "templateType": templateType,
        "moduleId": moduleId
    }

    resp = requests.post(self.APIEndpoint+"/v2/MultiLink", headers=self.headers, data=json.dumps(data))
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output

def addMultiLinks(self, templateType, moduleId, multiLinks):
    """
    Add multi links to a content page.

    Arguments:
        templateType -- The template type of the page you want to add links to

        moduleId -- The moduleId of the page you want to add links to

        multiLinks -- The links you want to add

        e.g.

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

    Returns:
        Base response object
    """
    data = {
        "projectId":self.projectID,
        "apiKey": self.apiKey,
        "templateType": templateType,
        "moduleId": moduleId,
        "multiLinks": multiLinks
    }

    resp = requests.post(self.APIEndpoint+"/v2/MultiLink/Add", headers=self.headers, data=json.dumps(data))
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output

def removeMultiLink(self, templateType, moduleId, targetTemplateType, targetModuleId):
    """
    Removes a single multi link from a page

    Arguments:
        templateType -- The template type of the page you want to remove links from

        moduleId -- The moduleId of the page you want to remove links from

        targetTemplateType -- The moduleId of the multi link you want to remove

        targetModuleId -- The template type of the multi link you want to remove

        e.g.

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

    Returns:
        Base response object
    """
    data = {
        "projectId":self.projectID,
        "apiKey": self.apiKey,
        "templateType": templateType,
        "moduleId": moduleId,
        "targetTemplateType": targetTemplateType,
        "targetModuleId": targetModuleId
    }

    resp = requests.post(self.APIEndpoint+"/v2/MultiLink/Remove", headers=self.headers, data=json.dumps(data))
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output

def removeAllMultiLinks(self, templateType, moduleId, linkTemplateType = None):
    """
    Removes all the multi links from a page

    Arguments:
        templateType -- The template type of the page you want to remove links from

        moduleId -- The moduleId of the page you want to remove links from

        linkTemplateType -- The template type of the multi links you want to remove

    Returns:
        Base response object
    """
    data = {
        "projectId":self.projectID,
        "apiKey": self.apiKey,
        "templateType": templateType,
        "moduleId": moduleId
    }

    if(linkTemplateType != None):
        updateData = {"linkTemplateType": linkTemplateType}
        data.update(updateData)

    resp = requests.post(self.APIEndpoint+"/v2/MultiLink/RemoveAll", headers=self.headers, data=json.dumps(data))
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output