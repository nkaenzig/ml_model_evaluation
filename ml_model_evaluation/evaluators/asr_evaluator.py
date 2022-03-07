from .base_evaluator import BaseEvaluator
from ..models.asr_model import ASRModel
from ..datasets.asr_dataset import ASRDataset
from typing import List, Dict


class ASREvaluator(BaseEvaluator):
    """ """

    def __init__(self) -> None:
        pass

    def evaluate(
        self, model: ASRModel, dataset: ASRDataset, metrics: List[str]
    ) -> Dict[str, float]:
        return super().evaluate(dataset, metrics)
