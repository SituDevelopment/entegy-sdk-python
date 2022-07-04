import requests, json, os, sys
sys.path.append(os.path.dirname(__file__))
from icons import icon

def addDocuments(self, templateType ,moduleId, fileDocuments):
    """
    Return all user profiles

    Arguments:
        templateType -- The template type of the page you're adding the documents to

        moduleId -- The moduleId of the page you're adding the documents to

        fileDocuments -- The file documents you want to add

        e.g.

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

    Returns:
        Base response object
    """
    data = {
        "projectId":self.projectID,
        "apiKey": self.apiKey,
        "templateType":templateType,
        "moduleId": moduleId,
        "fileDocuments": fileDocuments
    }

    resp = requests.post(self.APIEndpoint+"/v2/Document/AddFile", headers=self.headers, data=json.dumps(data))
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output

def addExternalContentDocuments(self, templateType ,moduleId, externalContentItems):
    """
    Return all user profiles

    Arguments:
        templateType -- The template type of the page you're adding the documents to

        moduleId -- The moduleId of the page you're adding the documents to

        externalContentItems -- The external content documents you want to add

        e.g.

        [
            {
                "name": "Test External Content",
                "icon": 69,
                "externalReference": "ext_content",
                "fileUrl": "https://www.youtube.com/watch?v=ieWm9T_GgSA",
                "type": "YouTube"
            }
        ]

    Returns:
        Base response object
    """
    data = {
        "projectId":self.projectID,
        "apiKey": self.apiKey,
        "templateType":templateType,
        "moduleId": moduleId,
        "externalContentItems": externalContentItems
    }

    resp = requests.post(self.APIEndpoint+"/v2/Document/AddExternalContent", headers=self.headers, data=json.dumps(data))
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output