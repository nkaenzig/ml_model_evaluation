from .model_task import ModelTask


class BaseModel:
    """
    Super class of openspeech models.

    note:
        do not use this class directly, use one of the sub classes.
    """

    def __init__(self, model_name: str, model_task: ModelTask) -> None:
        self.model_name = model_name

    def predict():
        raise NotImplementedError

    def batch_predict():
        raise NotImplementedError
