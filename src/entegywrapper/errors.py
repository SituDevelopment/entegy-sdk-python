class EntegyError(Exception):
    """Base class for all Entegy errors."""

    pass


class EntegyFailedRequestError(EntegyError):
    """Raised when the Entegy API returns a failed request response."""

    pass


class EntegyInvalidAPIKeyError(EntegyError):
    """Raised when the Entegy API returns an invalid API key response."""

    pass
