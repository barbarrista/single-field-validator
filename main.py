from typing import Any
from src.validator import ValidationParams, MainValidator
from src.errors import ValidationErrors


def validate(value: Any, params: ValidationParams) -> None | ValidationErrors:
    validator = MainValidator(validation_params=params)
    return validator.validate(value=value)


def main() -> None:
    values = ["Something", "Nani", "NANIIIIIIIIIIIIIIIIIII", "YAMEDECUDASAIII"]
    params = ValidationParams(min_length=10, max_length=15)
    for value in values:
        result = validate(value=value, params=params)
        if result is None:
            print(f'Value "{value}" is valid')
            continue

        print(f'"{value}": {result}')
        for error in result.errors:
            print(error.message)
        print()


if __name__ == "__main__":
    main()
