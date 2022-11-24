import json
import os
import sys

from typing import Any

sys.path.append(os.path.dirname(__file__))

Document: type = dict[str, any]
ExternalContent: type = dict[str, any]


def add_documents(
    self,
    template_type: str,
    module_id: int,
    file_documents: list[Document]
) -> dict[str, Any]:
    """
    Adds documents to a page.

    Parameters
    ----------
        `template_type` (`str`): the template type of the page you're adding the documents to
        `module_id` (`int`): the moduleId of the page you're adding the documents to
        `file_documents` (`list[Document]`): the file documents you want to add

    The format of `file_documents` is as follows:
    ```python
        [
            {
                "name": "Power Point",
                "externalReference": "document-56454",
                "icon":icon["Film Reel"],
                "fileUrl": "https://example.org/powerpoints/session/44444/powerpoint.ppt"
            },
            {
                "name": "Demonstration Video",
                "externalReference": "document-56455",
                "icon":icon["Film Reel"],
                "fileUrl": "https://example.org/powerpoints/session/44444/demonstrationvideo.mp4"
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
        "moduleId": module_id,
        "fileDocuments": file_documents,
    }

    return self.post(
        self.api_endpoint + "/v2/Document/AddFile",
        headers=self.headers,
        data=json.dumps(data)
    )


def add_external_content_documents(
    self,
    template_type: str,
    module_id: int,
    external_content_items: list[ExternalContent]
) -> dict[str, Any]:
    """
    Adds external content documents to a page.

    Parameters
    ----------
        `template_type` (`str`): the template type of the page you're adding the documents to
        `module_id` (`int`): the moduleId of the page you're adding the documents to
        `external_content_items` (`list[ExternalContent]`): the external content documents you want to add

    The format of `external_content_items` is as follows:
    ```python
        [
            {
                "name": "Test External Content",
                "icon": 69,
                "externalReference": "ext_content",
                "fileUrl": "https://www.youtube.com/watch?v=ieWm9T_GgSA",
                "type": "YouTube"
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
        "moduleId": module_id,
        "externalContentItems": external_content_items,
    }

    return self.post(
        self.api_endpoint + "/v2/Document/AddExternalContent",
        headers=self.headers,
        data=json.dumps(data)
    )
