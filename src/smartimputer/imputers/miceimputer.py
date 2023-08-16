from smartimputer.dataset import SmartDataset
from smartimputer.models.base import BaseModel


class SimpleMiceImputer:
    def __init__(self, dataset: SmartDataset):
        self.dataset = dataset

    def impute(self):
        pass
