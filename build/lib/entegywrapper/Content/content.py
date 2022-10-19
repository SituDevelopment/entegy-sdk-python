import json
import requests


def getContent(
    self,
    templateType: str,
    moduleId: int = None,
    externalReference: str = None,
    includeCategories: bool = False,
    includeDocuments: bool = False,
    includeLinks: bool = False,
    includeMultiLinks: bool = False,
    includePageSettings: bool = False,
):
    """
    Returns an entire schedule.

    You can expand the response returned by optionally asking for categories,
    documents, links and multilinks. You should only request these if you need
    them as they will slow down the request.

    Parameters
    ----------
        `templateType` (`str`): the type of the template you want content from
        `moduleId` (`int`): the instance of the data you're after
        `externalReference` (`str`): the external reference for the content you want
        `includeCategories` (`bool`): whether you want Categories in the response; defaults to False
        `includeDocuments` (`bool`): whether you want Documents in the response; defaults to False
        `includeLinks` (`bool`): whether you want Links in the response; defaults to False
        `includeMultiLinks` (`bool`): whether you want MultiLinks in the response; defaults to False
        `includePageSettings` (`bool`): whether you want PageSettings in the response; defaults to False

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "templateType": templateType,
        "includeCategories": includeCategories,
        "includeDocuments": includeDocuments,
        "includeLinks": includeLinks,
        "includeMultiLinks": includeMultiLinks,
        "includePageSettings": includePageSettings,
    }

    if moduleId != None:
        data.update({"moduleId": moduleId})
    if externalReference != None:
        data.update({"externalReference": externalReference})

    resp = self.post(
        self.APIEndpoint + "/v2/Content", headers=self.headers, data=json.dumps(data)
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output


def getScheduleContent(
    self,
    moduleId: int = None,
    externalReference: str = None,
    includeCategories: bool = False,
    includeDocuments: bool = False,
    includeLinks: bool = False,
    includeMultiLinks: bool = False,
    includePageSettings: bool = False,
):
    """
    Returns an entire schedule.

    You can expand the response returned by optionally asking for categories,
    documents, links and multilinks. You should only request these if you need
    them as they will slow down the request.

    Parameters
    ----------
        `moduleId` (`int`): the instance of the data you're after
        `externalReference` (`str`): the external reference for the content you want
        `includeCategories` (`bool`): whether you want Categories in the response; defaults to False
        `includeDocuments` (`bool`): whether you want Documents in the response; defaults to False
        `includeLinks` (`bool`): whether you want Links in the response; defaults to False
        `includeMultiLinks` (`bool`): whether you want MultiLinks in the response; defaults to False
        `includePageSettings` (`bool`): whether you want PageSettings in the response; defaults to False

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "includeCategories": includeCategories,
        "includeDocuments": includeDocuments,
        "includeLinks": includeLinks,
        "includeMultiLinks": includeMultiLinks,
        "includePageSettings": includePageSettings,
        "moduleId": moduleId,
    }

    if externalReference != None:
        data.update({"externalReference": externalReference})

    resp = self.post(
        self.APIEndpoint + "/v2/Content/Schedule",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output


def createContent(
    self,
    content: dict,
    contentGroup: str = "Default"
):
    """
    Creates a root content item. You can only create Template Types that are
    listed as root content.

    Parameters
    ----------
        `content` (`dict`): the content you are creating, supports templateType, name, mainImage and externalReference
        `contentGroup` (`str`) the content group in the core this new root content should go in; defaults to "Default"

    The format of `content` is as follows:
    ```python
        {
            "templateType":"Schedule",
            "name":"Conference Program",
            "externalReference":""
        }
    ```

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "contentGroup": contentGroup,
        "content": content,
    }

    resp = self.post(
        self.APIEndpoint + "/v2/Content/Create",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output


def addChildrenContent(
    self,
    templateType: str,
    childTemplateType: str,
    children: list,
    moduleId: int = None,
    externalReference: str = None,
):
    """
    Adds children to templateType.

    Parameters
    ----------
        `templateType` (`string`): the template type the children are being added to
        `moduleId` (`int`): the name for the page
        `externalReference` (`str`): the externalReference for the page
        `childTemplateType` (`string`): the templateType for the children you're creating
        `children` (`list`): the page data you want to add to the root templateType

    The format of `children` is as follows:
    ```python
        [
            {
                "externalReference":"au-speaker-545415842",
                "name":"John Smith",
                "strings":
                    {
                        "copy":"John Smith is an expert on many fields. He holds many prestigious awards from many prestigious parties",
                        "companyAndPosition":"XYZ Widgets // Director"
                    },
                "category":3,
                "sortOrder" : 4
            },
            {
                "externalReference":"au-speaker-874561246",
                "name":"John Doe",
                "strings":
                    {
                        "copy":"John Doe is an expert on many fields. He holds many prestigious awards from many prestigious parties",
                        "companyAndPosition":"ACME Corp // Director",
                        "phoneNumber":"1300 123 456",
                        "emailAddress":"john.doe@acme.corp",
                        "website":"https://acme.corp",
                        "address":"123 Acme Street
                                Corporation Town 1234
                                Australia"
                    },
                "category":2,
                "sortOrder" : 5
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
        "childTemplateType": childTemplateType,
        "children": children,
    }

    if moduleId != None:
        data.update({"moduleId": moduleId})
    if externalReference != None:
        data.update({"externalReference": externalReference})

    resp = self.post(
        self.APIEndpoint + "/v2/Content/AddChildren",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output


def updateContent(
    self,
    templateType: str,
    content: list,
    moduleId: int = None,
    externalReference: str = None
):
    """
    Updates data within a content item.

    Parameters
    ----------
        `templateType` (`str`): the templateType you're updating
        `moduleId` (`int`): the moduleId of the page you're updating
        `content` (`list`): the content you're updating, supports the name, sort order, mainImage, strings and links

    The format of `content` is as follows:
    ```python
        {
            "name":"Mr John Smith",
            "sortOrder":1
            "strings":
                {
                    "copy":"Mr John Smith is an expert on many fields. He holds many prestigious awards from many prestigious parties",
                    "companyAndPosition":"XYZ Widgets || Director"
                }
        }
    ```

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "templateType": templateType,
        "content": content,
    }

    if moduleId != None:
        data.update({"moduleId": moduleId})
    if externalReference != None:
        data.update({"externalReference": externalReference})

    resp = self.post(
        self.APIEndpoint + "/v2/Content/Update",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output


def deleteContent(
    self,
    templateType: str,
    moduleId: int = None,
    externalReference: str = None
):
    """
    Allows you to delete a content resource from the Entegy System. Any content
    deleted is unrecoverable.

    WARNING
    -------
        Deleting root content will result in all child pages being deleted.

    Parameters
    ----------
        `templateType` (`str`): the templateType of the resource you're deleting
        `moduleId` (`int`): the moduleId of the page you're deleting
        `externalReference` (`str`): the externalReference of the page you're deleting

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

    resp = requests.delete(
        self.APIEndpoint + "/v2/Content/Delete",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output
