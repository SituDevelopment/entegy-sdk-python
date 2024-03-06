from typing import Literal, TypeAlias

from pydantic import BaseModel

from .profile import Profile

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
    "ManualPoints",
]


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
