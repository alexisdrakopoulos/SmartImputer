from typing import Protocol

from smartimputer.column_types.base_type import BaseType


class BaseModel(Protocol):
    def __init__(self, label_name: str, label_type: BaseType):
        pass

    def fit(self):
        pass

    def predict(self):
        pass

    def _validate_prediction(self):
        pass
