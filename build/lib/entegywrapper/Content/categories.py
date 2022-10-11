import json
import requests

from entegywrapper.EntegyAPI import Identifier

Category: type = dict[Identifier, str | int]


def availableCategories(self, templateType: str, moduleId: int):
    """
    This returns a list of the available categories for the page in question.

    Parameters
    ----------
        `templateType` (`str`): the template type of the page you want
        `moduleId`     (`int`): the moduleId of the page you want

    Returns
    -------
        `list[Category]`: the available categories
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
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output


def selectCategories(self, templateType: str, moduleId: int, categories: list[Category]):
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
        `moduleId` (`int`): the moduleId of the page selecting the categories
        `categories` (`list[Category]`): the categories you want to select

    Returns
    -------
        `dict`: API response JSON
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
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output


def deselectCategories(self, templateType: str, moduleId: int, categories: list[Category]):
    """
    You can unselect a category with either an `externalReference` or `moduleId`.

    Parameters
    ----------
        `templateType` (`str`): the template type of the page you're unselecting the categories from
        `moduleId` (`int`): the moduleId of the page you're unselecting the categories from
        `categories` (`list[Category]`): the categories you want to select

    Returns
    -------
        `dict`: API response JSON
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
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output


def createCategories(self, templateType: str, moduleId: int, categories: list[Category]):
    """
    Allows you to create categories under a root page.

    You cannot create child / sub categories with this endpoint. You will need
    to use the create child categories endpoint. It is highly recommended you
    use unique names for each category list. Using unique names allows you to
    select categories with just the name.

    Parameters
    ----------
        `templateType` (`str`): the template type of the page holding the categories
        `moduleId` (`int`): the moduleId of the page holding the categories
        `categories` (`list[Category]`): the categories you want to create

    Returns
    -------
        `dict`: API response JSON
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
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output


def createChildCategories(self, externalReference: int, categories: list[Category]):
    """
    Allows you to create categories under another category.

    Adding categories under a category prevents the parent category from being
    selected by a page. It is highly recommended you use unique names for each
    category list. Using unique names allows you to reliably select categories
    with just the name.

    Parameters
    ----------
        `externalReference` (`int`): the externalReference of the page holding the categories
        `categories` (`list[Category]`): the categories you want to create

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "externalReference": externalReference,
        "categories": categories,
    }

    resp = self.post(
        self.APIEndpoint + "/v2/Categories/CreateChild",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output


def updateCategories(self, moduleId: int, name: str):
    """
    Allows you to change the name of a category.

    Parameters
    ----------
        `moduleId` (`int`): the moduleId of the category
        `name` (`str`): the new name of the category

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "moduleId": moduleId,
        "name": name
    }

    resp = self.post(
        self.APIEndpoint + "/v2/Categories/Update",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output


def deleteCategories(self, templateType: str, moduleId: int, categories: list[Category]):
    """
    Allows you to create categories under another category.

    Parameters
    ----------
        `templateType` (`str`): the template type of the page you want
        `moduleId` (`int`): the moduleId of the page you want
        `categories` (`list[Category]`): the categories you want to delete

    Returns
    -------
        `dict`: API response JSON
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
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output
