from typing import TypedDict

from . import content


class ScheduleDay(TypedDict):
    children: list[content.Content]


class Schedule(TypedDict):
    days: list[ScheduleDay]


class SessionSegment(TypedDict):
    links: list[content.Link]
    multiLinks: list[content.NamedLink]
    documents: list[content.Document]


class Session(TypedDict):
    links: list[content.Link]
    multiLinks: list[content.NamedLink]
    documents: list[content.Document]
    selectedCategories: list[content.Category]
    segments: list[SessionSegment]


class SessionGroup(TypedDict):
    documents: list[content.Document]
    links: list[content.Link]
    multiLinks: list[content.NamedLink]
    selectedCategories: list[content.Category]
