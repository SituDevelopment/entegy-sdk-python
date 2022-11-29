from typing import Any


def add_profile_payment(
    self,
    profile_id: str,
    payment_info: dict[str, str | int]
) -> dict[str, Any]:
    """
    Return all the profile links the profile ha

    Parameters
    ----------
        `profile_id` (`str`): the profileId of the profile
        `payment_info` (`dict[str, str | int`): all payment information in JSON format

    The format of `payment_info` is as follows:
    ```python
        {
            "amount": 1000,
            "amountTax": 100,
            "amountTaxRate": 0.1,
            "currency": "JPY",
            "platformFee": 30,
            "platformFeeTax": 3,
            "platformFeeTaxRate": 0.1,
            "platformFeeInvoiceDate": "2021-04-21 10:06:00",
            "gateway": "Stripe",
            "gatewayAccountId": "StripeAccount",
            "transactionId": "123456789",
            "method": "CreditCard",
            "status": "Paid"
        }
    ```

    Returns
    -------
        `dict[str, Any]`: API response JSON
    """
    data = {
        "projectId": self.project_id,
        "apiKey": self.get_key(),
        "profileID": profile_id,
    }

    data.update(payment_info)

    return self.post(
        self.api_endpoint + "/v2/ProfilePayment/Add/",
        headers=self.headers,
        data=data
    )
