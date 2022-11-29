
from typing import Any


def award_points(
    self,
    point_event: str,
    points: int,
    *,
    profile_id: str = "",
    external_reference: str = None,
    badge_reference: str = None,
    internal_reference: str = None,
) -> dict[str, Any]:
    """
    Allows you to give points to a profile.

    Parameters
    ----------
        `point_event` (`str`): the types of points you're assigning
        `points` (`int`): the amount of points you're assigning
        `profile_id` (`str`): the profileId for the profile
        `external_reference` (`str`): the externalReference of the profile
        `badge_reference` (`str`): the badgeReference of the profile
        `internal_reference` (`str`): the internalReference of the profile

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "profileId": profile_id,
        "pointEvent": point_event,
        "points": points,
    }

    if external_reference is not None:
        data.update({"externalReference": profile_id})
    if badge_reference is not None:
        data.update({"badgeReference": profile_id})
    if internal_reference is not None:
        data.update({"internalReference": profile_id})

    return self.post(
        self.api_endpoint + "/v2/Point/Award",
        headers=self.headers,
        data=data
    )


def get_points(
    self,
    *,
    profile_id: str = "",
    external_reference: str = None,
    badge_reference: str = None,
    internal_reference: str = None
) -> dict[str, Any]:
    """
    Returns the amount of points a profile has.

    Parameters
    ----------
        `profile_id` (`str`, optional): the profileId for the profile; defaults to `""`
        `external_reference` (`str`, optional): the externalReference of the profile; defaults to `None`
        `badge_reference` (`str`, optional): the badgeReference of the profile; defaults to `None`
        `internal_reference` (`str`, optional): the internalReference of the profile; defaults to `None`

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "profileId": profile_id
    }

    if external_reference is not None:
        data.update({"externalReference": profile_id})
    if badge_reference is not None:
        data.update({"badgeReference": profile_id})
    if internal_reference is not None:
        data.update({"internalReference": profile_id})

    return self.post(
        self.api_endpoint + "/v2/Point/Earned",
        headers=self.headers,
        data=data
    )


def get_point_leaderboard(self) -> dict[str, Any]:
    """
    Allows you to see the leaderboard for the project. The response is sorted
    by the profiles response and includes their position with ties correctly
    handled.

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key()
    }

    return self.post(
        self.api_endpoint + "/v2/Point/Leaderboard",
        headers=self.headers,
        data=data
    )
