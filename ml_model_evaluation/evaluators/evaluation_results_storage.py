from enum import Enum


class EvaluationResultsStorage(Enum):
    wandb = 1
    postgres = 2
    mongo = 3
