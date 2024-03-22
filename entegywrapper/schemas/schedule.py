from .content import Category, Content, Document, Link, NamedLink


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
    links: list[Link]
    multiLinks: list[NamedLink]
    sessions: list[Session]


class ScheduleDay(Content):
    children: list[Session | SessionGroup]


class Schedule(Content):
    days: list[ScheduleDay]
