from typing import Literal, TypeAlias, TypedDict

from . import project

ProfileExtendedPrivacy: TypeAlias = Literal["Public", "Connections", "Hidden"]


class Permissions(TypedDict, total=False):
    loggedInApp: bool
    loggedInCapture: bool
    showInList: bool
    allowMessaging: bool
    showEmail: ProfileExtendedPrivacy
    showContactNumber: ProfileExtendedPrivacy
    apiManaged: bool
    printedBadge: bool
    optedOutOfEmails: bool
    acceptedTerms: bool


class ProfileReference(TypedDict, total=False):
    profileId: str
    externalReference: str
    internalReference: str
    badgeReference: str
    secondaryId: str


class ProfileRequired(TypedDict):
    type: str
    firstName: str
    lastName: str


class ProfileNotRequired(TypedDict, total=False):
    profileId: str
    externalReference: str
    internalReference: str
    badgeReference: str
    accessCode: str  # ^[A-Za-z0-9]+(?:[._-][A-Za-z0-9]+)*$
    password: str
    title: str
    displayName: str
    organization: str
    position: str
    email: str
    contactNumber: str
    imageUrl: str
    created: str
    lastUpdated: str
    enabled: bool
    permissions: Permissions
    customFields: dict[str, str]
    parentProfile: ProfileReference


class Profile(ProfileRequired, ProfileNotRequired):
    pass


class ProfileType(TypedDict):
    name: str
    isOrganiser: bool
    allowAppLogin: bool
    price: int
    moduleId: int


CustomProfileFieldType: TypeAlias = Literal[
    "MultiChoice",
    "ShortText",
    "MediumText",
    "Facebook",
    "Twitter",
    "Instagram",
    "Website",
]


class MultiChoiceOptions(TypedDict):
    optionId: int
    name: str
    externalMappings: str


class CustomProfileFieldRequired(TypedDict):
    key: str
    name: str
    required: bool
    userAccess: str
    profileVisibility: str
    type: CustomProfileFieldType
    sortOrder: int
    externallyManaged: bool


class CustomProfileFieldNotRequired(TypedDict, total=False):
    options: list[MultiChoiceOptions]


class CustomProfileField(CustomProfileFieldRequired, CustomProfileFieldNotRequired):
    pass


class ProfileCreate(TypedDict):
    externalReference: str
    projectName: str
    projectShortName: str
    eventCode: str
    renewalDate: str
    status: project.ProjectStatus
    type: project.ProjectType
    softwareElements: list[project.SoftwareElement]
    eventInfo: project.ProjectEventInfo


class ProfileUpdate(TypedDict, total=False):
    type: str
    firstName: str
    lastName: str
    externalReference: str
    badgeReference: str
    accessCode: str  # ^[A-Za-z0-9]+(?:[._-][A-Za-z0-9]+)*$
    password: str
    title: str
    organization: str
    position: str
    email: str
    contactNumber: str
    imageUrl: str
    enabled: bool
    permissions: Permissions
    customFields: dict[str, str]


ProfileIdentifier: TypeAlias = Literal[
    "profileId", "externalReference", "internalReference", "badgeReference"
]


PaymentStatus: TypeAlias = Literal["Pending", "Cancelled", "Paid", "Refunded"]


PaymentMethod: TypeAlias = Literal[
    "None", "CreditCard", "DirectDeposit", "Cash", "Cheque", "Other"
]


class PaymentInfoRequired(TypedDict):
    profileId: str
    externalReference: str
    internalReference: str
    badgeReference: str
    currency: str
    amount: int


class PaymentInfoNotRequired(TypedDict, total=False):
    description: str
    amountTax: int
    amountTaxRate: float
    platformFee: int
    platformFeeTax: int
    platformFeeTaxRate: float
    platformFeeInvoiceId: str
    transactionId: str
    gateway: str
    gatewayAccountId: str
    status: PaymentStatus
    method: PaymentMethod


class PaymentInfo(PaymentInfoRequired, PaymentInfoNotRequired):
    pass
