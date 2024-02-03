from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from entegywrapper.errors import EntegyFailedRequestError
from entegywrapper.schemas.points import LeaderboardPosition, PointType

if TYPE_CHECKING:
    from entegywrapper import EntegyAPI


def award_points(
    self: EntegyAPI,
    point_type: PointType,
    points: int,
    *,
    profile_id: Optional[str] = None,
    external_reference: Optional[str] = None,
    internal_reference: Optional[str] = None,
    badge_reference: Optional[str] = None,
):
    """
    Awards the given number of points to the specified profile.

    Parameters
    ----------
        `point_type` (`PointType`): the type of points to assign

        `points` (`int`): the amount of points to assign

        `profile_id` (`str`, optional): the profileId for the profile; defaults to `None`

        `external_reference` (`str`, optional): the externalReference of the profile; defaults to `None`

        `internal_reference` (`str`, optional): the internalReference of the profile; defaults to `None`

        `badge_reference` (`str`, optional): the badgeReference of the profile; defaults to `None`

    Raises
    ------
        `ValueError`: if no identifier is specified
    """
    data = {"pointEvent": point_type, "points": points}

    if profile_id is not None:
        data["profileId"] = profile_id
    elif external_reference is not None:
        data["externalReference"] = profile_id
    elif internal_reference is not None:
        data["internalReference"] = profile_id
    elif badge_reference is not None:
        data["badgeReference"] = profile_id
    else:
        raise ValueError("Please specify an identifier")

    response = self.post(self.api_endpoint + "/v2/Point/Award", data=data)

    match response["response"]:
        case 200:
            return
        case 401:
            raise EntegyFailedRequestError("Missing profile reference")
        case 402:
            raise EntegyFailedRequestError("Invalid point event")
        case _:
            raise EntegyFailedRequestError(
                f"{response['response']}: {response.get('message', 'Unknown error')}"
            )


def get_points(
    self: EntegyAPI,
    *,
    profile_id: Optional[str] = None,
    external_reference: Optional[str] = None,
    internal_reference: Optional[str] = None,
    badge_reference: Optional[str] = None,
) -> int:
    """
    Returns the amount of points the specified profile has.

    Parameters
    ----------
        `profile_id` (`str`, optional): the profileId for the profile; defaults to `None`

        `external_reference` (`str`, optional): the externalReference of the profile; defaults to `None`

        `internal_reference` (`str`, optional): the internalReference of the profile; defaults to `None`

        `badge_reference` (`str`, optional): the badgeReference of the profile; defaults to `None`

    Raises
    ------
        `ValueError`: if no identifier is specified

    Returns
    -------
        `int`: the amount of points the specified profile has
    """
    data = {}

    if profile_id is not None:
        data["profileId"] = profile_id
    elif external_reference is not None:
        data["externalReference"] = profile_id
    elif internal_reference is not None:
        data["internalReference"] = profile_id
    elif badge_reference is not None:
        data["badgeReference"] = profile_id
    else:
        raise ValueError("Please specify an identifier")

    response = self.post(self.api_endpoint + "/v2/Point/Earned", data=data)

    match response["response"]:
        case 200:
            return response["points"]
        case 401:
            raise EntegyFailedRequestError("Missing profile reference")
        case 402:
            raise EntegyFailedRequestError("Invalid point event")
        case _:
            raise EntegyFailedRequestError(
                f"{response['response']}: {response.get('message', 'Unknown error')}"
            )


def get_point_leaderboard(self) -> list[LeaderboardPosition]:
    """
    Returns the leaderboard for the project. The response is sorted by the
    profiles response and includes their position with ties correctly handled.

    Returns
    -------
        `list[LeaderboardPosition]`: the leaderboard position for each profile
    """
    data = {}

    response = self.post(self.api_endpoint + "/v2/Point/Leaderboard", data=data)

    match response["response"]:
        case 200:
            return response["leaderboard"]
        case _:
            raise EntegyFailedRequestError(
                f"{response['response']}: {response.get('message', 'Unknown error')}"
            )
