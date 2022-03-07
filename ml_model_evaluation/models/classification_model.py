from .model_task import ModelTask
from .base_model import BaseModel
from typing import Union
import numpy as np
from pathlib import Path


class ClassificationModel(BaseModel):
    def __init__(self, model_name: str, model_task: ModelTask) -> None:
        super().__init__(model_name, model_task)

    def predict(input: Union[np.array, Path]) -> np.array:
        raise NotImplementedError
