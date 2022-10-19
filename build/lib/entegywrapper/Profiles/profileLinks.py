import json

Link: type = dict
"""
The format of a `Link` is as follows:
    ```python
        {
            "templateType":"session",
            "moduleId":1
        }
    ```
"""


def selectedProfileLinks(
    self,
    profileId: str,
    returnLimit: int = 100
):
    """
    Return all the profile links the profile has.

    Parameters
    ----------
        `profileId` (`str`): the profileId of the profile
        `returnLimit` (`int`): the index and amount of results to return; defaults to 100

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "profileID": profileId,
        "pagination": {
            "index": 0,
            "limit": returnLimit
        },
    }

    resp = self.post(
        self.APIEndpoint + "/v2/ProfileLink/Selected/",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    if isinstance(resp, dict):
        return resp
    output = resp.json()
    return output


def pageProfileLinks(
    self,
    templateType: str,
    moduleId: str,
    returnLimit: int = 100
):
    """
    Gets all the profiles linked to a Content Page.

    Parameters
    ----------
        `templateType` (`str`): the templateType of the page
        `moduleId` (`int`): the moduleId of the page
        `returnLimit` (`int`): the maximum number of results to return; defaults to 100

    Returns
    -------
        Pagination response and list of profile objects
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "templateType": templateType,
        "moduleId": moduleId,
        "pagination": {
            "index": 0,
            "limit": returnLimit
        },
    }

    resp = self.post(
        self.APIEndpoint + "/v2/ProfileLink/Page/",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    if isinstance(resp, dict):
        return resp
    output = resp.json()
    return output


def selectProfileLink(
    self,
    profileId: str,
    link: Link
):
    """
    Allows you to select a link for a profile

    Parameters
    ----------
        `profileId` (`str`): the profileId of the profile
        `link` (`Link`): the link you wish to select
    ```

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "profileID": profileId,
        "link": link,
    }

    resp = self.post(
        self.APIEndpoint + "/v2/ProfileLink/Select/",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    if isinstance(resp, dict):
        return resp
    output = resp.json()
    return output


def multiSelectProfileLinks(
    self,
    profiles: list[str, str | list[Link]]
):
    """
    Allows you to select multiple pages on multiple profiles at once

    Parameters
    ----------
        `profiles` (`list[str, str | list[Link]]`): list of profile references with link objects within

    The format of `profiles` is as follows:
    ```python
        [
            {
                "profileId":"ff11c742-346e-4874-9e24-efe6980a7453",
                "links": [
                    {
                        "templateType":"sesSiOn",
                        "moduleId":1
                    },
                    {
                        "templateType":"sesSiOn",
                        "moduleId":2
                    },
                    {
                        "templateType":"sesSiOn",
                        "moduleId":3
                    }
                ]
            },
        ]
    ```

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "profiles": profiles
    }

    resp = self.post(
        self.APIEndpoint + "/v2/ProfileLink/MultiSelect/",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    if isinstance(resp, dict):
        return resp
    output = resp.json()
    return output


def deSelectProfileLinks(
    self,
    profileId: str,
    link: Link
):
    """
    Allows you to deselect a link for a profile.

    Parameters
    ----------
        `profileId` (`str`): the profileId of the profile
        `link` (`Link`): the link you wish to deselect

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "profileId": profileId,
        "link": link,
    }

    resp = self.post(
        self.APIEndpoint + "/v2/ProfileLink/Deselect/",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    if isinstance(resp, dict):
        return resp
    output = resp.json()
    return output


def clearProfileLinks(
    self,
    profileId,
    templateType
):
    """
    Allows you to clear all the selected links of a templateType on a single profile

    Parameters
    ----------
        `profileId` (`str`): the profileId of the profile
        `templateType` (`str`): the templateType to clear links of

    Returns
    -------
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "profileId": profileId,
        "templateType": templateType,
    }

    resp = self.post(
        self.APIEndpoint + "/v2/ProfileLink/Clear/",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    if isinstance(resp, dict):
        return resp
    output = resp.json()
    return output
