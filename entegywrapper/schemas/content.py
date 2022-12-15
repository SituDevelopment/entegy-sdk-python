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


class Document(TypedDict):
    name: str
    externalReference: str
    icon: int
    fileUrl: str


class ExternalContent(TypedDict):
    name: str
    externalReference: str
    icon: int
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
