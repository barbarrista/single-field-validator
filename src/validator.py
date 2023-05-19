from typing import Any, get_type_hints, get_args

from .validators import Validator
from .validation_params import ValidationParams
from .errors import ValidationErrors


class MainValidator:
    def __init__(self, validation_params: ValidationParams) -> None:
        self._validation_params = validation_params
        self.validators: list[Validator] = []
        self._init_validators()

    def _init_validators(self) -> None:
        typehints = get_type_hints(
            type(self._validation_params),
            include_extras=True,
        )

        for param, check_value in self._validation_params.params.items():
            raw_validator_type = typehints[param]
            args = get_args(raw_validator_type)
            validator_class: type[Validator] = args[1]
            self.validators.append(validator_class(check_value=check_value))

    def validate(self, value: Any) -> None | ValidationErrors:
        result = [
            validation_result
            for validator in self.validators
            if (validation_result := validator.validate(value=value)) is not None
        ]
        if result:
            return ValidationErrors(errors=result)
        return None
