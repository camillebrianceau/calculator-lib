import numpy as np


class Image:
    def __init__(self, data: np.ndarray):
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("Image data should be a 2D Numpy array.")
        self._data: np.ndarray = data


