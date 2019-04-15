class GenericError(Exception):
    """Error Class defalut system."""

    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        """Construct method."""
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        """Convert Error to Dict python."""
        rv = dict(self.payload or ())
        rv['error'] = self.message
        return rv


class ErrorStartTornado(Exception):
    pass


class ParamInvalid(Exception):
    """Class ParamInvalid"""
    pass


class ObjectNotExists(Exception):

    """Object not exist in database."""
    pass


class PageNotFound(Exception):

    """Page Not found."""
    pass


class ObjectExists(Exception):

    """Object exist in database."""
    pass


class TypePaymentNotFound(Exception):
    """Type payment not exist."""
    pass


class CreditCartdInvalid(Exception):
    """Credit Card Invalid."""
    pass


class ExpirationDateExceeded(Exception):
    """Expiration Date Exceeded."""
    pass


class InstanceNotFound(Exception):
    """Instance not found"""
    pass


ERRORS_CHALLENGE = (ErrorStartTornado, ParamInvalid, ObjectExists, InstanceNotFound,
                    ObjectNotExists, PageNotFound, TypePaymentNotFound, CreditCartdInvalid, ExpirationDateExceeded)
