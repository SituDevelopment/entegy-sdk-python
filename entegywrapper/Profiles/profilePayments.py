from entegywrapper.schemas.profile import PaymentInfo


def add_profile_payment(
    self,
    payment_info: PaymentInfo,
    *,
    profile_id: str | None = None,
    external_reference: str | None = None,
    internal_reference: str | None = None,
    badge_reference: str | None = None
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

    self.post(self.api_endpoint + "/v2/ProfilePayment/Add/", data=data)
