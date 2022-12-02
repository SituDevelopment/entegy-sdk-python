from entegywrapper.entegySchemas.profile import PaymentInfo


def add_profile_payment(
    self,
    profile_id: str,
    payment_info: PaymentInfo
):
    """
    Add the given payment info to the specified profile.

    Parameters
    ----------
        `profile_id` (`str`): the profileId of the profile
        `payment_info` (`PaymentInfo`): all payment information in JSON format
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "profileId": profile_id
    }
    data.update(payment_info)

    self.post(
        self.api_endpoint + "/v2/ProfilePayment/Add/",
        headers=self.headers,
        data=data
    )
