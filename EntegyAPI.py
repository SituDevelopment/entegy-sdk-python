import requests
import json
from requests.structures import CaseInsensitiveDict

from Profiles.profileCustom import deleteProfileCustom

APIEndpoints = {
    "AU": "https://api.entegy.com.au",
    "US": "https://api-us.entegy.com.au",
    "EU": "https://api-eu.entegy.com.au"
}

# API Constructor
class EntegyAPI():

    # Public variables
    apiKey = ""
    apiSecret = ""
    projectID = ""
    headers = CaseInsensitiveDict()
    APIEndpoint = ""

    # Import methods

    # Profiles
    from Profiles.profiles import allProfiles, createProfile, getProfile, deleteProfile, syncProfiles, sendWelcomeEmail
    from Profiles.profileTypes import getProfileType, createProfileType, updateProfileType, deleteProfileType, allProfileTypes
    from Profiles.profileCustom import getProfileCustom, createProfileCustom, updateProfileCustom, deleteProfileCustom, allProfileCustom
    from Profiles.profileLinks import selectedProfileLinks, pageProfileLinks, selectProfileLink, multiSelectProfileLinks, deSelectProfileLinks, clearProfileLinks
    from Profiles.profilePayments import addProfilePayment
    
    # Content
    from Content.content import getContent, getScheduleContent, createContent, addChildrenContent, updateContent, deleteContent
    from Content.categories import availableCategories, selectCategories, deselectCategories, createCategories, createChildCategories, updateCategories, deleteCategories
    from Content.documents import addDocuments, addExternalContentDocuments
    from Content.multiLink import getMultiLinks, addMultiLinks, removeMultiLink, removeAllMultiLinks

    # Contruct api class with given params
    def __init__(self, apiKey, apiSecret, projectID, region = 'AU'):
        """
        Contruct an EntegyAPI wrapper

        Arguments:
            apiKey -- Entegy API key

            apiSecret -- Entegy API secret key

            projectID -- Entegy project ID

            region -- 'AU', 'US', 'EU' (Default = 'AU')
        """

        # Set public variables
        self.apiKey = apiKey
        self.apiSecret = apiSecret
        self.projectID = projectID

        # Set API endpoint
        self.APIEndpoint = APIEndpoints[region]

        # Set API header
        self.headers["Content-Type"] = "application/json"
        self.headers["Authorization"] = f"ApiKey {apiSecret}"

    def getEndpoint(self):
        """
        Returns:
        API endpoint URL
        """
        return self.APIEndpoint
    

    
    
    
    