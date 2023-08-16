from typing import Any

from smartimputer.column_types.base_type import BaseType


def json_to_types(data: dict[str, Any]) -> dict[str, BaseType]:
    raise NotImplementedError
