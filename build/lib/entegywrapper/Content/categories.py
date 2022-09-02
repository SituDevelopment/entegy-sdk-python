import requests, json


def availableCategories(self, templateType, moduleId):
    """
    This returns a list of the available categories for the page in question.

    Arguments:
        templateType -- The template type of the page you want

        moduleId -- 	The moduleId of the page you want

    Returns:
        List of available categories
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "templateType": templateType,
        "moduleId": moduleId,
    }

    resp = self.post(
        self.APIEndpoint + "/v2/Categories/Available",
        headers=self.headers,
        data=json.dumps(data),
    )
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output


def selectCategories(self, templateType, moduleId, categories):
    """
    Allows you to select multiple categories of a template type

    Arguments:
        templateType -- The template type of the page you want

        moduleId -- 	The moduleId of the page you want

        categories -- The categories you want to select

        e.g.

        [
            {
                "name":"Keynote",
            },
            {
                "externalReference":"plenary"
            },
            {
                "moduleId":5,
            },
            {
                "name":"Panel",
            },
            {
                "externalReference":"chair"
            },
            {
                "moduleId":6
            }
        ]

    Returns:
        Base response object
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "templateType": templateType,
        "moduleId": moduleId,
        "categories": categories,
    }

    resp = self.post(
        self.APIEndpoint + "/v2/Categories/Select",
        headers=self.headers,
        data=json.dumps(data),
    )
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output


def deselectCategories(self, templateType, moduleId, categories):
    """
    You can unselect a category with either an externalReference or moduleId.

    Arguments:
        templateType -- The template type of the page you want

        moduleId -- 	The moduleId of the page you want

        categories -- The categories you want to select

        e.g.

        [
            {
                "name":"Keynote",
            },
            {
                "externalReference":"plenary"
            },
            {
                "moduleId":5,
            },
            {
                "name":"Panel",
            },
            {
                "externalReference":"chair"
            },
            {
                "moduleId":6
            }
        ]

    Returns:
        Base response object
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "templateType": templateType,
        "moduleId": moduleId,
        "categories": categories,
    }

    resp = self.post(
        self.APIEndpoint + "/v2/Categories/Deselect",
        headers=self.headers,
        data=json.dumps(data),
    )
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output


def createCategories(self, templateType, moduleId, categories):
    """
    Allows you to create categories under a root page.

    Arguments:
        templateType -- The template type of the page you want

        moduleId -- 	The moduleId of the page you want

        categories -- The categories you want to select

        e.g.

        [
            {
                "name":"Keynote",
                "externalReference":"keynote"
            },
            {
                "name":"Plenary",
                "externalReference":"plenary"
            },
            {
                "name":"Breakout",
                "externalReference":"breakout"
            },
            {
                "name":"Panel",
                "externalReference":"panel"
            },
            {
                "name":"Chair",
                "externalReference":"chair"
            },
            {
                "name":"Sponsored",
                "externalReference":"sponsored"
            }
        ]

    Returns:
        Base response object
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "templateType": templateType,
        "moduleId": moduleId,
        "categories": categories,
    }

    resp = self.post(
        self.APIEndpoint + "/v2/Categories/Create",
        headers=self.headers,
        data=json.dumps(data),
    )
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output


def createChildCategories(self, templateType, externalReference, categories):
    """
    Allows you to create categories under another category.

    Arguments:
        templateType -- The template type of the page you want

        externalReference -- The externalReference of the page you want

        categories -- The categories you want to select

        e.g.

        [
            {
                "name":"Stream 1",
                "externalReference":"stream1"
            },
            {
                "name":"Stream 2",
                "externalReference":"stream2"
            },
            {
                "name":"Stream 3",
                "externalReference":"stream3"
            }
        ]

    Returns:
        Base response object
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "templateType": templateType,
        "externalReference": externalReference,
        "categories": categories,
    }

    resp = self.post(
        self.APIEndpoint + "/v2/Categories/CreateChild",
        headers=self.headers,
        data=json.dumps(data),
    )
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output


def updateCategories(self, moduleId, name):
    """
    Allows you to change the name of a category.

    Arguments:
        moduleId -- The moduleId of the category

        name -- The new name of the category

    Returns:
        Base response object
    """
    data = {"projectId": self.projectID, "moduleId": moduleId, "name": name}

    resp = self.post(
        self.APIEndpoint + "/v2/Categories/Update",
        headers=self.headers,
        data=json.dumps(data),
    )
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output


def deleteCategories(self, templateType, moduleId, categories):
    """
    Allows you to create categories under another category.

    Arguments:
        templateType -- The template type of the page you want

        moduleId -- The moduleId of the page you want

        categories -- The categories you want to select

        e.g.

        [
            {
                "externalReference":"plenary"
            },
            {
                "moduleId":5,
            },
            {
                "externalReference":"chair"
            },
            {
                "moduleId":6
            }
        ]

    Returns:
        Base response object
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "templateType": templateType,
        "moduleId": moduleId,
        "categories": categories,
    }

    resp = requests.delete(
        self.APIEndpoint + "/v2/Categories/Delete",
        headers=self.headers,
        data=json.dumps(data),
    )
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output
