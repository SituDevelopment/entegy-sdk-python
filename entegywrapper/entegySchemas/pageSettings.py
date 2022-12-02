from typing import Literal, TypeAlias


PageSetting: TypeAlias = Literal[
    "hiddenInApp",
    "unclickable",
    "disableComments",
    "disableRating",
    "requireLogin",
    "reminderAlert",
    "apiManaged",
    "showByProfile"
]
