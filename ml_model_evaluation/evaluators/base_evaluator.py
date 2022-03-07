from ..models.base_model import BaseModel
from ..datasets.base_dataset import BaseDataset
from .evaluation_results_storage import EvaluationResultsStorage
from typing import List, Dict


class BaseEvaluator:
    """ """

    def __init__(self) -> None:
        pass

    def evaluate(
        self, model: BaseModel, dataset: BaseDataset, metrics: List[str]
    ) -> Dict[str, float]:
        raise NotImplementedError

    def save_results(self, results_storage: EvaluationResultsStorage):
        raise NotImplementedError
