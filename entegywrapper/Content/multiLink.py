from entegywrapper.entegySchemas.content import Link, NamedLink, TemplateType


def get_multi_links(
    self,
    template_type: TemplateType,
    *,
    module_id: int | None = None,
    external_reference: str | None = None
) -> list[NamedLink]:
    """
    Returns all the multi links associated with the content page.

    Parameters
    ----------
        `template_type` (`TemplateType`): the templateType of the page
        `module_id` (`int`, optional): the moduleId of the page; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the page; defaults to `None`

    Returns
    -------
        `list[NamedLink]`: all multi links associated with the content page
    """
    data = {
        "templateType":template_type
    }

    if module_id is not None:
        data["moduleId"] = module_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    else:
        raise ValueError("You must provide an identifier")

    response = self.post(
        self.api_endpoint + "/v2/MultiLink",
        headers=self.headers,
        data=data
    )

    return response["multiLinks"]


def add_multi_links(
    self,
    template_type: TemplateType,
    multi_links: list[Link],
    *,
    module_id: int | None = None,
    external_reference: str | None = None
):
    """
    Add multi links to a content page.

    Parameters
    ----------
        `template_type` (`TemplateType`): the templateType of the page to add links to
        `module_id` (`int`): the moduleId of the page to add links to
        `multi_links` (`list[Link]`, optional): the links to add; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the page; defaults to `None`

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
    """
    data = {
        "templateType":template_type,
        "multiLinks": multi_links
    }

    if module_id is not None:
        data["moduleId"] = module_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    else:
        raise ValueError("You must provide an identifier")

    self.post(
        self.api_endpoint + "/v2/MultiLink/Add",
        headers=self.headers,
        data=data
    )


def remove_multi_link(
    self,
    template_type: TemplateType,
    target_template_type: TemplateType,
    *,
    module_id: int | None = None,
    external_reference: str | None = None,
    target_module_id: int | None = None,
    target_external_reference: str | None = None,
):
    """
    Removes a single multi link from a page.

    Parameters
    ----------
        `template_type` (`TemplateType`): the templateType of the page to remove links from
        `target_template_type` (`TemplateType`): the templateType of the multi link to remove
        `module_id` (`int`, optional): the moduleId of the page to remove links from; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the page to remove links from; defaults to `None`
        `target_module_id` (`int`, optional): the moduleId of the multi link to remove; defaults to `None`
        `target_external_reference` (`str`, optional): the externalReference of the multi link to remove; defaults to `None`
    """
    data = {
        "templateType":template_type,
        "targetTemplateType": target_template_type
    }

    if module_id is not None:
        data["moduleId"] = module_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    else:
        raise ValueError("You must provide a page identifier")

    if target_external_reference is not None:
        data["targetExternalReference"] = target_external_reference
    elif target_module_id is not None:
        data["targetModuleId"] = target_module_id
    else:
        raise ValueError("You must provide a target identifier")

    self.post(
        self.api_endpoint + "/v2/MultiLink/Remove",
        headers=self.headers,
        data=data
    )


def remove_all_multi_links(
    self,
    template_type: TemplateType,
    *,
    module_id: int | None = None,
    external_reference: str | None = None,
    link_template_type: TemplateType | None = None
):
    """
    Removes all the multi links from a page.

    Parameters
    ----------
        `template_type` (`TemplateType`): the templateType of the page
        `module_id` (`int`, optional): the moduleId of the page; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the page; defaults to `None`
        `link_template_type` (`TemplateType`, optional): the templateType of the page; defaults to `None`
    """
    data = {
        "templateType":template_type
    }

    if module_id is not None:
        data["moduleId"] = module_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    else:
        raise ValueError("You must provide an identifier")

    if link_template_type is not None:
        data["linkTemplateType"] = link_template_type

    self.post(
        self.api_endpoint + "/v2/MultiLink/RemoveAll",
        headers=self.headers,
        data=data
    )
