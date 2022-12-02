from entegywrapper.entegySchemas.content import Category, TemplateType


def available_categories(
    self,
    template_type: TemplateType,
    *,
    module_id: int | None = None,
    external_reference: str | None = None,
) -> list[Category]:
    """
    Returns the list of available categories for the page specified by the given
    identifier.

    Parameters
    ----------
        `template_type` (`TemplateType`): the templateType of the page
        `module_id` (`int`, optional): the moduleId of the page; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the page; defaults to `None`

    Returns
    -------
        `list[Category]`: the available categories
    """
    data = {
        "templateType": template_type
    }

    if module_id is not None:
        data["moduleId"] = module_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    else:
        raise ValueError("You must provide an identifier")

    response = self.post(
        self.api_endpoint + "/v2/Categories/Available",
        headers=self.headers,
        data=data
    )

    return response["availableCategories"]


def select_categories(
    self,
    template_type: TemplateType,
    categories: list[Category],
    *,
    module_id: int | None = None,
    external_reference: str | None = None
):
    """
    Selects the specified categories for the specified content page.

    Parameters
    ----------
        `template_type` (`TemplateType`): the templateType of the page selecting the categories
        `categories` (`list[Category]`): the categories to select
        `module_id` (`int`, optional): the moduleId of the page selecting the categories; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the page selecting the categories; defaults to `None`
    """
    data = {
        "templateType": template_type,
        "categories": categories
    }

    if module_id is not None:
        data["moduleId"] = module_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    else:
        raise ValueError("You must provide an identifier")

    self.post(
        self.api_endpoint + "/v2/Categories/Select",
        headers=self.headers,
        data=data
    )


def deselect_categories(
    self,
    template_type: TemplateType,
    categories: list[Category],
    *,
    module_id: int | None = None,
    external_reference: str | None = None
):
    """
    Deselects the specified categories for the specified content page.

    Parameters
    ----------
        `template_type` (`TemplateType`): the templateType of the page to unselect the categories from
        `categories` (`list[Category]`): the categories to select
        `module_id` (`int`, optional): the moduleId of the page to unselect the categories from; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the page to unselect the categories from; defaults to `None`
    """
    data = {
        "templateType": template_type,
        "categories": categories
    }

    if module_id is not None:
        data["moduleId"] = module_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    else:
        raise ValueError("You must provide an identifier")

    self.post(
        self.api_endpoint + "/v2/Categories/Deselect",
        headers=self.headers,
        data=data
    )


def create_categories(
    self,
    template_type: TemplateType,
    categories: list[Category],
    *,
    module_id: int | None = None,
    external_reference: str | None = None
):
    """
    Create categories under a root page.

    Parameters
    ----------
        `template_type` (`TemplateType`): the templateType of the page holding the categories
        `categories` (`list[Category]`): the categories to create
        `module_id` (`int`, optional): the moduleId of the page holding the categories; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the page holding the categories; defaults to `None`
    """
    data = {
        "templateType": template_type,
        "categories": categories
    }

    if module_id is not None:
        data["moduleId"] = module_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    else:
        raise ValueError("You must provide an identifier")

    self.post(
        self.api_endpoint + "/v2/Categories/Create",
        headers=self.headers,
        data=data
    )


def create_child_categories(
    self,
    categories: list[Category],
    *,
    module_id: int | None = None,
    external_reference: str | None = None
):
    """
    Creates categories under another category.

    Parameters
    ----------
        `categories` (`list[Category]`): the categories to create
        `module_id` (`int`): the moduleId of the page holding the categories
        `external_reference` (`int`): the externalReference of the page holding the categories
    """
    data = {
        "categories": categories
    }

    if module_id is not None:
        data["moduleId"] = module_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    else:
        raise ValueError("You must provide an identifier")

    self.post(
        self.api_endpoint + "/v2/Categories/CreateChild",
        headers=self.headers,
        data=data
    )


def update_categories(
    self,
    name: str,
    *,
    module_id: int | None = None,
    external_reference: str | None = None
):
    """
    Allows you to change the name of a category.

    Parameters
    ----------
        `name` (`str`): the new name of the category
        `module_id` (`int`, optional): the moduleId of the category; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the category; defaults to `None`
    """
    data = {
        "name": name
    }

    if module_id is not None:
        data["moduleId"] = module_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    else:
        raise ValueError("You must provide an identifier")

    self.post(
        self.api_endpoint + "/v2/Categories/Update",
        headers=self.headers,
        data=data
    )


def delete_categories(
    self,
    template_type: TemplateType,
    categories: list[Category],
    *,
    module_id: int | None = None,
    external_reference: str | None = None
):
    """
    Allows you to create categories under another category.

    Parameters
    ----------
        `template_type` (`TemplateType`): the templateType of the page
        `categories` (`list[Category]`): the categories to delete
        `module_id` (`int`, optional): the moduleId of the page; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the page; defaults to `None`
    """
    data = {
        "templateType": template_type,
        "categories": categories
    }

    if module_id is not None:
        data["moduleId"] = module_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    else:
        raise ValueError("You must provide an identifier")

    self.delete(
        self.api_endpoint + "/v2/Categories/Delete",
        headers=self.headers,
        data=data
    )
