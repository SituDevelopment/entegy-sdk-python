from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from entegywrapper.errors import EntegyFailedRequestError
from entegywrapper.schemas.profile import PaymentInfo

if TYPE_CHECKING:
    from entegywrapper import EntegyAPI


def add_profile_payment(
    self: EntegyAPI,
    payment_info: PaymentInfo,
    *,
    profile_id: Optional[str] = None,
    external_reference: Optional[str] = None,
    internal_reference: Optional[str] = None,
    badge_reference: Optional[str] = None,
):
    """
    Adds the given payment info to the specified profile.

    Parameters
    ----------
        `payment_info` (`PaymentInfo`): the payment information to add

        `profile_id` (`str`, optional): the profileId of the profile; defaults to `None`

        `external_reference` (`str`, optional): the externalReference of the profile; defaults to `None`

        `internal_reference` (`str`, optional): the internalReference of the profile; defaults to `None`

        `badge_reference` (`str`, optional): the badgeReference of the profile; defaults to `None`

    Raises
    ------
        `ValueError`: if no identifier is specified

        `EntegyFailedRequestError`: if the API request fails
    """
    data = {"profileId": profile_id}
    data.update(payment_info)

    if profile_id is not None:
        data["profileId"] = profile_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    elif internal_reference is not None:
        data["internalReference"] = internal_reference
    elif badge_reference is not None:
        data["badgeReference"] = badge_reference
    else:
        raise ValueError("Please specify an identifier")

    response = self.post(self.api_endpoint + "/v2/ProfilePayment/Add/", data=data)

    match response["response"]:
        case 200:
            return
        case 400:
            raise EntegyFailedRequestError("Invalid amount")
        case 400:
            raise EntegyFailedRequestError("Invalid currency")
        case 401:
            raise EntegyFailedRequestError("Profile not found")
        case 402:
            raise EntegyFailedRequestError("Duplicate transaction")
        case _:
            raise EntegyFailedRequestError(
                f"{response['response']}: {response.get('message', 'Unknown error')}"
            )
