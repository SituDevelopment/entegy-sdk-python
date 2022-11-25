import json

from typing import Any


def get_content(
    self,
    template_type: str,
    *,
    module_id: int = None,
    external_reference: str = None,
    include_categories: bool = False,
    include_documents: bool = False,
    include_links: bool = False,
    include_multi_links: bool = False,
    include_page_settings: bool = False,
) -> dict[str, Any]:
    """
    Returns an entire schedule.

    You can expand the response returned by optionally asking for categories,
    documents, links and multilinks. You should only request these if you need
    them as they will slow down the request.

    Parameters
    ----------
        `template_type` (`str`): the type of the template you want content from
        `module_id` (`int`, optional): the instance of the data you're after; defaults to `None`
        `external_reference` (`str`, optional): the external reference for the content you want; defaults to `None`
        `include_categories` (`bool`, optional): whether you want Categories in the response; defaults to `False`
        `include_documents` (`bool`, optional): whether you want Documents in the response; defaults to `False`
        `include_links` (`bool`, optional): whether you want Links in the response; defaults to `False`
        `include_multi_links` (`bool`, optional): whether you want MultiLinks in the response; defaults to `False`
        `include_page_settings` (`bool`, optional): whether you want PageSettings in the response; defaults to `False`

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "templateType": template_type,
        "includeCategories": include_categories,
        "includeDocuments": include_documents,
        "includeLinks": include_links,
        "includeMultiLinks": include_multi_links,
        "includePageSettings": include_page_settings,
    }

    if module_id is not None:
        data.update({"moduleId": module_id})
    if external_reference is not None:
        data.update({"externalReference": external_reference})

    return self.post(
        self.api_endpoint + "/v2/Content",
        headers=self.headers,
        data=json.dumps(data)
    )


def get_schedule_content(
    self,
    *,
    module_id: int = None,
    external_reference: str = None,
    include_categories: bool = False,
    include_documents: bool = False,
    include_links: bool = False,
    include_multi_links: bool = False,
    include_page_settings: bool = False,
) -> dict[str, Any]:
    """
    Returns an entire schedule.

    You can expand the response returned by optionally asking for categories,
    documents, links and multilinks. You should only request these if you need
    them as they will slow down the request.

    Parameters
    ----------
        `module_id` (`int`, optional): the instance of the data you're after; defaults to `None`
        `external_reference` (`str`, optional): the external reference for the content you want; defaults to `None`
        `include_categories` (`bool`, optional): whether you want Categories in the response; defaults to `False`
        `include_documents` (`bool`, optional): whether you want Documents in the response; defaults to `False`
        `include_links` (`bool`, optional): whether you want Links in the response; defaults to `False`
        `include_multi_links` (`bool`, optional): whether you want MultiLinks in the response; defaults to `False`
        `include_page_settings` (`bool`, optional): whether you want PageSettings in the response; defaults to `False`

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "includeCategories": include_categories,
        "includeDocuments": include_documents,
        "includeLinks": include_links,
        "includeMultiLinks": include_multi_links,
        "includePageSettings": include_page_settings,
        "moduleId": module_id,
    }

    if external_reference is not None:
        data.update({"externalReference": external_reference})

    return self.post(
        self.api_endpoint + "/v2/Content/Schedule",
        headers=self.headers,
        data=json.dumps(data)
    )


def create_content(
    self,
    content: dict,
    *,
    content_group: str = "Default"
) -> dict[str, Any]:
    """
    Creates a root content item. You can only create Template Types that are
    listed as root content.

    Parameters
    ----------
        `content` (`dict`): the content you are creating, supports templateType, name, mainImage and externalReference
        `content_group` (`str`, optional) the content group in the core this new root content should go in; defaults to "Default"

    The format of `content` is as follows:
    ```python
        {
            "templateType": "Schedule",
            "name": "Conference Program",
            "externalReference": ""
        }
    ```

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "contentGroup": content_group,
        "content": content,
    }

    return self.post(
        self.api_endpoint + "/v2/Content/Create",
        headers=self.headers,
        data=json.dumps(data)
    )


def add_children_content(
    self,
    template_type: str,
    child_template_type: str,
    children: list,
    *,
    module_id: int = None,
    external_reference: str = None,
) -> dict[str, Any]:
    """
    Adds children to templateType.

    Parameters
    ----------
        `template_type` (`string`): the template type the children are being added to
        `child_template_type` (`string`): the templateType for the children you're creating
        `children` (`list`): the page data you want to add to the root templateType
        `module_id` (`int`, optional): the name for the page; defaults to `None`
        `external_reference` (`str`, optional): the externalReference for the page; defaults to `None`

    The format of `children` is as follows:
    ```python
        [
            {
                "externalReference": "au-speaker-545415842",
                "name": "John Smith",
                "strings":
                    {
                        "copy": "John Smith is an expert on many fields. He holds many prestigious awards from many prestigious parties",
                        "companyAndPosition": "XYZ Widgets // Director"
                    },
                "category":3,
                "sortOrder" : 4
            },
            {
                "externalReference": "au-speaker-874561246",
                "name": "John Doe",
                "strings":
                    {
                        "copy": "John Doe is an expert on many fields. He holds many prestigious awards from many prestigious parties",
                        "companyAndPosition": "ACME Corp // Director",
                        "phoneNumber": "1300 123 456",
                        "emailAddress": "john.doe@acme.corp",
                        "website": "https://acme.corp",
                        "address": "123 Acme Street
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
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "templateType": template_type,
        "childTemplateType": child_template_type,
        "children": children,
    }

    if module_id is not None:
        data.update({"moduleId": module_id})
    if external_reference is not None:
        data.update({"externalReference": external_reference})

    return self.post(
        self.api_endpoint + "/v2/Content/AddChildren",
        headers=self.headers,
        data=json.dumps(data)
    )


def update_content(
    self,
    template_type: str,
    content: dict,
    *,
    module_id: int = None,
    external_reference: str = None
) -> dict[str, Any]:
    """
    Updates data within a content item.

    Parameters
    ----------
        `template_type` (`str`): the templateType you're updating
        `content` (`dict`): the content you're updating, supports the name, sort order, mainImage, strings and links
        `module_id` (`int`, optional): the moduleId of the page you're updating; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the page you're updating; defaults to `None`

    The format of `content` is as follows:
    ```python
        {
            "name": "Mr John Smith",
            "sortOrder":1
            "strings":
                {
                    "copy": "Mr John Smith is an expert on many fields. He holds many prestigious awards from many prestigious parties",
                    "companyAndPosition": "XYZ Widgets || Director"
                }
        }
    ```

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "templateType":template_type,
        "content": content,
    }

    if module_id is not None:
        data.update({"moduleId": module_id})
    if external_reference is not None:
        data.update({"externalReference": external_reference})

    return self.post(
        self.api_endpoint + "/v2/Content/Update",
        headers=self.headers,
        data=json.dumps(data)
    )


def delete_content(
    self,
    template_type: str,
    *,
    module_id: int = None,
    external_reference: str = None
) -> dict[str, Any]:
    """
    Allows you to delete a content resource from the Entegy System. Any content
    deleted is unrecoverable.

    WARNING
    -------
        Deleting root content will result in all child pages being deleted.

    Parameters
    ----------
        `template_type` (`str`): the templateType of the resource you're deleting
        `module_id` (`int`, optional): the moduleId of the page you're deleting; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the page you're deleting; defaults to `None`

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "templateType":template_type,
    }

    if module_id is not None:
        data.update({"moduleId": module_id})
    if external_reference is not None:
        data.update({"externalReference": external_reference})

    return self.delete(
        self.api_endpoint + "/v2/Content/Delete",
        headers=self.headers,
        data=json.dumps(data)
    )
