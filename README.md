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

Install over HTTPS with:

```bash
pip install git+https://github.com/SituDevelopment/python3-entegy-API-wrapper.git
```

Install over SSH with:

```bash
pip install git+ssh://git@github.com/SituDevelopment/python3-entegy-API-wrapper.git
```

Import with:

```python
from entegywrapper import EntegyAPI
```

## Ported Modules

- Content
  - [Management](https://situ.entegysuite.com.au/Docs/Api/content-get)
  - [Categories](https://situ.entegysuite.com.au/Docs/Api/category-available)
  - [Documents](https://situ.entegysuite.com.au/Docs/Api/document-addfile)
  - [MultiLinks](https://situ.entegysuite.com.au/Docs/Api/multilink-get)
- Attendance Tracking
  - [Management](https://situ.entegysuite.com.au/Docs/Api/track-addcheckin)
- Notification
  - [Send Bulk](https://situ.entegysuite.com.au/Docs/Api/notifications-send-bulk)
- Plugins
  - [External Authentication](https://situ.entegysuite.com.au/Docs/Api/plugins-authenticate-external)
- Points & Achievement
  - [Point Management](https://situ.entegysuite.com.au/Docs/Api/point-award)
- Profiles
  - [Management](https://situ.entegysuite.com.au/Docs/Api/profile-get)
  - [Types](https://situ.entegysuite.com.au/Docs/Api/profiletype-get)
  - [Custom Fields](https://situ.entegysuite.com.au/Docs/Api/profilecustomfield-get)
  - [Links](https://situ.entegysuite.com.au/Docs/Api/profilelink-selected)
  - [Payments](https://situ.entegysuite.com.au/Docs/Api/profile-payment-add)
