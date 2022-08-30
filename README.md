<div align="center">
<a href="https://www.python.org/"><img src="https://forthebadge.com/images/badges/made-with-python.svg"></a>
<a href="https://github.com/psf/black"><img src="readmeimages/code-format-black.svg"></a>
<a href="https://www.python.org/downloads/release/python-3100/"><img src="readmeimages/python-3.10.svg"></a>
</div>

# Python Wrapper For Entegy APIv2

[Entegy API Documentation](https://situ.entegysuite.com.au/Docs/Api/)

Install with

```bash
pip install git+https://github.com/SituDevelopment/python3-entegy-API-wrapper.git
```

Import via

```python
from entegyWrapper import EntegyAPI
```

### Currently Ported Modules

- Profiles
    - [Management](https://situ.entegysuite.com.au/Docs/Api/profile-get)
    - [Types](https://situ.entegysuite.com.au/Docs/Api/profiletype-get)
    - [Custom Fields](https://situ.entegysuite.com.au/Docs/Api/profilecustomfield-get)
    - [Links](https://situ.entegysuite.com.au/Docs/Api/profilelink-selected)
    - [Payments](https://situ.entegysuite.com.au/Docs/Api/profile-payment-add)
- Content
    - [Management](https://situ.entegysuite.com.au/Docs/Api/content-get)
    - [Categories](https://situ.entegysuite.com.au/Docs/Api/category-available)
    - [Documents](https://situ.entegysuite.com.au/Docs/Api/document-addfile)
    - [MultiLinks](https://situ.entegysuite.com.au/Docs/Api/multilink-get)
- Points & Achievement
    - [Point Management](https://situ.entegysuite.com.au/Docs/Api/point-award)
- External Authentication
    - [External Authentication](https://situ.entegysuite.com.au/Docs/Api/plugins-authenticate-external)
- Notification
    - [Send Bulk](https://situ.entegysuite.com.au/Docs/Api/notifications-send-bulk)