from utils.exceptions import DefaultHTTPException


class InvalidEmailException(DefaultHTTPException):
    status_code = 400
    error = "INVALID_EMAIL"
    message = "Invalid email. (placeholder)"
