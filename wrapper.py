import requests
import json
from requests.structures import CaseInsensitiveDict

APIEndpoints = {
    "AU": "https://api.entegy.com.au",
    "US": "https://api-us.entegy.com.au",
    "EU": "https://api-eu.entegy.com.au"
}

# API Constructor
class EntegyAPI:

    # Public variables
    apiKey = ""
    apiSecret = ""
    projectID = ""

    # Private variables
    __headers = CaseInsensitiveDict()
    __APIEndpoint = ""

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
        self.__APIEndpoint = APIEndpoints[region]

        # Set API header
        self.__headers["Content-Type"] = "application/json"
        self.__headers["Authorization"] = f"ApiKey {apiSecret}"

    def getEndpoint(self):
        """
        Returns:
        API endpoint URL
        """
        return self.__APIEndpoint
    
    def allProfiles(self, returnLimit=100 ,params={}):
        """
        Delete user profile from ID

        Arguments:
            userID -- User profile ID

        Returns:
            Base response object
        """
        data = {
            "projectId":self.projectID,
            "apiKey": self.apiKey,
            "pagination": {
                "start":0,
                "limit":returnLimit
            }
        }

        data.update(params)

        resp = requests.post(self.__APIEndpoint+"/v2/Profile/All", headers=self.__headers, data=json.dumps(data))
        if resp == None:
            raise Exception("No reponse received from API")
        output = resp.json()
        return output

    def getProfile(self, userID):
        """
        Get user profile from ID

        Arguments:
            userID -- User profile ID

        Returns:
            User profile JSON output
        """
        data = {
            "projectId":self.projectID,
            "apiKey": self.apiKey,
            "profileId": userID
        }

        resp = requests.post(self.__APIEndpoint+"/v2/Profile/", headers=self.__headers, data=json.dumps(data))
        if resp == None:
            raise Exception("No reponse received from API")
        output = resp.json()
        return output
    
    def deleteProfile(self, userID):
        """
        Delete user profile from ID

        Arguments:
            userID -- User profile ID

        Returns:
            Base response object
        """
        data = {
            "projectId":self.projectID,
            "apiKey": self.apiKey,
            "profileId": userID
        }

        resp = requests.delete(self.__APIEndpoint+"/v2/Profile/Delete", headers=self.__headers, data=json.dumps(data))
        if resp == None:
            raise Exception("No reponse received from API")
        output = resp.json()
        return output
    
    def createProfile(self, profileObject):
        """
        Create user profile from profile JSON object
        
        Arguments:
            profileObject -- User profile JSON object
            e.g.
            {
                "externalReference":"au-prf-31242354253",
                "firstName":"John",
                "lastName":"Smith",
                "type":"Attendee"
                /* rest of profile object (all extra fields are optional)*/
            }
                    
        Returns:
            Reponse code, success/error message, and profileID in JSON format"""

        data = {
            "projectId":self.projectID,
            "apiKey": self.apiKey,
            "profile": profileObject
        }
        print(data)
        resp = requests.post(self.__APIEndpoint+"/v2/Profile/Create", headers=self.__headers, data=json.dumps(data))
        if resp == None:
            raise Exception("No reponse received from API")
        output = resp.json()
        return output
    
    def updateProfile(self, profileID, profileObject):
        """
        Update user profile from profile JSON object 
        
        Arguments:
            profileID -- User profile ID to update
            
            profileObject -- User profile JSON object
            e.g.
            {
                "firstName":"Fred",
                "imageUrl":"https://images.example.org/profileimages/fredsmith/image.png"
            }
                    
        Returns:
            Base response object"""

        data = {
            "projectId":self.projectID,
            "apiKey": self.apiKey,
            "profileID": profileID,
            "profile": profileObject
        }
        print(data)
        resp = requests.post(self.__APIEndpoint+"/v2/Profile/Update", headers=self.__headers, data=json.dumps(data))
        if resp == None:
            raise Exception("No reponse received from API")
        output = resp.json()
        return output

    def syncProfiles(self, updateReferenceType, profiles, groupByFirstProfile = False):
        """
        Sync user profiles with reference to updateReferenceType
        
        Arguments:
            updateReferenceType -- The identifier to use to match profiles for updating. profileId, internalReference, externalReference, badgeReference
            
            profiles -- The list of profiles you want to create or update
            e.g.
            [
                {
                    "profileId": "ff11c742-346e-4874-9e24-efe6980a7453",
                    "customFields": 
                    {
                        "favourite-Food": "Pizza",
                        "water-Preference": "Cold Water"
                    }
                },
                {
                    "profileId": "4255a414-d95c-4106-a988-d0e10947ede5",
                    "customFields": 
                    {
                        "favourite-Food": "Pizza",
                        "water-Preference": "Cold Water"
                    }
                },
                {
                    "firstName": "Test",
                    "lastName": "User",
                    "type": "attendee",
                    "customFields": 
                    {
                        "favourite-Food": "Pizza",
                        "water-Preference": "Cold Water"
                    }
                }
            ]

        groupByFirstProfile	-- If true the parent profile of all profiles in this sync will be set to the first profile in the profiles list (except the first profile itself, which will be set to have no parent)
                    
        Returns:
            This endpoint returns a base response with an array of specific profile results in the same input order as the request"""

        data = {
            "projectId":self.projectID,
            "apiKey": self.apiKey,
            "updateReferenceType": updateReferenceType,
            "profiles": profiles
        }
        print(data)
        resp = requests.post(self.__APIEndpoint+"/v2/Profile/Sync", headers=self.__headers, data=json.dumps(data))
        if resp == None:
            raise Exception("No reponse received from API")
        output = resp.json()
        return output

    def getProfileType(self, name):
        """
        This request will get a single profile type
        
        Arguments:
            name -- The name of the profile type
                    
        Returns:
            The requested profile"""

        data = {
            "projectId":self.projectID,
            "apiKey": self.apiKey,
            "name": name
        }
        print(data)
        resp = requests.post(self.__APIEndpoint+"/v2/ProfileType", headers=self.__headers, data=json.dumps(data))
        if resp == None:
            raise Exception("No reponse received from API")
        output = resp.json()
        return output

    def createProfileType(self, profileType):
        """
        Creates a ProfileType with the data passed in the profileType
        
        Arguments:
            profileType -- The data for the profile type you're creating
            
            e.g.
            {
                "name":"Exhibitor",
                "externalReference":"au-ref-tickettype-564545"
            }
                    
        Returns:
            Base response object"""

        data = {
            "projectId":self.projectID,
            "apiKey": self.apiKey,
            "profileType": profileType
        }
        print(data)
        resp = requests.post(self.__APIEndpoint+"/v2/ProfileType/Create", headers=self.__headers, data=json.dumps(data))
        if resp == None:
            raise Exception("No reponse received from API")
        output = resp.json()
        return output
    
    def updateProfileType(self, name, profileType):
        """
        Updates the ProfileType with the data passed in the profileType
        
        Arguments:
            name -- The name of the profile type

            profileType -- The data you wish to update

            e.g.

            {
                "externalReference":"au-ref-tickettype-564545"
            }
                    
        Returns:
            Base response object"""

        data = {
            "projectId":self.projectID,
            "apiKey": self.apiKey,
            "name": name,
            "profileType": profileType
        }
        print(data)
        resp = requests.post(self.__APIEndpoint+"/v2/ProfileType/Update", headers=self.__headers, data=json.dumps(data))
        if resp == None:
            raise Exception("No reponse received from API")
        output = resp.json()
        return output

    def deleteProfileType(self, name):
        """
        Deletes a profile type. The type cannot be in use.
        
        Arguments:
            name -- The name of the profile type
                    
        Returns:
            Base response object"""

        data = {
            "projectId":self.projectID,
            "apiKey": self.apiKey,
            "name": name
        }
        print(data)
        resp = requests.delete(self.__APIEndpoint+"/v2/ProfileType/Delete", headers=self.__headers, data=json.dumps(data))
        if resp == None:
            raise Exception("No reponse received from API")
        output = resp.json()
        return output
    
    def allProfileTypes(self):
        """
        This request will get all profile types
                    
        Returns:
            All profileTypes"""

        data = {
            "projectId":self.projectID,
            "apiKey": self.apiKey
        }
        print(data)
        resp = requests.post(self.__APIEndpoint+"/v2/ProfileType/All", headers=self.__headers, data=json.dumps(data))
        if resp == None:
            raise Exception("No reponse received from API")
        output = resp.json()
        return output
    
    def getProfileCustom(self, key):
        """
        This request will get a single custom field
                    
        Arguments:
            key -- The key of the custom field to return
        
        Returns:
            The requested customField object"""

        data = {
            "projectId":self.projectID,
            "apiKey": self.apiKey,
            "key": key
        }
        print(data)
        resp = requests.post(self.__APIEndpoint+"/v2/ProfileCustomField", headers=self.__headers, data=json.dumps(data))
        if resp == None:
            raise Exception("No reponse received from API")
        output = resp.json()
        return output

    def createProfileCustom(self, customField):
        """
        Creates a new Custom Field for Profiles.

        There is a limited number of text custom fields allowed per project. Once a custom field is created, it's type cannot be modified.
                    
        Arguments:
            customField -- The custom field you wish to create

            e.g.

            {
                "key":"dietary-requirements",
                "name":"Dietary requirements",
                "type":"MultiChoice",
                "options":[
                    {
                        "name":"Halal"           
                    },
                    {
                        "name":"Vegan"
                    },
                    {
                        "name":"Lactose Intolerant"
                    },
                    {
                        "name":"Gluten Intolerant"
                    }
                ]
            }
        
        Returns:
            Base response object"""

        data = {
            "projectId":self.projectID,
            "apiKey": self.apiKey,
            "customField": customField
        }
        print(data)
        resp = requests.post(self.__APIEndpoint+"/v2/ProfileCustomField/Create", headers=self.__headers, data=json.dumps(data))
        if resp == None:
            raise Exception("No reponse received from API")
        output = resp.json()
        return output
    
    def updateProfileCustom(self, key, customField):
        """
        Update custom profile 'key' with 'customField' data
                    
        Arguments:
            key -- The key of the custom field to return

            customField -- The data to update the field with

            e.g.

            {
                "options":[
                    {
                        "optionId": 6,
                        "name":""
                    },
                    {
                        "optionId": 7,
                        "name":"Halal"           
                    },
                    {
                        "optionId": 8,
                        "name":"Vegan"
                    },
                    {
                        "name":"Lactose Intolerant"
                    },
                    {
                        "name":"Gluten Intolerant"
                    }
                ]
            }
        
        Returns:
            The requested customField object"""

        data = {
            "projectId":self.projectID,
            "apiKey": self.apiKey,
            "key": key
        }
        print(data)
        resp = requests.post(self.__APIEndpoint+"/v2/ProfileCustomField/Update", headers=self.__headers, data=json.dumps(data))
        if resp == None:
            raise Exception("No reponse received from API")
        output = resp.json()
        return output
    
    def deleteProfileCustom(self, key):
        """
        This request will delete a single custom field
                    
        Arguments:
            key -- The key of the custom field to delete
        
        Returns:
            Base response object"""

        data = {
            "projectId":self.projectID,
            "apiKey": self.apiKey,
            "key": key
        }
        print(data)
        resp = requests.delete(self.__APIEndpoint+"/v2/ProfileCustomField/Delete", headers=self.__headers, data=json.dumps(data))
        if resp == None:
            raise Exception("No reponse received from API")
        output = resp.json()
        return output

    def alldeleteProfileCustom(self):
        """
        This request will return all custom fields
        
        Returns:
            List of all customFields"""

        data = {
            "projectId":self.projectID,
            "apiKey": self.apiKey
        }
        print(data)
        resp = requests.post(self.__APIEndpoint+"/v2/ProfileCustomField/All", headers=self.__headers, data=json.dumps(data))
        if resp == None:
            raise Exception("No reponse received from API")
        output = resp.json()
        return output
    