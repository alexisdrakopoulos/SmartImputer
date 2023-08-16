from typing import Any, Optional, Protocol


class BaseType(Protocol):
    """
    This defines the base type for column types.
    """

    name: str
    description: Optional[str]
    value: Any

    def validate(self) -> bool:
        raise NotImplementedError
