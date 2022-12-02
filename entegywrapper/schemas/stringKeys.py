from enum import Enum


class StringKey:
    pass


class ContactInformationKeys(StringKey, Enum):
    "phoneNumber"
    "emailAddress"
    "website"
    "address"
    "facebook"
    "twitterHandle"
    "linkedIn"


class About(ContactInformationKeys, Enum):
    "subtitle"


class Speaker(ContactInformationKeys, Enum):
    "sortName"
    "companyAndPosition"
    "copy"


class ScheduleDay(StringKey, Enum):
    "date"


class SessionGroup(StringKey, Enum):
    "startTime"
    "endTime"


class Session(StringKey, Enum):
    "startTime"
    "endTime"
    "askAQuestionEnabled"
    "copy"


class SessionSegment(StringKey, Enum):
    "startTime"
    "endTime"
    "copy"


class Exhibitor(ContactInformationKeys, Enum):
    "subtitle"
    "copy"
    "markerX"
    "markerY"


class GenericGroup(StringKey, Enum):
    "cellStyle"


class GenericGroupItem(ContactInformationKeys, Enum):
    "subtitle"
    "keywords"
    "copy"
