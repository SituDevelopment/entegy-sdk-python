import json

from typing import Any

Link: type = dict[str, str | int]


def get_multi_links(
    self,
    template_type: str,
    *,
    module_id: int = None,
    external_reference: str = None
) -> dict[str, Any]:
    """
    Returns all the multi links associated with the content page.

    Parameters
    ----------
        `template_type` (`str`): the template type of the page you want
        `module_id` (`int`, optional): the moduleId of the page you want; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the page you want; defaults to `None`

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

    return self.post(
        self.api_endpoint + "/v2/MultiLink",
        headers=self.headers,
        data=json.dumps(data)
    )


def add_multi_links(
    self,
    template_type: str,
    multi_links: list[Link],
    *,
    module_id: int = None,
    external_reference: str = None
) -> dict[str, Any]:
    """
    Add multi links to a content page.

    Parameters
    ----------
        `template_type` (`str`): the template type of the page you want to add links to
        `module_id` (`int`): the moduleId of the page you want to add links to
        `multi_links` (`list[Link]`, optional): the links you want to add; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the page you want; defaults to `None`

    The format of `multi_links` is as follows:
    ```python
        [
            {
                "template_type": "Speaker",
                "moduleId":1
            },
            {
                "template_type": "Speaker",
                "externalReference": "au-speaker-1546895"
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
        "templateType":template_type,
        "multiLinks": multi_links,
    }

    if module_id is not None:
        data.update({"moduleId": module_id})
    if external_reference is not None:
        data.update({"externalReference": external_reference})

    return self.post(
        self.api_endpoint + "/v2/MultiLink/Add",
        headers=self.headers,
        data=json.dumps(data)
    )


def remove_multi_link(
    self,
    template_type: str,
    target_template_type: str,
    *,
    module_id: int = None,
    external_reference: str = None,
    target_module_id: int = None,
    target_external_reference: str = None,
) -> dict[str, Any]:
    """
    Removes a single multi link from a page.

    Parameters
    ----------
        `template_type` (`str`): the template type of the page you want to remove links from
        `target_template_type` (`str`): the template type of the multi link you want to remove
        `module_id` (`int`, optional): the moduleId of the page you want to remove links from; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the page you want to remove links from; defaults to `None`
        `target_module_id` (`int`, optional): the moduleId of the multi link you want to remove; defaults to `None`
        `target_external_reference` (`str`, optional): the externalReference of the multi link you want to remove; defaults to `None`

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "templateType":template_type,
        "targetTemplateType": target_template_type,
    }

    if module_id is not None:
        data.update({"moduleId": module_id})
    if external_reference is not None:
        data.update({"externalReference": external_reference})
    if target_external_reference is not None:
        data.update({"targetExternalReference": target_external_reference})
    if target_module_id is not None:
        data.update({"targetModuleId": target_module_id})

    return self.post(
        self.api_endpoint + "/v2/MultiLink/Remove",
        headers=self.headers,
        data=json.dumps(data)
    )


def remove_all_multi_links(
    self,
    template_type: str,
    *,
    module_id: int = None,
    external_reference: str = None,
    link_template_type: str = None
) -> dict[str, Any]:
    """
    Removes all the multi links from a page.

    Parameters
    ----------
        `template_type` (`str`): the template type of the page you want
        `module_id` (`int`, optional): the moduleId of the page you want; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the page you want; defaults to `None`
        `link_template_type` (`str`, optional): the template type of the page you want; defaults to `None`

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

    if link_template_type is not None:
        update_data = {"linkTemplateType": link_template_type}
        data.update(update_data)

    return self.post(
        self.api_endpoint + "/v2/MultiLink/RemoveAll",
        headers=self.headers,
        data=json.dumps(data)
    )
