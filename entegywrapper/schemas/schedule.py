from typing import TypedDict

from . import content


class ScheduleDay(content.Content, TypedDict):
    children: list[content.Content]


class Schedule(content.Content, TypedDict):
    days: list[ScheduleDay]


class SessionSegment(content.Content, TypedDict):
    links: list[content.Link]
    multiLinks: list[content.NamedLink]
    documents: list[content.Document]


class Session(content.Content, TypedDict):
    links: list[content.Link]
    multiLinks: list[content.NamedLink]
    documents: list[content.Document]
    selectedCategories: list[content.Category]
    segments: list[SessionSegment]


class SessionGroup(content.Content, TypedDict):
    documents: list[content.Document]
    links: list[content.Link]
    multiLinks: list[content.NamedLink]
    selectedCategories: list[content.Category]
