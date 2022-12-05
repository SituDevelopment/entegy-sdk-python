from enum import Enum
from typing import Literal, TypeAlias, TypedDict


ApiKeyPermission: TypeAlias = Literal[
    "ViewContent",
    "EditContent",
    "EditProfiles",
    "ViewProfiles",
    "Achievements",
    "SendNotifications"
]


Region: TypeAlias = Literal[
    "61a948f2-d505-4b0b-81de-31af6925647e",
    "2b9bd3fc-405e-4df5-888d-f5323e2b5093",
    "86f89b50-1bbb-4019-9ca2-b2d9f4167064"
]


class ProjectEventInfo(TypedDict):
    startDate: str
    endDate: str


ProjectType: TypeAlias = Literal[
    "Event"
    "Ongoing"
    "Demo"
    "Portal",
    "DemoTemplate"
]


ProjectStatus: TypeAlias = Literal[
    "Draft",
    "HandOver",
    "PopulateAndTesting",
    "Production",
    "Finished",
    "Expired",
    "Canceled"
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
    "FloorPlan"
]


class Project(TypedDict, total=False):
    projectId: str
    regionId: Region
    regionName: str
    externalReference: str
    internalReference: str
    projectName: str
    projectShortName: str
    iconUrl: str
    eventCode: str
    renewalDate: str
    status: ProjectStatus
    type: ProjectType
    softwareElements: list[SoftwareElement]
    eventInfo: ProjectEventInfo


class ProjectApiKey(TypedDict):
    apiKeyId: str
    description: str
    expireDate: str
    allowedDomains: list[str]
    permissions: list[ApiKeyPermission]
