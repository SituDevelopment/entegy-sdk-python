# Python SDK for the Entegy API

## Installation

```bash
pip install entegywrapper

poetry add entegywrapper
```

## Usage

```python
from entegywrapper import EntegyAPI

api = EntegyAPI("api-key", "api-secret", "project-id", "project-region")
api = EntegyAPI(["api-key-1", "api-key-2", "api-key-3"], ["api-secret-1", "api-secret-2", "api-secret-3"], "project-id", "project-region")
```

## Ported Modules

-   API Objects
-   Content
    -   [Content Objects](https://situ.entegysuite.com.au/Docs/Api/content-objects)
    -   [Content Management](https://situ.entegysuite.com.au/Docs/Api/content-get)
    -   [Categories](https://situ.entegysuite.com.au/Docs/Api/category-available)
    -   [Documents](https://situ.entegysuite.com.au/Docs/Api/document-addfile)
    -   [MultiLinks](https://situ.entegysuite.com.au/Docs/Api/multilink-get)
-   Attendance Tracking
    -   [Attendance Tracking Objects](https://situ.entegysuite.com.au/Docs/Api/track-objects)
    -   [Track Management](https://situ.entegysuite.com.au/Docs/Api/track-addcheckin)
-   Notification
    -   [Notification - Send Bulk](https://situ.entegysuite.com.au/Docs/Api/notifications-send-bulk)
-   Plugins
    -   [External Authentication](https://situ.entegysuite.com.au/Docs/Api/plugins-authenticate-external)
-   Points & Achievement
    -   [Points & Achievement Objects](https://situ.entegysuite.com.au/Docs/Api/point-constants)
    -   [Point Management](https://situ.entegysuite.com.au/Docs/Api/point-award)
-   Profile
    -   [Profile Objects](https://situ.entegysuite.com.au/Docs/Api/profile-object)
    -   [Profile Management](https://situ.entegysuite.com.au/Docs/Api/profile-get)
    -   [Profile Types](https://situ.entegysuite.com.au/Docs/Api/profiletype-get)
    -   [Profile Custom Fields](https://situ.entegysuite.com.au/Docs/Api/profilecustomfield-get)
    -   [Profile Links](https://situ.entegysuite.com.au/Docs/Api/profilelink-selected)
    -   [Profile Payments](https://situ.entegysuite.com.au/Docs/Api/profile-payment-add)

## Modules to Port

-   Lead Capture
    -   [Lead Capture Objects](https://situ.entegysuite.com.au/Docs/Api/lead-capture-objects)
    -   [Lead Capture Management](https://situ.entegysuite.com.au/Docs/Api/capture-lead-add)
-   Points & Achievement
    -   [Achievement Management](https://situ.entegysuite.com.au/Docs/Api/achievement-all)
-   Project
    -   [Project Objects](https://situ.entegysuite.com.au/Docs/Api/project-objects)
    -   [Project Management](https://situ.entegysuite.com.au/Docs/Api/project-get)
    -   [Project API Keys](https://situ.entegysuite.com.au/Docs/Api/projectapikey-get)
-   Submission Forms
    -   [Submission Form - Get](https://situ.entegysuite.com.au/Docs/Api/submission-form-get)
