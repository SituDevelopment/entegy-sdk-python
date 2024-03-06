from pydantic import BaseModel

from .content import NamedLink
from .profile import Profile


class Attendee(BaseModel):
    profile: Profile
    checkInTime: str


class Attended(BaseModel):
    session: NamedLink
    checkInTime: str
