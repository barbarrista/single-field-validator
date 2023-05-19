from abc import ABC
from typing import Any

from .errors import (
    ValidationError,
    MaxLengthError,
    MinLengthError,
    LtError,
    LeError,
    GtError,
    GeError,
    EqError,
    NeError,
    MustBeNoneError,
    MustBeNotNoneError,
)


class Validator(ABC):
    exception_class: type[ValidationError]

    def __init__(self, check_value: Any) -> None:
        self._checking_value = check_value

    def validate(self, value: Any) -> None | ValidationError:
        raise NotImplementedError

    def check_for_error(self, result: bool) -> None | ValidationError:
        if result is False:
            return self.exception_class(required_value=self._checking_value)


class MaxLengthValidator(Validator):
    exception_class = MaxLengthError

    def validate(self, value: Any) -> None | ValidationError:
        result = len(value) <= self._checking_value
        return self.check_for_error(result)


class MinLengthValidator(Validator):
    exception_class = MinLengthError

    def validate(self, value: Any) -> None | ValidationError:
        result = len(value) > self._checking_value
        return self.check_for_error(result)


class LtValidator(Validator):
    exception_class = LtError

    def validate(self, value: int) -> None | ValidationError:
        result = value < self._checking_value
        return self.check_for_error(result)


class LeValidator(Validator):
    exception_class = LeError

    def validate(self, value: int) -> None | ValidationError:
        result = value <= self._checking_value
        return self.check_for_error(result)


class GtValidator(Validator):
    exception_class = GtError

    def validate(self, value: int) -> None | ValidationError:
        result = value > self._checking_value
        return self.check_for_error(result)


class GeValidator(Validator):
    exception_class = GeError

    def validate(self, value: int) -> None | ValidationError:
        result = value >= self._checking_value
        return self.check_for_error(result)


class EqValidator(Validator):
    exception_class = EqError

    def validate(self, value: int) -> None | ValidationError:
        result = value == self._checking_value
        return self.check_for_error(result)


class NeValidator(Validator):
    exception_class = NeError

    def validate(self, value: int) -> None | ValidationError:
        result = value != self._checking_value
        return self.check_for_error(result)


class MustBeNoneValidator(Validator):
    exception_class = MustBeNoneError

    def validate(self, value: Any) -> None | ValidationError:
        result = value is self._checking_value
        return self.check_for_error(result)


class MustBeNotNoneValidator(Validator):
    exception_class = MustBeNotNoneError

    def validate(self, value: Any) -> None | ValidationError:
        result = value is not self._checking_value
        return self.check_for_error(result)
