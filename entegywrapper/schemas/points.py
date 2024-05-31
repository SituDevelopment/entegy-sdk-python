from enum import Enum

from pydantic import BaseModel

from .profile import Profile


class PointType(str, Enum):
    COMMENT = "Comment"
    COMMENT_WITH_IMAGE = "CommentWithImage"
    STATUS = "Status"
    STATUS_WITH_IMAGE = "StatusWithImage"
    VIEW_COMMENT = "ViewComment"
    PROFILE_LOGIN = "ProfileLogin"
    PROFILE_UPDATED = "ProfileUpdated"
    PROFILE_IMAGE_UPDATED = "ProfileImageUpdated"
    VIEW_PAGE = "ViewPage"
    VIEW_PAGE_FIRST_TIME = "ViewPageFirstTime"
    VIEW_NOTIFICATION = "ViewNotification"
    MESSAGE_SENT = "MessageSent"
    FEEDBACK_SUBMITTED = "FeedbackSubmitted"
    LEAD_CREATED = "LeadCreated"
    SESSION_TRACKED = "SessionTracked"
    INTERACTIVE_SESSION_VOTE = "InteractiveSessionVote"
    INTERACTIVE_SESSION_COMMENT = "InteractiveSessionComment"
    INTERACTIVE_SESSION_QUESTION = "InteractiveSessionQuestion"
    MANUAL_POINTS = "ManualPoints"


class Achievement(BaseModel):
    achievementId: int
    title: str
    message: str
    pointType: PointType
    pointOccurrancesRequired: int
    pointReward: int
    iconUrl: str


class AchievementUnlocked(Achievement):
    unlockedTime: str


class LeaderboardPosition(BaseModel):
    profile: Profile
    position: int
    points: int
    unlockedAchievementsCount: int
