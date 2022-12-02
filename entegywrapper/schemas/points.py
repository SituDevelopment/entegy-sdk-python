from typing import Literal, TypeAlias, TypedDict

from . import profile


PointType: TypeAlias = Literal[
    "Comment",
    "CommentWithImage",
    "Status",
    "StatusWithImage",
    "ViewComment",
    "ProfileLogin",
    "ProfileUpdated",
    "ProfileImageUpdated",
    "ViewPage",
    "ViewPageFirstTime",
    "ViewNotification",
    "MessageSent",
    "FeedbackSubmitted",
    "LeadCreated",
    "SessionTracked",
    "InteractiveSessionVote",
    "InteractiveSessionComment",
    "InteractiveSessionQuestion",
    "ManualPoints"
]


class Achievement(TypedDict):
    achievementId: int
    title: str
    message: str
    pointType: PointType
    pointOccurrancesRequired: int
    pointReward: int
    iconUrl: str


class AchievementUnlocked(Achievement):
    unlockedTime: str


class LeaderboardPosition(TypedDict):
    profile: profile.Profile
    position: int
    points: int
    unlockedAchievementsCount: int
