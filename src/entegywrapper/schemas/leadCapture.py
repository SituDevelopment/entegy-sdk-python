from typing import TypedDict

from . import content, profile


class ExhibitorLead(TypedDict):
    Profile: profile.Profile
    scannedTime: str
    syncedTime: str


class ProfileLead(TypedDict):
    exhibitor: content.NamedLink
    scannedTime: str
    syncedTime: str
