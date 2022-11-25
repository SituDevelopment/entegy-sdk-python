import json

from entegywrapper.EntegyAPI import Identifier
from typing import Any

Category: type = dict[Identifier, str | int]


def available_categories(
    self,
    template_type: str,
    *,
    module_id: int = None,
    external_reference: str = None,
) -> list[Category]:
    """
    This returns a list of the available categories for the page in question.

    Parameters
    ----------
        `template_type` (`str`): the template type of the page you want
        `module_id` (`int`, optional): the moduleId of the page you want; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the page you want; defaults to `None`

    Returns
    -------
        `list[Category]`: the available categories
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "templateType": template_type
    }

    if module_id is not None:
        data.update({"moduleId": module_id})
    if external_reference is not None:
        data.update({"externalReference": external_reference})

    return self.post(
        self.api_endpoint + "/v2/Categories/Available",
        headers=self.headers,
        data=json.dumps(data)
    )


def select_categories(
    self,
    template_type: str,
    categories: list[Category],
    *,
    module_id: int = None,
    external_reference: str = None
) -> dict[str, Any]:
    """
    You can select a category with either an `externalReference`, `moduleId` or
    `name`.

    If you have duplicate names, one of the them will be selected. If this
    is a problem either use externalReference or moduleId or have unique names.
    You cannot select a category that has child categories. This method will
    succeed provided at least one of the categories supplied is valid.

    Parameters
    ----------
        `template_type` (`str`): the template type of the page selecting the categories
        `categories` (`list[Category]`): the categories you want to select
        `module_id` (`int`, optional): the moduleId of the page selecting the categories; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the page selecting the categories; defaults to `None`

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "templateType": template_type,
        "categories": categories,
    }

    if module_id is not None:
        data.update({"moduleId": module_id})
    if external_reference is not None:
        data.update({"externalReference": external_reference})

    return self.post(
        self.api_endpoint + "/v2/Categories/Select",
        headers=self.headers,
        data=json.dumps(data)
    )


def deselect_categories(
    self,
    template_type: str,
    categories: list[Category],
    *,
    module_id: int = None,
    external_reference: str = None
) -> dict[str, Any]:
    """
    You can unselect a category with either an `externalReference` or `moduleId`.

    Parameters
    ----------
        `template_type` (`str`): the template type of the page you're unselecting the categories from
        `categories` (`list[Category]`): the categories you want to select
        `module_id` (`int`, optional): the moduleId of the page you're unselecting the categories from; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the page you're unselecting the categories from; defaults to `None`

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "templateType": template_type,
        "categories": categories,
    }

    if module_id is not None:
        data.update({"moduleId": module_id})
    if external_reference is not None:
        data.update({"externalReference": external_reference})

    return self.post(
        self.api_endpoint + "/v2/Categories/Deselect",
        headers=self.headers,
        data=json.dumps(data)
    )


def create_categories(
    self,
    template_type: str,
    categories: list[Category],
    *,
    module_id: int = None,
    external_reference: str = None
) -> dict[str, Any]:
    """
    Allows you to create categories under a root page.

    You cannot create child / sub categories with this endpoint. You will need
    to use the create child categories endpoint. It is highly recommended you
    use unique names for each category list. Using unique names allows you to
    select categories with just the name.

    Parameters
    ----------
        `template_type` (`str`): the template type of the page holding the categories
        `categories` (`list[Category]`): the categories you want to create
        `module_id` (`int`, optional): the moduleId of the page holding the categories; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the page holding the categories; defaults to `None`

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "templateType": template_type,
        "categories": categories,
    }

    if module_id is not None:
        data.update({"moduleId": module_id})
    if external_reference is not None:
        data.update({"externalReference": external_reference})

    return self.post(
        self.api_endpoint + "/v2/Categories/Create",
        headers=self.headers,
        data=json.dumps(data)
    )


def create_child_categories(
    self,
    categories: list[Category],
    *,
    module_id: int = None,
    external_reference: str = None
) -> dict[str, Any]:
    """
    Allows you to create categories under another category.

    Adding categories under a category prevents the parent category from being
    selected by a page. It is highly recommended you use unique names for each
    category list. Using unique names allows you to reliably select categories
    with just the name.

    Parameters
    ----------
        `categories` (`list[Category]`): the categories you want to create
        `module_id` (`int`): the moduleId of the page holding the categories
        `external_reference` (`int`): the externalReference of the page holding the categories

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "categories": categories,
    }

    if module_id is not None:
        data.update({"moduleId": module_id})
    if external_reference is not None:
        data.update({"externalReference": external_reference})

    return self.post(
        self.api_endpoint + "/v2/Categories/CreateChild",
        headers=self.headers,
        data=json.dumps(data)
    )


def update_categories(
    self,
    name: str,
    *,
    module_id: int = None,
    external_reference: str = None
) -> dict[str, Any]:
    """
    Allows you to change the name of a category.

    Parameters
    ----------
        `name` (`str`): the new name of the category
        `module_id` (`int`, optional): the moduleId of the category; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the category; defaults to `None`

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "name": name
    }

    if module_id is not None:
        data.update({"moduleId": module_id})
    if external_reference is not None:
        data.update({"externalReference": external_reference})

    return self.post(
        self.api_endpoint + "/v2/Categories/Update",
        headers=self.headers,
        data=json.dumps(data)
    )


def delete_categories(
    self,
    template_type: str,
    categories: list[Category],
    *,
    module_id: int = None,
    external_reference: str = None
) -> dict[str, Any]:
    """
    Allows you to create categories under another category.

    Parameters
    ----------
        `template_type` (`str`): the template type of the page you want
        `categories` (`list[Category]`): the categories you want to delete
        `module_id` (`int`, optional): the moduleId of the page you want; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the page you want; defaults to `None`

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "templateType": template_type,
        "categories": categories,
    }

    if module_id is not None:
        data.update({"moduleId": module_id})
    if external_reference is not None:
        data.update({"externalReference": external_reference})

    return self.delete(
        self.api_endpoint + "/v2/Categories/Delete",
        headers=self.headers,
        data=json.dumps(data)
    )
