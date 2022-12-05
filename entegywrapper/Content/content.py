from entegywrapper.schemas.content import (
    Content,
    ContentChildCreate,
    TemplateType
)
from entegywrapper.schemas.schedule import Schedule


def get_content(
    self,
    template_type: TemplateType,
    *,
    module_id: int | None = None,
    external_reference: str | None = None,
    include_categories: bool = False,
    include_documents: bool = False,
    include_links: bool = False,
    include_multi_links: bool = False,
    include_page_settings: bool = False,
) -> dict:
    """
    Returns an entire schedule.

    Parameters
    ----------
        `template_type` (`TemplateType`): the templateType of the content
        `module_id` (`int`, optional): the moduleId of the content; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the content; defaults to `None`
        `include_categories` (`bool`, optional): whether to include Categories in the response; defaults to `False`
        `include_documents` (`bool`, optional): whether to include Documents in the response; defaults to `False`
        `include_links` (`bool`, optional): whether to include Links in the response; defaults to `False`
        `include_multi_links` (`bool`, optional): whether to include MultiLinks in the response; defaults to `False`
        `include_page_settings` (`bool`, optional): whether to include PageSettings in the response; defaults to `False`

    Raises
    ------
        `ValueError`: if no identifier is specified

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "templateType": template_type,
        "includeCategories": include_categories,
        "includeDocuments": include_documents,
        "includeLinks": include_links,
        "includeMultiLinks": include_multi_links,
        "includePageSettings": include_page_settings
    }

    if module_id is not None:
        data["moduleId"] = module_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    else:
        raise ValueError("Please specify an identifier")

    response = self.post(
        self.api_endpoint + "/v2/Content",
        headers=self.headers,
        data=data
    )

    return response


def get_schedule_content(
    self,
    *,
    module_id: int | None = None,
    external_reference: str | None = None,
    include_categories: bool = False,
    include_documents: bool = False,
    include_links: bool = False,
    include_multi_links: bool = False,
    include_page_settings: bool = False,
) -> Schedule:
    """
    Returns an entire schedule.

    Parameters
    ----------
        `module_id` (`int`, optional): the moduleId of the schedule; defaults to `None`
        `external_reference` (`str`, optional): the externalReference for the content; defaults to `None`
        `include_categories` (`bool`, optional): whether to include Categories in the response; defaults to `False`
        `include_documents` (`bool`, optional): whether to include Documents in the response; defaults to `False`
        `include_links` (`bool`, optional): whether to include Links in the response; defaults to `False`
        `include_multi_links` (`bool`, optional): whether to include MultiLinks in the response; defaults to `False`
        `include_page_settings` (`bool`, optional): whether to include PageSettings in the response; defaults to `False`

    Raises
    ------
        `ValueError`: if no identifier is specified

    Returns
    -------
        `Schedule`: the schedule
    """
    data = {
        "includeCategories": include_categories,
        "includeDocuments": include_documents,
        "includeLinks": include_links,
        "includeMultiLinks": include_multi_links,
        "includePageSettings": include_page_settings
    }

    if module_id is not None:
        data["moduleId"] = module_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    else:
        raise ValueError("Please specify an identifier")

    response = self.post(
        self.api_endpoint + "/v2/Content/Schedule",
        headers=self.headers,
        data=data
    )

    return response["content"]


def create_content(
    self,
    content: Content,
    *,
    content_group: str = "Default"
) -> int:
    """
    Creates a root content item.

    Parameters
    ----------
        `content` (`Content`): the content to create
        `content_group` (`str`, optional) the content group in the core this new root content should go in; defaults to "Default"
    """
    data = {
        "contentGroup": content_group,
        "content": content
    }

    response = self.post(
        self.api_endpoint + "/v2/Content/Create",
        headers=self.headers,
        data=data
    )

    return response["moduleId"]


def add_children_content(
    self,
    template_type: TemplateType,
    child_template_type: TemplateType,
    children: list[ContentChildCreate],
    *,
    module_id: int | None = None,
    external_reference: str | None = None,
):
    """
    Adds children to templateType.

    Parameters
    ----------
        `template_type` (`string`): the templateType the children are being added to
        `child_template_type` (`string`): the templateType for the children to create
        `children` (`list[ContentChildCreate]`): the page data to add to the root templateType
        `module_id` (`int`, optional): the name for the page; defaults to `None`
        `external_reference` (`str`, optional): the externalReference for the page; defaults to `None`

    Raises
    ------
        `ValueError`: if no identifier is specified
    """
    data = {
        "templateType": template_type,
        "childTemplateType": child_template_type,
        "children": children
    }

    if module_id is not None:
        data["moduleId"] = module_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    else:
        raise ValueError("Please specify an identifier")

    self.post(
        self.api_endpoint + "/v2/Content/AddChildren",
        headers=self.headers,
        data=data
    )


def update_content(
    self,
    template_type: TemplateType,
    content: Content,
    *,
    module_id: int | None = None,
    external_reference: str | None = None
):
    """
    Updates data within a content item.

    Parameters
    ----------
        `template_type` (`TemplateType`): the templateType to update
        `content` (`Content`): the content to update
        `module_id` (`int`, optional): the moduleId of the page to update; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the page to update; defaults to `None`

    Raises
    ------
        `ValueError`: if no identifier is specified
    """
    data = {
        "templateType": template_type,
        "content": content
    }

    if module_id is not None:
        data["moduleId"] = module_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    else:
        raise ValueError("Please specify an identifier")

    self.post(
        self.api_endpoint + "/v2/Content/Update",
        headers=self.headers,
        data=data
    )


def delete_content(
    self,
    template_type: TemplateType,
    *,
    module_id: int | None = None,
    external_reference: str | None = None
):
    """
    Deletes a content resource from the Entegy System. Any content deleted is
    unrecoverable.

    WARNING
    -------
        Deleting root content will result in all child pages being deleted.

    Parameters
    ----------
        `template_type` (`TemplateType`): the templateType of the resource to delete
        `module_id` (`int`, optional): the moduleId of the page to delete; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the page to delete; defaults to `None`

    Raises
    ------
        `ValueError`: if no identifier is specified
    """
    data = {
        "templateType": template_type
    }

    if module_id is not None:
        data["moduleId"] = module_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    else:
        raise ValueError("Please specify an identifier")

    self.delete(
        self.api_endpoint + "/v2/Content/Delete",
        headers=self.headers,
        data=data
    )
