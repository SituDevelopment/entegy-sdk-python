from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from entegywrapper.errors import (
    EntegyDuplicateExternalReferenceError,
    EntegyFailedRequestError,
    EntegyNoDataError,
)
from entegywrapper.schemas.content import Content, ContentChildCreate, TemplateType
from entegywrapper.schemas.schedule import Schedule

if TYPE_CHECKING:
    from entegywrapper import EntegyAPI


def get_content(
    self: EntegyAPI,
    template_type: TemplateType,
    *,
    module_id: Optional[int] = None,
    external_reference: Optional[str] = None,
    include_categories: bool = False,
    include_documents: bool = False,
    include_links: bool = False,
    include_multi_links: bool = False,
    include_page_settings: bool = False,
) -> Content:
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

        `EntegyFailedRequestError`: if the API request fails

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
        "includePageSettings": include_page_settings,
    }

    if module_id is not None:
        data["moduleId"] = module_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    else:
        raise ValueError("Please specify an identifier")

    response = self.post(self.api_endpoint + "/v2/Content", data=data)

    if "content" not in response:
        raise EntegyNoDataError("No content returned")

    return Content(**response["content"])


def get_schedule_content(
    self: EntegyAPI,
    *,
    module_id: Optional[int] = None,
    external_reference: Optional[str] = None,
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

        `external_reference` (`str`, optional): the externalReference of the schedule; defaults to `None`

        `include_categories` (`bool`, optional): whether to include Categories in the response; defaults to `False`

        `include_documents` (`bool`, optional): whether to include Documents in the response; defaults to `False`

        `include_links` (`bool`, optional): whether to include Links in the response; defaults to `False`

        `include_multi_links` (`bool`, optional): whether to include MultiLinks in the response; defaults to `False`

        `include_page_settings` (`bool`, optional): whether to include PageSettings in the response; defaults to `False`

    Raises
    ------
        `ValueError`: if no identifier is specified

        `EntegyFailedRequestError`: if the API request fails

    Returns
    -------
        `Schedule`: the schedule
    """
    data = {
        "includeCategories": include_categories,
        "includeDocuments": include_documents,
        "includeLinks": include_links,
        "includeMultiLinks": include_multi_links,
        "includePageSettings": include_page_settings,
    }

    if module_id is not None:
        data["moduleId"] = module_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    else:
        raise ValueError("Please specify an identifier")

    response = self.post(self.api_endpoint + "/v2/Content/Schedule", data=data)

    if "content" not in response:
        raise EntegyNoDataError("No content returned")

    # We're requesting data off the schedule end-point, so let's go ahead and assume a Schedule
    # template type if it's not provided.
    if not response["content"].get("templateType"):
        response["content"]["templateType"] = TemplateType.SCHEDULE

    return Schedule(**response["content"])


def create_content(
    self: EntegyAPI, content: dict[str, Any], *, content_group: str = "Default"
) -> int:
    """
    Creates a root content item.

    Parameters
    ----------
        `content` (`Content`): the content to create

        `content_group` (`str`, optional) the content group in the core this new root content should go in; defaults to "Default"

    Raises
    ------
        `EntegyFailedRequestError`: if the API request fails
    """
    data = {"contentGroup": content_group, "content": content}

    response = self.post(self.api_endpoint + "/v2/Content/Create", data=data)

    match response["response"]:
        case 200:
            return response["moduleId"]
        case 401:
            raise EntegyFailedRequestError("Missing or invalid template type")
        case 402:
            raise EntegyDuplicateExternalReferenceError("Duplicate External Reference")
        case 404:
            raise EntegyFailedRequestError("Missing Name")
        case 405:
            raise EntegyFailedRequestError("Invalid Content Group")
        case _:
            raise EntegyFailedRequestError(
                f"{response['response']}: {response.get('message', 'Unknown error')}"
            )


def add_children_content(
    self: EntegyAPI,
    template_type: TemplateType,
    child_template_type: TemplateType,
    children: list[dict[str, Any]],
    *,
    module_id: Optional[int] = None,
    external_reference: Optional[str] = None,
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

        `EntegyFailedRequestError`: if the API request fails
    """
    data = {
        "templateType": template_type,
        "childTemplateType": child_template_type,
        "children": children,
    }

    if module_id is not None:
        data["moduleId"] = module_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    else:
        raise ValueError("Please specify an identifier")

    response = self.post(self.api_endpoint + "/v2/Content/AddChildren", data=data)

    match response["response"]:
        case 200:
            return
        case 401:
            raise EntegyFailedRequestError("Missing ID")
        case 402:
            raise EntegyFailedRequestError("Page doesn't exist")
        case 404:
            raise EntegyFailedRequestError("Invalid Child Template ID")
        case 405:
            raise EntegyFailedRequestError("Missing Children")
        case 406:
            raise EntegyDuplicateExternalReferenceError("Duplicate External Reference")
        case _:
            raise EntegyFailedRequestError(response)


def update_content(
    self: EntegyAPI,
    template_type: TemplateType,
    content: dict[str, Any],
    *,
    module_id: Optional[int] = None,
    external_reference: Optional[str] = None,
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

        `EntegyFailedRequestError`: if the API request fails
    """
    data = {"templateType": template_type, "content": content}

    if module_id is not None:
        data["moduleId"] = module_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    else:
        raise ValueError("Please specify an identifier")

    response = self.post(self.api_endpoint + "/v2/Content/Update", data=data)

    match response["response"]:
        case 200:
            return
        case 400:
            raise EntegyFailedRequestError("Content not provided")
        case 401:
            raise EntegyFailedRequestError("Content doesn't exist")
        case 406:
            raise EntegyFailedRequestError("Invalid page setting")
        case 410:
            raise EntegyFailedRequestError("Invalid String")
        case 413:
            raise EntegyFailedRequestError("Link doesn't exist")


def delete_content(
    self: EntegyAPI,
    template_type: TemplateType,
    *,
    module_id: Optional[int] = None,
    external_reference: Optional[str] = None,
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

        `EntegyFailedRequestError`: if the API request fails
    """
    data = {"templateType": template_type}

    if module_id is not None:
        data["moduleId"] = module_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    else:
        raise ValueError("Please specify an identifier")

    response = self.delete(self.api_endpoint + "/v2/Content/Delete", data=data)

    match response["response"]:
        case 200:
            return
        case 401:
            raise EntegyFailedRequestError("Missing ID")
        case _:
            raise EntegyFailedRequestError(
                f"{response['response']}: {response.get('message', 'Unknown error')}"
            )
