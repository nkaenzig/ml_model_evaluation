import numpy as np


class BaseMetric:
    """ """

    def __init__(self) -> None:
        pass

    def compute(predictions: np.array, gnd_truth: np.array):
        raise NotImplementedError
