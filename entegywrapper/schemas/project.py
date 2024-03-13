from enum import Enum
from typing import Optional

from pydantic import BaseModel


class ApiKeyPermission(Enum):
    VIEW_CONTENT = "ViewContent"
    EDIT_CONTENT = "EditContent"
    EDIT_PROFILES = "EditProfiles"
    VIEW_PROFILES = "ViewProfiles"
    ACHIEVEMENTS = "Achievements"
    SEND_NOTIFICATIONS = "SendNotifications"


class Region(Enum):
    AU = "61a948f2-d505-4b0b-81de-31af6925647e"
    US = "2b9bd3fc-405e-4df5-888d-f5323e2b5093"
    EU = "86f89b50-1bbb-4019-9ca2-b2d9f4167064"


class ProjectEventInfo(BaseModel):
    startDate: str
    endDate: str


class ProjectType(Enum):
    EVENT = "Event"
    ONGOING = "Ongoing"
    DEMO = "Demo"
    PORTAL = "Portal"
    DEMO_TEMPLATE = "DemoTemplate"


class ProjectStatus(Enum):
    DRAFT = "Draft"
    HAND_OVER = "HandOver"
    POPULATE_AND_TESTING = "PopulateAndTesting"
    PRODUCTION = "Production"
    FINISHED = "Finished"
    EXPIRED = "Expired"
    CANCELED = "Canceled"


class SoftwareElement(Enum):
    APP = "App"
    STORE_LISTING = "StoreListing"
    ENGAGE = "Engage"
    CAPTURE = "Capture"
    TRACK = "Track"
    INTERACT = "Interact"
    REGISTRATION = "Registration"
    MARKET = "Market"
    KIOSK = "Kiosk"
    KIOSK_ADDITIONAL = "KioskAdditional"
    EMAIL_DOMAIN = "EmailDomain"
    FLOOR_PLAN = "FloorPlan"


class Project(BaseModel):
    projectId: Optional[str] = None
    regionId: Optional[Region] = None
    regionName: Optional[str] = None
    externalReference: Optional[str] = None
    internalReference: Optional[str] = None
    projectName: Optional[str] = None
    projectShortName: Optional[str] = None
    iconUrl: Optional[str] = None
    eventCode: Optional[str] = None
    renewalDate: Optional[str] = None
    status: Optional[ProjectStatus] = None
    type: Optional[ProjectType] = None
    softwareElements: Optional[list[SoftwareElement]] = None
    eventInfo: Optional[ProjectEventInfo] = None


class ProjectApiKey(BaseModel):
    apiKeyId: str
    description: str
    expireDate: str
    allowedDomains: list[str]
    permissions: list[ApiKeyPermission]
