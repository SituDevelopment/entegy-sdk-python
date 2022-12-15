import os
import sys

from entegywrapper.schemas.content import Document, ExternalContent, TemplateType

sys.path.append(os.path.dirname(__file__))


def add_documents(
    self, template_type: TemplateType, module_id: int, file_documents: list[Document]
):
    """
    Adds documents to a page.

    Parameters
    ----------
        `template_type` (`TemplateType`): the templateType of the page to add the documents to
        `module_id` (`int`): the moduleId of the page to add the documents to
        `file_documents` (`list[Document]`): the file documents to add
    """
    data = {
        "templateType": template_type,
        "moduleId": module_id,
        "fileDocuments": file_documents,
    }

    self.post(self.api_endpoint + "/v2/Document/AddFile", data=data)


def add_external_content_documents(
    self,
    template_type: TemplateType,
    module_id: int,
    external_content_items: list[ExternalContent],
):
    """
    Adds external content documents to a page.

    Parameters
    ----------
        `template_type` (`TemplateType`): the templateType of the page to add the documents to
        `module_id` (`int`): the moduleId of the page to add the documents to
        `external_content_items` (`list[ExternalContent]`): the external content documents to add
    """
    data = {
        "templateType": template_type,
        "moduleId": module_id,
        "externalContentItems": external_content_items,
    }

    self.post(self.api_endpoint + "/v2/Document/AddExternalContent", data=data)
