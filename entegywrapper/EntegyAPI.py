from random import randint
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

    # Import methods

    # Profiles
    from .Profiles.profiles import (
        allProfiles,
        createProfile,
        getProfile,
        deleteProfile,
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
