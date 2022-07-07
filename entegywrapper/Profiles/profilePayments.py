import requests, json


def addProfilePayment(self, profileId, paymentInfo):
    """
    Return all the profile links the profile ha

    Arguments:
        profileId -- User profile ID

        paymentInfo -- All payment information in JSON format

        e.g.

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

    Returns:
        Base response object
    """
    data = {
        "projectId": self.projectID,
        "apiKey": self.getKey(),
        "profileID": profileId,
    }
    data.update(paymentInfo)

    resp = requests.post(
        self.APIEndpoint + "/v2/ProfilePayment/Add/",
        headers=self.headers,
        data=json.dumps(data),
    )
    if resp == None:
        raise Exception("No reponse received from API")
    output = resp.json()
    return output
