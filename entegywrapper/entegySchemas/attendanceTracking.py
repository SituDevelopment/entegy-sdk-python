from typing import TypedDict

from . import content, profile


class Attendee(TypedDict):
    profile: profile.Profile
    checkInTime: str


class Attended(TypedDict):
    session: content.NamedLink
    checkInTime: str
