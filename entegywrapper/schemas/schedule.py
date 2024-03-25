from .content import Content


class SessionSegment(Content):
    pass


class Session(Content):
    segments: list[SessionSegment] = []


class SessionGroup(Content):
    sessions: list[Session] = []


class ScheduleDay(Content):
    children: list[Session | SessionGroup]


class Schedule(Content):
    days: list[ScheduleDay]
