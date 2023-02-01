from enum import IntEnum
from typing import Literal, TypeAlias, TypedDict

from . import pageSettings, stringKeys


TemplateType: TypeAlias = Literal[
    "Schedule",
    "ScheduleDay",
    "Session",
    "SessionGroup",
    "SessionSegement",
    "Stream",
    "SessionType",
    "Speakers",
    "Speaker",
    "About",
    "Exhibitors",
    "Exhibitor",
    "GenericGroup",
    "GenericGroupPage",
    "FloorPlan",
    "Room",
    "Abstracts",
    "Abstract",
    "HTMLGroup",
    "HTMLPage",
    "Sponsors",
    "Sponsor",
]


class Icon(IntEnum):
    DOCUMENT: 0
    FACEBOOK: 1
    LINKEDIN: 2
    TWITTER: 3
    MAPPIN: 4
    GLOBE: 5
    ENEVELOPE: 6
    PHONE: 7
    SPEAKER: 8
    FILMREEL: 9
    DESKTOP: 10
    CHAT: 11
    MAP: 12
    ARTICLE: 13
    GALLERY: 14
    OUTBOX: 15
    LINKEDIN: 16
    PIN: 17
    BARGRAPH: 18
    PAPERCLIP: 19
    ACCESSPOINT: 20
    CALENDAR: 21
    CHECKMARK: 22
    PAPERPLANE: 23
    STAR: 24
    WARNINGTRIANGLE: 25
    SEARCH: 26
    FOLDER: 27
    INBOX: 28
    EDIT: 31
    PEOPLE: 32
    HOME: 37
    HOMESEARCH: 38
    DINER: 39
    OPENSIGN: 40
    INFOCIRCLE: 41
    HELPCIRCLE: 42
    FLAG: 43
    WINEGLASS: 44
    COCKTAIL: 45
    COFFEE: 46
    NEWS: 47
    CAR: 48
    OFFICEBUILDING: 49
    INFOSQUARE: 52
    GLOBESEARCH: 53
    ALARMCLOCK: 54
    GUITAR: 55
    ROADSIGNS: 56
    WIFITABLET: 57
    OPENBOOK: 58
    XBOX: 62
    GEAR: 64
    LOGOUT: 65
    INSTAGRAM: 68
    GOOGLEPLUS: 69
    HASHTAG: 70
    BACK: 71
    FORWARD: 72
    REFRESH: 73
    DOCUMENTSTAMP: 75
    ALARMBELL: 77
    ALARMBELLCOG: 78


class Document(TypedDict):
    name: str
    externalReference: str
    icon: Icon
    fileUrl: str


class ExternalContent(TypedDict):
    name: str
    externalReference: str
    icon: Icon
    fileUrl: str
    type: str


class Link(TypedDict):
    templateType: TemplateType
    moduleId: int
    externalReference: str


class NamedLink(Link, TypedDict, total=False):
    name: str


class CategoryRequired(TypedDict):
    moduleId: int
    externalReference: str


class CategoryNotRequired(TypedDict, total=False):
    name: str


class Category(CategoryRequired, CategoryNotRequired):
    pass


class Content(TypedDict):
    contentType: str
    templateType: TemplateType
    moduleId: int
    externalReference: str
    mainImage: str
    strings: dict[stringKeys.StringKey, str]
    pageSettings: dict[pageSettings.PageSetting, bool]
    sortOrder: int


class ContentPage(Content, TypedDict):
    documents: list[Document]
    links: list[Link]
    multiLinks: list[NamedLink]
    selectedCategories: list[Category]


class ContentChild(Content, TypedDict):
    documents: list[Document]
    links: list[Link]
    multiLinks: list[NamedLink]
    selectedCategories: list[Category]


class ContentChildCreateRequired(TypedDict):
    name: str


class ContentChildCreateNotRequired(TypedDict, total=False):
    externalReference: str
    mainImage: str
    strings: dict[stringKeys.StringKey, str]
    links: list[Link]
    sortOrder: int


class ContentChildCreate(ContentChildCreateRequired, ContentChildCreateNotRequired):
    pass


class ContentParent(Content, TypedDict):
    children: list[ContentChild]


ContentIdentifier: TypeAlias = Literal["moduleId", "externalReference"]
