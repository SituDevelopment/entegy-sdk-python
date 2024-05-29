from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel, field_validator

from .project import ProjectEventInfo, ProjectStatus, ProjectType, SoftwareElement


class ProfileExtendedPrivacy(Enum):
    PUBLIC = "Public"
    CONNECTIONS = "Connections"
    HIDDEN = "Hidden"


class Permissions(BaseModel):
    loggedInApp: Optional[bool] = None
    loggedInCapture: Optional[bool] = None
    showInList: Optional[bool] = None
    allowMessaging: Optional[bool] = None
    showEmail: Optional[ProfileExtendedPrivacy] = None
    showContactNumber: Optional[ProfileExtendedPrivacy] = None
    apiManaged: Optional[bool] = None
    printedBadge: Optional[bool] = None
    optedOutOfEmails: Optional[bool] = None
    acceptedTerms: Optional[bool] = None


class ProfileReference(BaseModel):
    profileId: Optional[str] = None
    externalReference: Optional[str] = None
    internalReference: Optional[str] = None
    badgeReference: Optional[str] = None
    secondaryId: Optional[str] = None


class Profile(BaseModel):
    type: str
    firstName: str
    lastName: str
    profileId: Optional[str] = None
    externalReference: Optional[str] = None
    internalReference: Optional[str] = None
    badgeReference: Optional[str] = None
    accessCode: Optional[str] = None  # ^[A-Za-z0-9]+(?:[._-][A-Za-z0-9]+)*$
    password: Optional[str] = None
    title: Optional[str] = None
    displayName: Optional[str] = None
    organisation: Optional[str] = None
    position: Optional[str] = None
    email: Optional[str] = None
    contactNumber: Optional[str] = None
    imageUrl: Optional[str] = None
    created: Optional[str] = None
    lastUpdated: Optional[str] = None
    enabled: Optional[bool] = None
    permissions: Optional[Permissions] = None
    customFields: Optional[dict[str, Any]] = None
    parentProfile: Optional[ProfileReference] = None


class ProfileType(BaseModel):
    name: str
    externalReference: str
    isOrganiser: Optional[bool] = None
    allowAppLogin: Optional[bool] = None
    price: Optional[int] = None
    moduleId: Optional[int] = None


class CustomProfileFieldType(Enum):
    MULTI_CHOICE = "MultiChoice"
    SHORT_TEXT = "ShortText"
    MEDIUM_TEXT = "MediumText"
    LONG_TEXT = "LongText"
    FACEBOOK = "Facebook"
    TWITTER = "Twitter"
    INSTAGRAM = "Instagram"
    WEBSITE = "Website"


class MultiChoiceOptions(BaseModel):
    optionId: int
    name: str
    externalMappings: Optional[str] = None


class CustomProfileField(BaseModel):
    key: str
    name: str
    required: bool
    userAccess: str
    profileVisibility: str
    type: CustomProfileFieldType
    sortOrder: Optional[int] = None
    externallyManaged: bool
    options: Optional[list[MultiChoiceOptions]] = None

    @field_validator("key")
    @classmethod
    def lowercase_key(cls, value: str) -> str:
        return value.lower()


class ProfileCreate(BaseModel):
    externalReference: str
    projectName: str
    projectShortName: str
    eventCode: str
    renewalDate: str
    status: ProjectStatus
    type: ProjectType
    softwareElements: list[SoftwareElement]
    eventInfo: ProjectEventInfo


class ProfileUpdate(BaseModel):
    type: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    externalReference: Optional[str] = None
    badgeReference: Optional[str] = None
    accessCode: Optional[str] = None  # ^[A-Za-z0-9]+(?:[._-][A-Za-z0-9]+)*$
    password: Optional[str] = None
    title: Optional[str] = None
    organisation: Optional[str] = None
    position: Optional[str] = None
    email: Optional[str] = None
    contactNumber: Optional[str] = None
    imageUrl: Optional[str] = None
    enabled: Optional[bool] = None
    permissions: Optional[Permissions] = None
    customFields: Optional[dict[str, Any]] = None


class ProfileIdentifier(Enum):
    PROFILE_ID = "profileId"
    EXTERNAL_REFERENCE = "externalReference"
    INTERNAL_REFERENCE = "internalReference"
    BADGE_REFERENCE = "badgeReference"


class PaymentStatus(Enum):
    PENDING = "Pending"
    CANCELLED = "Cancelled"
    PAID = "Paid"
    REFUNDED = "Refunded"


class PaymentMethod(Enum):
    NONE = "None"
    CREDIT_CARD = "CreditCard"
    DIRECT_DEPOSIT = "DirectDeposit"
    CASH = "Cash"
    CHEQUE = "Cheque"
    OTHER = "Other"


class PaymentInfo(BaseModel):
    profileId: str
    externalReference: str
    internalReference: str
    badgeReference: str
    currency: str
    amount: int
    description: Optional[str] = None
    amountTax: Optional[int] = None
    amountTaxRate: Optional[float] = None
    platformFee: Optional[int] = None
    platformFeeTax: Optional[int] = None
    platformFeeTaxRate: Optional[float] = None
    platformFeeInvoiceId: Optional[str] = None
    transactionId: Optional[str] = None
    gateway: Optional[str] = None
    gatewayAccountId: Optional[str] = None
    status: Optional[PaymentStatus] = None
    method: Optional[PaymentMethod] = None
