from enum import Enum, IntEnum
from typing import Any, Optional

from pydantic import BaseModel

from .page_settings import PageSetting


class TemplateType(Enum):
    @classmethod
    def _missing_(cls, value):
        """Enables case-insensitive lookup."""
        if value is None:
            raise ValueError("None is not a valid value for this Enum.")

        if not isinstance(value, str):
            raise TypeError(f"Expected string type for value, got {type(value).__name__} instead.")

        value = value.lower()
        for member in cls.__members__.values():
            if member.value.lower() == value:
                return member

    ABOUT = "About"
    ABSTRACT = "Abstract"
    ABSTRACTS = "Abstracts"
    EXHIBITOR = "Exhibitor"
    EXHIBITORS = "Exhibitors"
    FLOOR_PLAN = "FloorPlan"
    FLOOR_PLANS = "FloorPlans"  # Doesn't exist in API docs :(
    GENERIC_GROUP = "GenericGroup"
    GENERIC_GROUP_PAGE = "GenericGroupPage"
    HTML_GROUP = "HTMLGroup"
    HTML_PAGE = "HTMLPage"
    ROOM = "Room"
    SCHEDULE = "Schedule"
    SCHEDULE_DAY = "ScheduleDay"
    SESSION = "Session"
    SESSION_GROUP = "SessionGroup"
    SESSION_SEGMENT = "SessionSegment"  # Spelt SessionSegement in API docs :(
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
    moduleId: Optional[int]
    externalReference: str
    name: Optional[str] = None
    childCategories: list["Category"] = []


class Content(BaseModel):
    name: str
    templateType: TemplateType
    externalReference: str
    mainImage: str
    strings: dict[str, str]
    contentType: Optional[str] = None
    moduleId: Optional[int]  # Optional when creating, not optional when retrieving.
    pageSettings: Optional[dict[PageSetting, bool]] = None
    sortOrder: Optional[int] = None
    documents: Optional[list[Document]] = None
    links: Optional[list[Link]] = None
    multiLinks: Optional[list[NamedLink]] = None
    selectedCategories: Optional[list[Category]] = None
    children: Optional[list["Content"]] = None

    def get_updated_content(self, other: "Content") -> dict[str, Any]:
        """
        Get a dictionary of updated content when comparing another content object against self.
        The list of items that can be updated is guided by Entegy's API docs however a number of the
        optional attributes have been left in. Time will tell if this is a valid assumption.

        Return should really be an object. See:
        https://github.com/SituDevelopment/entegy-sdk-python/issues/184

        Parameters
        ----------
            `other` (`Content`): The content object against which to compare self.

        Returns
        -------
            `dict[str, Any]`: The results dict. Could really use an object here. To be fixed in
            https://github.com/SituDevelopment/entegy-sdk-python/issues/184
        """
        updated_content = {}
        if self.name != other.name:
            updated_content["name"] = other.name
        if self.mainImage != other.mainImage:
            updated_content["mainImage"] = other.mainImage
        if self.strings != other.strings:
            updated_content["strings"] = other.strings
        if self.pageSettings != other.pageSettings:
            updated_content["pageSettings"] = other.pageSettings
        if self.sortOrder != other.sortOrder:
            updated_content["sortOrder"] = other.sortOrder
        if self.documents != other.documents:
            updated_content["documents"] = other.documents
        if self.links != other.links:
            updated_content["links"] = other.links
        if self.multiLinks != other.multiLinks:
            updated_content["multiLinks"] = other.multiLinks
        if self.selectedCategories != other.selectedCategories:
            updated_content["selectedCategories"] = other.selectedCategories
        return updated_content


class ContentCreate(BaseModel):
    name: str
    templateType: TemplateType
    externalReference: str


class ContentChildCreate(BaseModel):
    name: str
    externalReference: Optional[str] = None
    mainImage: Optional[str] = None
    strings: Optional[dict[str, str]] = None
    links: Optional[list[Link]] = None
