from enum import Enum


class PageSetting(str, Enum):
    HIDDEN_IN_APP = "hiddenInApp"
    UNCLICKABLE = "unclickable"
    DISABLE_COMMENTS = "disableComments"
    DISABLE_RATING = "disableRating"
    REQUIRE_LOGIN = "requireLogin"
    REMINDER_ALERT = "reminderAlert"
    API_MANAGED = "apiManaged"
    SHOW_BY_PROFILE = "showByProfile"
