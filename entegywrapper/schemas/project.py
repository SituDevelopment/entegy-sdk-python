from typing import Literal, Optional, TypeAlias

from pydantic import BaseModel

ApiKeyPermission: TypeAlias = Literal[
    "ViewContent",
    "EditContent",
    "EditProfiles",
    "ViewProfiles",
    "Achievements",
    "SendNotifications",
]


Region: TypeAlias = Literal[
    "61a948f2-d505-4b0b-81de-31af6925647e",
    "2b9bd3fc-405e-4df5-888d-f5323e2b5093",
    "86f89b50-1bbb-4019-9ca2-b2d9f4167064",
]


class ProjectEventInfo(BaseModel):
    startDate: str
    endDate: str


ProjectType: TypeAlias = Literal["Event" "Ongoing" "Demo" "Portal", "DemoTemplate"]


ProjectStatus: TypeAlias = Literal[
    "Draft",
    "HandOver",
    "PopulateAndTesting",
    "Production",
    "Finished",
    "Expired",
    "Canceled",
]


SoftwareElement: TypeAlias = Literal[
    "App",
    "StoreListing",
    "Engage",
    "Capture",
    "Track",
    "Interact",
    "Registration",
    "Market",
    "Kiosk",
    "KioskAdditional",
    "EmailDomain",
    "FloorPlan",
]


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
