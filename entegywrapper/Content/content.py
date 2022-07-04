import requests, json

def getContent(self, moduleId="",extRef=None, templateType=None, includeCategories = False, includeDocuments = False, includeLinks = False, includeMultiLinks = False, includePageSettings = False):
    """
    Return all user profiles

    Arguments:
        templateType -- The type of the template you want content from

        moduleId -- The moduleId of the page you want content from

    Returns:
        The content response differs depending on what type of content you request.
    """
    data = {
        "projectId":self.projectID,
        "apiKey": self.apiKey,
        "templateType": templateType,
        "includeCategories": includeCategories,
        "includeDocuments": includeDocuments, 
        "includeLinks": includeLinks,
        "includeMultiLinks": includeMultiLinks,
        "includePageSettings": includePageSettings
    }
    if moduleId != None:
        data.update({"moduleId": moduleId})
    if extRef != None:
        data.update({"externalReference": extRef})
    resp = requests.post(self.APIEndpoint+"/v2/Content", headers=self.headers, data=json.dumps(data))
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output

def getScheduleContent(self, moduleId=None, extRef = None, includeCategories = False, includeDocuments = False, includeLinks = False, includeMultiLinks = False, includePageSettings = False):
    """
    Returns an entire schedule.

    Arguments:
        moduleId -- Any parameters to filter the returned profile by

    Returns:
        Content Schedule object
    """
    data = {
        "projectId":self.projectID,
        "apiKey": self.apiKey,
        "includeCategories": includeCategories,
        "includeDocuments": includeDocuments, 
        "includeLinks": includeLinks,
        "includeMultiLinks": includeMultiLinks,
        "includePageSettings": includePageSettings
    }

    if moduleId != None:
        data.update({"moduleId": moduleId})
    if extRef != None:
        data.update({"externalReference": extRef})
    resp = requests.post(self.APIEndpoint+"/v2/Content/Schedule", headers=self.headers, data=json.dumps(data))
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output

def createContent(self, content, contentGroup = "Default"):
    """
    Creates a root content item. You can only create Template Types that are listed as root content.

    Arguments:
        content -- The content you are creating, supports templateType, name, mainImage and externalReference

        e.g.

        {
            "templateType":"Schedule",
            "name":"Conference Program",
            "externalReference":""
        }

        moduleId -- The content group in the core this new root content should go in, leave blank for default

    Returns:
        The moduleId of the page you just created
    """
    data = {
        "projectId":self.projectID,
        "apiKey": self.apiKey,
        "contentGroup": contentGroup,
        "content": content
    }

    resp = requests.post(self.APIEndpoint+"/v2/Content/Create", headers=self.headers, data=json.dumps(data))
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output

def addChildrenContent(self, templateType, childTemplateType, children, moduleId = None, extRef = None):
    """
    Adds children to templateType

    Arguments:
        templateType -- The template type the children are being added to

        moduleId -- The name for the page

        childTemplateType -- The templateType for the children you're creating

        children -- The page data you want to add to the root templateType

        e.g.

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

    Returns:
        Base response object
    """
    data = {
        "projectId":self.projectID,
        "apiKey": self.apiKey,
        "templateType": templateType,
        "childTemplateType": childTemplateType,
        "children": children
    }
    if moduleId != None:
        data.update({"moduleId": moduleId})
    if extRef != None:
        data.update({"externalReference": extRef})
        
    resp = requests.post(self.APIEndpoint+"/v2/Content/AddChildren", headers=self.headers, data=json.dumps(data))
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output

def updateContent(self, templateType,content, moduleId = None, extRef = None):
    """
    Updates data within a content item

    Arguments:
        templateType -- The templateType you're updating

        moduleId -- The moduleId of the page you're updating

        content -- The content you're updating, supports the name, sort order, mainImage, strings and links

        e.g.

        {
            "name":"Mr John Smith",
            "sortOrder":1
            "strings":
                {
                    "copy":"Mr John Smith is an expert on many fields. He holds many prestigious awards from many prestigious parties",
                    "companyAndPosition":"XYZ Widgets || Director"
                }
        }

    Returns:
        Base response object
    """
    data = {
        "projectId":self.projectID,
        "apiKey": self.apiKey,
        "templateType": templateType,
        "content": content
    }
    if moduleId != None:
        data.update({"moduleId": moduleId})
    if extRef != None:
        data.update({"externalReference": extRef})

    resp = requests.post(self.APIEndpoint+"/v2/Content/Update", headers=self.headers, data=json.dumps(data))
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output

def deleteContent(self, templateType, moduleId= None, extRef = None):
    """
    Allows you to delete a content resource from the Entegy System. Any content deleted is unrecoverable.

    -= WARNING =- Deleting root content will result in all child pages being deleted!

    Arguments:
        templateType -- The templateType of the resource you're deleting

        moduleId -- The moduleId of the page you're deleting

    Returns:
        Base response object
    """
    data = {
        "projectId":self.projectID,
        "apiKey": self.apiKey,
        "templateType": templateType
    }
    if moduleId != None:
        data.update({"moduleId": moduleId})
    if extRef != None:
        data.update({"externalReference": extRef})

    resp = requests.delete(self.APIEndpoint+"/v2/Content/Delete", headers=self.headers, data=json.dumps(data))
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output