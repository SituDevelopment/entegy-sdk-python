from icons import icon

import json
import os
import sys

sys.path.append(os.path.dirname(__file__))

Document: type = dict[str, any]
ExternalContent: type = dict[str, any]


def addDocuments(self, templateType: str, moduleId: int, fileDocuments: list[Document]):
    """
    Adds documents to a page.

    Parameters
    ----------
        `templateType` (`str`): the template type of the page you're adding the documents to
        `moduleId` (`int`): the moduleId of the page you're adding the documents to
        `fileDocuments` (`list[Document]`): the file documents you want to add

    The format of `` is as follows:
    ```python
        [
            {
                "name":"Power Point",
                "externalReference":"document-56454",
                "icon":icon["Film Reel"],
                "fileUrl":"https://example.org/powerpoints/session/44444/powerpoint.ppt"
            },
            {
                "name":"Demonstration Video",
                "externalReference":"document-56455",
                "icon":icon["Film Reel"],
                "fileUrl":"https://example.org/powerpoints/session/44444/demonstrationvideo.mp4"
            }
        ]
    ```

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "templateType": templateType,
        "moduleId": moduleId,
        "fileDocuments": fileDocuments,
    }

    resp = self.post(
        self.APIEndpoint + "/v2/Document/AddFile",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output


def addExternalContentDocuments(self, templateType: str, moduleId: int, externalContentItems: list[ExternalContent]):
    """
    Adds external content documents to a page.

    Parameters
    ----------
        `templateType` (`str`): the template type of the page you're adding the documents to
        `moduleId` (`int`): the moduleId of the page you're adding the documents to
        `externalContentItems` (`list[ExternalContent]`): the external content documents you want to add

    The format of `` is as follows:
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
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "templateType": templateType,
        "moduleId": moduleId,
        "externalContentItems": externalContentItems,
    }

    resp = self.post(
        self.APIEndpoint + "/v2/Document/AddExternalContent",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    output = resp.json()
    return output
