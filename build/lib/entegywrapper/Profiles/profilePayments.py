import json


def addProfilePayment(
    self,
    profileId: str,
    paymentInfo: dict[str, str | int]
):
    """
    Return all the profile links the profile ha

    Parameters
    ----------
        `profileId` (`str`): the profileId of the profile
        `paymentInfo` (`dict[str, str | int`): all payment information in JSON format

    The format of `paymentInfo` is as follows:
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
        `dict`: API response JSON
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "profileID": profileId,
    }

    data.update(paymentInfo)

    resp = self.post(
        self.APIEndpoint + "/v2/ProfilePayment/Add/",
        headers=self.headers,
        data=json.dumps(data),
    )

    if resp == None:
        raise Exception("No response received from Entegy API")

    if isinstance(resp, dict):
        return resp
    output = resp.json()
    return output
