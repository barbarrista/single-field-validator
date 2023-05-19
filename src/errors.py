from collections.abc import Sequence


class ValidationError(Exception):
    _message: str
    """Must be looks like "Value must be greatger then {}" """

    def __init__(self, required_value: str) -> None:
        self._required_value = required_value

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(message={self.message})"

    @property
    def message(self) -> str:
        return self._message.format(self._required_value)


class ValidationErrors(Exception):

    def __init__(self, errors: Sequence[ValidationError]) -> None:
        self.errors = errors

    def __str__(self) -> str:
        return f"ValidationErrors(errors={self.errors})"


class MaxLengthError(ValidationError):
    _message = "The length must be no more than {}"


class MinLengthError(ValidationError):
    _message = "The length must be at least {}"


class LtError(ValidationError):
    _message = "Value must be less than {}"


class LeError(ValidationError):
    _message = "Value must be less than or equal to {}"


class GtError(ValidationError):
    _message = "Value must be greater than {}"


class GeError(ValidationError):
    _message = "Value must be greater than or equal to {}"


class EqError(ValidationError):
    _message = "The value must be equal to {}"


class NeError(ValidationError):
    _message = "The value must not be equal {}"


class MustBeNoneError(ValidationError):
    _message = "Value must be None"


class MustBeNotNoneError(ValidationError):
    _message = "Value must be not None"
