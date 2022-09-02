import json
import os
import sys
import time
from random import randint

import requests
from requests.structures import CaseInsensitiveDict

from .Profiles.profileCustom import deleteProfileCustom

sys.path.append(os.path.dirname(__file__))

APIEndpoints = {
    "AU": "https://api.entegy.com.au",
    "US": "https://api-us.entegy.com.au",
    "EU": "https://api-eu.entegy.com.au",
}

# API Constructor


class EntegyAPI:

    # Public variables
    apiKey = ""
    apiSecret = ""
    projectID = ""
    headers = CaseInsensitiveDict()
    APIEndpoint = ""

    # Import methods

    # Profiles
    from .Content.categories import (availableCategories, createCategories,
                                     createChildCategories, deleteCategories,
                                     deselectCategories, selectCategories,
                                     updateCategories)
    # Content
    from .Content.content import (addChildrenContent, createContent,
                                  deleteContent, getContent,
                                  getScheduleContent, updateContent)
    from .Content.documents import addDocuments, addExternalContentDocuments
    from .Content.multiLink import (addMultiLinks, getMultiLinks,
                                    removeAllMultiLinks, removeMultiLink)
    # Notifications
    from .Notification.notification import (sendBulkNotification,
                                            sendNotification)
    # Plugins
    from .Plugins.extAuth import externalAuthentication
    # Points
    from .Points.pointManagement import (awardPoints, getPointLeaderboard,
                                         getPoints)
    from .Profiles.profileCustom import (allProfileCustom, createProfileCustom,
                                         deleteProfileCustom, getProfileCustom,
                                         updateProfileCustom)
    from .Profiles.profileLinks import (clearProfileLinks,
                                        deSelectProfileLinks,
                                        multiSelectProfileLinks,
                                        pageProfileLinks, selectedProfileLinks,
                                        selectProfileLink)
    from .Profiles.profilePayments import addProfilePayment
    from .Profiles.profiles import (allProfiles, createProfile, deleteProfile,
                                    getProfile, sendWelcomeEmail, syncProfiles,
                                    updateProfile)
    from .Profiles.profileTypes import (allProfileTypes, createProfileType,
                                        deleteProfileType, getProfileType,
                                        updateProfileType)

    # Contruct api class with given params
    def __init__(self, apiKey, apiSecret, projectID, region="AU"):
        """
        Contruct an EntegyAPI wrapper

        Arguments:
            apiKey -- Entegy API key (Can either be a string, or an array of strings)

            apiSecret -- Entegy API secret key (Can either be a string, or an array of strings the same size as apiKey)

            projectID -- Entegy project ID

            region -- 'AU', 'US', 'EU' (Default = 'AU')
        """

        # If multiple API keys were given, ensure that equal amounts of each were given
        if isinstance(self.apiKey, list):
            if len(self.apiKey) != len(self.apiSecret):
                raise IndexError(
                    "Invalid amount of API Keys to Secrets. Number of each must be equal!"
                )

        # Set public variables
        self.apiKey = apiKey
        self.apiSecret = apiSecret
        self.projectID = projectID

        # Set API header
        self.headers["Content-Type"] = "application/json"

        # Set API endpoint
        self.APIEndpoint = APIEndpoints[region]

    def getKey(self):
        """Return API Key

        Returns:
            string: API Key
        """
        # If the initially provided key was not an array, return `self.apiKey`
        if not isinstance(self.apiKey, list):
            self.headers["Authorization"] = f"ApiKey {self.apiSecret}"
            return self.apiKey

        randKeyNum = randint(0, len(self.apiKey) - 1)

        self.headers["Authorization"] = f"ApiKey {self.apiSecret[randKeyNum]}"
        return self.apiKey[randKeyNum]

    def getEndpoint(self):
        """
        Returns:
        API endpoint URL
        """
        return self.APIEndpoint

    def post(self, endpoint, data):
        """
        Post the given `data` to the given `endpoint` of the Entegy API.

        Arguments:
            endpoint -- API endpoint to post to

            data -- Data to post
        """
        resp = None
        while resp == None:
            resp = requests.post(
                endpoint,
                headers=self.headers,
                data=json.dumps(data)
            )
            if resp == None:
                raise Exception("No reponse received from API")

            # If there is a rate limit issue, wait the remaining time and try again
            if resp.json()['response'] == 489:
                time.sleep(resp.json()["resetDuration"] + 2)
                resp = None

        return resp
