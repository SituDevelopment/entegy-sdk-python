class EntegyError(Exception):
    """Base class for all Entegy errors."""

    pass


class EntegyDuplicateExternalReferenceError(EntegyError):
    """Raised when the Entegy API returns a failed request response."""

    pass


class EntegyFailedRequestError(EntegyError):
    """Raised when the Entegy API returns a failed request response."""

    pass


class EntegyInvalidAPIKeyError(EntegyError):
    """Raised when the Entegy API returns an invalid API key response."""

    pass


class EntegyNoDataError(EntegyError):
    """Raised when the Entegy API responds with no data."""

    pass


class EntegyServerError(EntegyError):
    """Raised when the Entegy API returns a server error response."""

    pass
