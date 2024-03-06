from .content import Category, Content, Document, Link, NamedLink


class ScheduleDay(Content):
    children: list[Content]


class Schedule(Content):
    days: list[ScheduleDay]


class SessionSegment(Content):
    links: list[Link]
    multiLinks: list[NamedLink]
    documents: list[Document]


class Session(Content):
    links: list[Link]
    multiLinks: list[NamedLink]
    documents: list[Document]
    selectedCategories: list[Category]
    segments: list[SessionSegment]


class SessionGroup(Content):
    documents: list[Document]
    links: list[Link]
    multiLinks: list[NamedLink]
    selectedCategories: list[Category]
