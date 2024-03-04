from pydantic import BaseModel

from .content import NamedLink
from .profile import Profile


class ExhibitorLead(BaseModel):
    Profile: Profile
    scannedTime: str
    syncedTime: str


class ProfileLead(BaseModel):
    exhibitor: NamedLink
    scannedTime: str
    syncedTime: str
