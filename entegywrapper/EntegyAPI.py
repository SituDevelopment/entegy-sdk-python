from random import randint
import time
import requests
import json
import sys
import os
from requests.structures import CaseInsensitiveDict

sys.path.append(os.path.dirname(__file__))
from .Profiles.profileCustom import deleteProfileCustom

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
    currentKeyPair = 0

    # Import methods

    # Profiles
    from .Profiles.profiles import (
        allProfiles,
        createProfile,
        getProfile,
        deleteProfile,
        updateProfile,
        syncProfiles,
        sendWelcomeEmail,
    )
    from .Profiles.profileTypes import (
        getProfileType,
        createProfileType,
        updateProfileType,
        deleteProfileType,
        allProfileTypes,
    )
    from .Profiles.profileCustom import (
        getProfileCustom,
        createProfileCustom,
        updateProfileCustom,
        deleteProfileCustom,
        allProfileCustom,
    )
    from .Profiles.profileLinks import (
        selectedProfileLinks,
        pageProfileLinks,
        selectProfileLink,
        multiSelectProfileLinks,
        deSelectProfileLinks,
        clearProfileLinks,
    )
    from .Profiles.profilePayments import addProfilePayment

    # Content
    from .Content.content import (
        getContent,
        getScheduleContent,
        createContent,
        addChildrenContent,
        updateContent,
        deleteContent,
    )
    from .Content.categories import (
        availableCategories,
        selectCategories,
        deselectCategories,
        createCategories,
        createChildCategories,
        updateCategories,
        deleteCategories,
    )
    from .Content.documents import addDocuments, addExternalContentDocuments
    from .Content.multiLink import (
        getMultiLinks,
        addMultiLinks,
        removeMultiLink,
        removeAllMultiLinks,
    )

    # Points
    from .Points.pointManagement import awardPoints, getPointLeaderboard, getPoints

    # Plugins
    from .Plugins.extAuth import externalAuthentication

    # Notifications
    from .Notification.notification import sendNotification, sendBulkNotification

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

        self.headers["Authorization"] = f"ApiKey {self.apiSecret[self.currentKeyPair]}"
        return self.apiKey[self.currentKeyPair]
    
    def cycleKey(self):
        """
        Cycle through the API keys provided in the constructor
        """

        self.currentKeyPair += 1
        if self.currentKeyPair >= len(self.apiKey):
            self.currentKeyPair = 0

    def getEndpoint(self):
        """
        Returns:
        API endpoint URL
        """
        return self.APIEndpoint

    def post(self, endpoint, data, headers=[]):
        """
        Post the given `data` to the given `endpoint` of the Entegy API.

        Arguments:
            endpoint -- API endpoint to post to

            data -- Data to post

            headers -- API headers; defaults to the empty list
        """
        resp = None
        retryCount = 0
        permErrorCount = 0
        while resp == None:
            resp = requests.post(
                endpoint,
                headers=headers,
                data=data
            )
            if resp == None:
                raise Exception("No reponse received from API")
            if resp.json()['response'] == 403:
                time.sleep(0.5)
                permErrorCount += 1
                if permErrorCount >= 5:
                    raise Exception("Invalid API Key")
                resp == None
            # If there is a rate limit issue, wait the remaining time and try again
            elif resp.json()['response'] == 489:
                # Turn 'data' string back into a dictionary, then revert it back after changing the apiKey
                if retryCount >= len(self.apiKey):
                    print("Rate limit reached, waiting " + str(resp.json()['resetDuration']) + " seconds")
                    time.sleep(resp.json()["resetDuration"] + 2)
                    print("Continuing...")
                    resp = None
                else:
                    self.cycleKey()
                    data = json.loads(data)
                    data["apiKey"] = self.getKey()
                    headers = self.headers
                    print(f"Rate limit reached, trying alternate key: {data['apiKey']}")
                    data = json.dumps(data)
                    retryCount+=1
                    resp = None

        return resp
