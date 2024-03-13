from enum import Enum, IntEnum
from typing import Optional

from pydantic import BaseModel

from .page_settings import PageSetting


class TemplateType(Enum):
    @classmethod
    def _missing_(cls, value):
        """Enables case-insensitive lookup."""
        value = value.lower()
        for member in cls.__members__.values():
            if member.lower() == value:
                return member

    ABOUT = "About"
    ABSTRACT = "Abstract"
    ABSTRACTS = "Abstracts"
    EXHIBITOR = "Exhibitor"
    EXHIBITORS = "Exhibitors"
    FLOOR_PLAN = "FloorPlan"
    GENERIC_GROUP = "GenericGroup"
    GENERIC_GROUP_PAGE = "GenericGroupPage"
    HTML_GROUP = "HTMLGroup"
    HTML_PAGE = "HTMLPage"
    ROOM = "Room"
    SCHEDULE = "Schedule"
    SCHEDULE_DAY = "ScheduleDay"
    SESSION = "Session"
    SESSION_GROUP = "SessionGroup"
    SESSION_SEGEMENT = "SessionSegement"
    SESSION_TYPE = "SessionType"
    SPEAKER = "Speaker"
    SPEAKERS = "Speakers"
    SPONSOR = "Sponsor"
    SPONSORS = "Sponsors"
    STREAM = "Stream"


class Icon(IntEnum):
    """
    All icons can be found here: https://situ.entegy.com.au/Docs/Api/document-icons.
    """

    FACEBOOK = 1
    LINKEDIN = 2
    TWITTER = 3
    MAPPIN = 4
    GLOBE = 5
    ENEVELOPE = 6
    PHONE = 7
    SPEAKER = 8
    FILMREEL = 9
    DESKTOP = 10
    CHAT = 11
    MAP = 12
    ARTICLE = 13
    GALLERY = 14
    OUTBOX = 15
    LINK = 16
    PIN = 17
    BARGRAPH = 18
    PAPERCLIP = 19
    ACCESSPOINT = 20
    CALENDAR = 21
    CHECKMARK = 22
    PAPERPLANE = 23
    STAR = 24
    WARNINGTRIANGLE = 25
    SEARCH = 26
    FOLDER = 27
    INBOX = 28
    EDIT = 31
    PEOPLE = 32
    DOCUMENT = 35
    HOME = 37
    HOMESEARCH = 38
    DINER = 39
    OPENSIGN = 40
    INFOCIRCLE = 41
    HELPCIRCLE = 42
    FLAG = 43
    WINEGLASS = 44
    COCKTAIL = 45
    COFFEE = 46
    NEWS = 47
    CAR = 48
    OFFICEBUILDING = 49
    INFOSQUARE = 52
    GLOBESEARCH = 53
    ALARMCLOCK = 54
    GUITAR = 55
    ROADSIGNS = 56
    WIFITABLET = 57
    OPENBOOK = 58
    XBOX = 62
    GEAR = 64
    LOGOUT = 65
    INSTAGRAM = 68
    GOOGLEPLUS = 69
    HASHTAG = 70
    BACK = 71
    FORWARD = 72
    REFRESH = 73
    DOCUMENTSTAMP = 75
    ALARMBELL = 77
    ALARMBELLCOG = 78


class Document(BaseModel):
    name: str
    externalReference: str
    icon: Icon
    fileUrl: str


class ExternalContent(BaseModel):
    name: str
    externalReference: str
    icon: Icon
    fileUrl: str
    type: str


class Link(BaseModel):
    templateType: TemplateType
    moduleId: int
    externalReference: str


class NamedLink(Link):
    name: str


class Category(BaseModel):
    moduleId: int
    externalReference: str
    name: Optional[str] = None
    childCategories: list["Category"] = []


class Content(BaseModel):
    contentType: str
    templateType: TemplateType
    moduleId: int
    externalReference: str
    mainImage: str
    strings: dict[str, str]
    pageSettings: Optional[dict[PageSetting, bool]] = None
    sortOrder: Optional[int] = None
    documents: Optional[list[Document]] = None
    links: Optional[list[Link]] = None
    multiLinks: Optional[list[NamedLink]] = None
    selectedCategories: Optional[list[Category]] = None
    children: Optional[list["Content"]] = None


class ContentChildCreate(BaseModel):
    name: str
    externalReference: Optional[str] = None
    mainImage: Optional[str] = None
    strings: Optional[dict[str, str]] = None
    links: Optional[list[Link]] = None
    sortOrder: Optional[int] = None
