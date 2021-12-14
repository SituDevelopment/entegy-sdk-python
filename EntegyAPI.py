import requests
import json
from requests.structures import CaseInsensitiveDict

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
    from Profiles.profiles import allProfiles, createProfile, getProfile, deleteProfile, syncProfiles

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
    

    
    
    
    