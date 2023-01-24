# Entegy APIv2 Wrapper

<div align="center">
    <a href="https://www.python.org/">
        <img src="https://forthebadge.com/images/badges/made-with-python.svg">
    </a>
    <a href="https://github.com/psf/black">
        <img src="readmeimages/code-format-black.svg">
    </a>
    <a href="https://www.python.org/downloads/release/python-3100/">
        <img src="readmeimages/python-3.10.svg">
    </a>
</div>

## Installation and Usage

Install with:

```bash
pip install git+ssh://git@github.com/SituDevelopment/python3-entegy-API-wrapper.git
```

Import with:

```python
from entegywrapper import EntegyAPI
```

## Ported Modules

- API Objects
- Content
  - [Content Objects](https://situ.entegysuite.com.au/Docs/Api/content-objects)
  - [Content Management](https://situ.entegysuite.com.au/Docs/Api/content-get)
  - [Categories](https://situ.entegysuite.com.au/Docs/Api/category-available)
  - [Documents](https://situ.entegysuite.com.au/Docs/Api/document-addfile)
  - [MultiLinks](https://situ.entegysuite.com.au/Docs/Api/multilink-get)
- Attendance Tracking
  - [Attendance Tracking Objects](https://situ.entegysuite.com.au/Docs/Api/track-objects)
  - [Track Management](https://situ.entegysuite.com.au/Docs/Api/track-addcheckin)
- Notification
  - [Notification - Send Bulk](https://situ.entegysuite.com.au/Docs/Api/notifications-send-bulk)
- Plugins
  - [External Authentication](https://situ.entegysuite.com.au/Docs/Api/plugins-authenticate-external)
- Points & Achievement
  - [Points & Achievement Objects](https://situ.entegysuite.com.au/Docs/Api/point-constants)
  - [Point Management](https://situ.entegysuite.com.au/Docs/Api/point-award)
- Profile
  - [Profile Objects](https://situ.entegysuite.com.au/Docs/Api/profile-object)
  - [Profile Management](https://situ.entegysuite.com.au/Docs/Api/profile-get)
  - [Profile Types](https://situ.entegysuite.com.au/Docs/Api/profiletype-get)
  - [Profile Custom Fields](https://situ.entegysuite.com.au/Docs/Api/profilecustomfield-get)
  - [Profile Links](https://situ.entegysuite.com.au/Docs/Api/profilelink-selected)
  - [Profile Payments](https://situ.entegysuite.com.au/Docs/Api/profile-payment-add)

## Modules to Port

- Lead Capture
  - [Lead Capture Objects](https://situ.entegysuite.com.au/Docs/Api/lead-capture-objects)
  - [Lead Capture Management](https://situ.entegysuite.com.au/Docs/Api/capture-lead-add)
- Points & Achievement
  - [Achievement Management](https://situ.entegysuite.com.au/Docs/Api/achievement-all)
- Project
  - [Project Objects](https://situ.entegysuite.com.au/Docs/Api/project-objects)
  - [Project Management](https://situ.entegysuite.com.au/Docs/Api/project-get)
  - [Project API Keys](https://situ.entegysuite.com.au/Docs/Api/projectapikey-get)
- Submission Forms
  - [Submission Form - Get](https://situ.entegysuite.com.au/Docs/Api/submission-form-get)
