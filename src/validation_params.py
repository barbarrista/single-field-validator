from dataclasses import asdict, dataclass
from typing import Annotated, Any

from .validators import (
    MaxLengthValidator,
    MinLengthValidator,
    LtValidator,
    LeValidator,
    GtValidator,
    GeValidator,
    EqValidator,
    NeValidator,
    MustBeNoneValidator,
    MustBeNotNoneValidator,
)


@dataclass(frozen=True)
class ValidationParams:
    max_length: Annotated[int | None, MaxLengthValidator] = None
    min_length: Annotated[int | None, MinLengthValidator] = None

    lt: Annotated[int | None, LtValidator] = None
    le: Annotated[int | None, LeValidator] = None
    gt: Annotated[int | None, GtValidator] = None
    ge: Annotated[int | None, GeValidator] = None
    eq: Annotated[int | None, EqValidator] = None
    ne: Annotated[int | None, NeValidator] = None

    must_be_none: Annotated[bool | None, MustBeNoneValidator] = None
    must_be_not_none: Annotated[bool | None, MustBeNotNoneValidator] = None

    @property
    def params(self) -> dict[str, Any]:
        return {key: value for key, value in asdict(self).items() if value is not None}
