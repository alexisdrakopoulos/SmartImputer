import pandas as pd

from .column_types.base_type import BaseType


class SmartDataset:
    def __init__(self, data: pd.DataFrame, column_types: dict[str, BaseType]):
        self.data = data
        self.column_types = column_types
        self._validate_data_on_load()

    def _validate_new_row(self, row: pd.Series):
        """
        Validate a new row.
        """
        for column_name in row:
            self._validate_column_value(column_name, row[column_name])

    def _validate_data_on_load(self):
        """
        Validate the data on load.
        """
        for column_name in self.data:
            self._validate_column(column_name)

    def _validate_column(self, column_name: str):
        """
        Validate an entire column
        """
        column_type = self.column_types[column_name]
        column_data = self.data[column_name]
        column_data.apply(column_type.validate)

    def _validate_column_value(self, column_name: str, value):
        """
        Validate a single value in a column.
        """
        column_type = self.column_types[column_name]
        column_type.validate(value)
