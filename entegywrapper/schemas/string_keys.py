from typing import Literal, TypeAlias

ContactInformationKeys: TypeAlias = Literal[
    "phoneNumber",
    "emailAddress",
    "website",
    "address",
    "facebook",
    "twitterHandle",
    "linkedIn",
]


About: TypeAlias = ContactInformationKeys | Literal["subtitle"]


Speaker: TypeAlias = (
    ContactInformationKeys
    | Literal[
        "sortName",
        "companyAndPosition",
        "copy",
    ]
)


ScheduleDay: TypeAlias = Literal["date"]


SessionGroup: TypeAlias = Literal["startTime", "endTime"]


Session: TypeAlias = Literal["startTime", "endTime", "askAQuestionEnabled", "copy"]


SessionSegment: TypeAlias = Literal["startTime", "endTime", "copy"]


Exhibitor: TypeAlias = ContactInformationKeys | Literal["subtitle", "copy", "markerX", "markerY"]


GenericGroup: TypeAlias = Literal["cellStyle"]


GenericGroupItem: TypeAlias = ContactInformationKeys | Literal["subtitle", "keywords", "copy"]

StringKey: TypeAlias = (
    About
    | Speaker
    | ScheduleDay
    | SessionGroup
    | Session
    | SessionSegment
    | Exhibitor
    | GenericGroup
    | GenericGroupItem
)
