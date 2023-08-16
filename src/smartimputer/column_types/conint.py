from typing import Optional

from pydantic import BaseModel, root_validator, validator


class ConstrainedInt(BaseModel):
    """
    Constrained integer class.

    Examples of it being used:
    >>> ConstrainedInt(value=1, sparse=False, min_value=0, max_value=10, multiple_of=2)
    >>> ConstrainedInt(value=1, sparse=False, constrained_set={1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
    >>> ConstrainedInt(value=1, sparse=False, min_value=0, max_value=10, multiple_of=2, constrained_set={1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
    """

    name = "ConstrainedInt"
    description = "A constrained integer"

    sparse: bool
    """Whether the value is sparse"""
    min_value: Optional[int] = None
    """inclusive minimum value"""
    max_value: Optional[int] = None
    """inclusive maximum value"""
    multiple_of: Optional[int] = None
    """multiple of this value"""
    constrained_set: Optional[set[int]] = None

    @validator("value", pre=True, always=True)
    def validate_value(cls, v):
        if not isinstance(v, int):
            raise ValueError(f"value must be an integer. Got {type(v)} instead.")
        return v

    @validator("sparse", pre=True, always=True)
    def validate_sparse(cls, v):
        if not isinstance(v, bool):
            raise ValueError(f"sparse must be a boolean. Got {type(v)} instead.")
        return v

    @root_validator(pre=True)
    def validate_constraints(cls, values):
        min_value = values.get("min_value")
        max_value = values.get("max_value")
        multiple_of = values.get("multiple_of")
        constrained_set = values.get("constrained_set")

        if constrained_set is not None:
            if any([min_value, max_value, multiple_of]):
                raise ValueError(
                    "constrained_set can only be used if min_value, max_value, and multiple_of are not set."
                )

    def validate(self, value):
        if not isinstance(value, int):
            raise ValueError(
                f"value {value} is not of type int. Got {type(value)} instead."
            )

        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"value {value} is less than min_value {self.min_value}")

        if self.max_value is not None and value > self.max_value:
            raise ValueError(
                f"value {value} is greater than max_value {self.max_value}"
            )

        if self.multiple_of is not None and value % self.multiple_of != 0:
            raise ValueError(f"value {value} is not a multiple of {self.multiple_of}")

        if self.constrained_set is not None and value not in self.constrained_set:
            raise ValueError(
                f"value {value} is not in constrained_set {self.constrained_set}"
            )
