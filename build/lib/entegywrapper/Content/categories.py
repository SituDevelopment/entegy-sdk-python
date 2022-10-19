import json
import requests

from entegywrapper.EntegyAPI import Identifier

Category: type = dict[Identifier, str | int]


def availableCategories(
    self,
    templateType: str, 
    moduleId: int = None,
    externalReference: str = None,
):
    """
    This returns a list of the available categories for the page in question.

    Parameters
    ----------
        `templateType` (`str`): the template type of the page you want
        `moduleId`     (`int`): the moduleId of the page you want
        `externalReference` (`str`): the externalReference of the page you want

    Returns
    -------
        `list[Category]`: the available categories
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "templateType": templateType
    }

    if moduleId != None:
        data.update({"moduleId": moduleId})
    if externalReference != None:
        data.update({"externalReference": externalReference})

    resp = self.post(
        self.APIEndpoint + "/v2/Categories/Available",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output


def selectCategories(
    self,
    templateType: str,
    categories: list[Category],
    moduleId: int = None,
    externalReference: str = None
):
    """
    You can select a category with either an `externalReference`, `moduleId` or
    `name`.

    If you have duplicate names, one of the them will be selected. If this
    is a problem either use externalReference or moduleId or have unique names.
    You cannot select a category that has child categories. This method will
    succeed provided at least one of the categories supplied is valid.

    Parameters
    ----------
        `templateType` (`str`): the template type of the page selecting the categories
        `categories` (`list[Category]`): the categories you want to select
        `moduleId` (`int`): the moduleId of the page selecting the categories
        `externalReference` (`str`): the externalReference of the page selecting the categories

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "templateType": templateType,
        "categories": categories,
    }

    if moduleId != None:
        data.update({"moduleId": moduleId})
    if externalReference != None:
        data.update({"externalReference": externalReference})

    resp = self.post(
        self.APIEndpoint + "/v2/Categories/Select",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output


def deselectCategories(
    self,
    templateType: str,
    categories: list[Category],
    moduleId: int = None,
    externalReference: str = None
):
    """
    You can unselect a category with either an `externalReference` or `moduleId`.

    Parameters
    ----------
        `templateType` (`str`): the template type of the page you're unselecting the categories from
        `categories` (`list[Category]`): the categories you want to select
        `moduleId` (`int`): the moduleId of the page you're unselecting the categories from
        `externalReference` (`str`): the externalReference of the page you're unselecting the categories from

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "templateType": templateType,
        "categories": categories,
    }

    if moduleId != None:
        data.update({"moduleId": moduleId})
    if externalReference != None:
        data.update({"externalReference": externalReference})

    resp = self.post(
        self.APIEndpoint + "/v2/Categories/Deselect",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output


def createCategories(
    self,
    templateType: str,
    categories: list[Category],
    moduleId: int = None,
    externalReference: str = None
):
    """
    Allows you to create categories under a root page.

    You cannot create child / sub categories with this endpoint. You will need
    to use the create child categories endpoint. It is highly recommended you
    use unique names for each category list. Using unique names allows you to
    select categories with just the name.

    Parameters
    ----------
        `templateType` (`str`): the template type of the page holding the categories
        `categories` (`list[Category]`): the categories you want to create
        `moduleId` (`int`): the moduleId of the page holding the categories
        `externalReference` (`str`): the externalReference of the page holding the categories

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "templateType": templateType,
        "categories": categories,
    }

    if moduleId != None:
        data.update({"moduleId": moduleId})
    if externalReference != None:
        data.update({"externalReference": externalReference})

    resp = self.post(
        self.APIEndpoint + "/v2/Categories/Create",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output


def createChildCategories(
    self,
    categories: list[Category],
    moduleId: int = None,
    externalReference: str = None
):
    """
    Allows you to create categories under another category.

    Adding categories under a category prevents the parent category from being
    selected by a page. It is highly recommended you use unique names for each
    category list. Using unique names allows you to reliably select categories
    with just the name.

    Parameters
    ----------
        `categories` (`list[Category]`): the categories you want to create
        `moduleId` (`int`): the moduleId of the page holding the categories
        `externalReference` (`int`): the externalReference of the page holding the categories

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "categories": categories,
    }

    if moduleId != None:
        data.update({"moduleId": moduleId})
    if externalReference != None:
        data.update({"externalReference": externalReference})

    resp = self.post(
        self.APIEndpoint + "/v2/Categories/CreateChild",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output


def updateCategories(
    self,
    name: str,
    moduleId: int = None,
    externalReference: str = None
):
    """
    Allows you to change the name of a category.

    Parameters
    ----------
        `name` (`str`): the new name of the category
        `moduleId` (`int`): the moduleId of the category
        `externalReference` (`str`): the externalReference of the category

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "name": name
    }

    if moduleId != None:
        data.update({"moduleId": moduleId})
    if externalReference != None:
        data.update({"externalReference": externalReference})

    resp = self.post(
        self.APIEndpoint + "/v2/Categories/Update",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output


def deleteCategories(
    self,
    templateType: str,
    categories: list[Category],
    moduleId: int = None,
    externalReference: str = None
):
    """
    Allows you to create categories under another category.

    Parameters
    ----------
        `templateType` (`str`): the template type of the page you want
        `categories` (`list[Category]`): the categories you want to delete
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
        "categories": categories,
    }

    if moduleId != None:
        data.update({"moduleId": moduleId})
    if externalReference != None:
        data.update({"externalReference": externalReference})

    resp = requests.delete(
        self.APIEndpoint + "/v2/Categories/Delete",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output
