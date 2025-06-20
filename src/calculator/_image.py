from pathlib import Path

import numpy as np


class Image:
    def __init__(self, data: np.ndarray):
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("Image data should be a 2D Numpy array.")
        self._data: np.ndarray = data

    @classmethod
    def from_array(cls, data: list):
        return cls(np.array(data))

    @classmethod
    def from_file(cls, file_path: str | Path):
        file_path = Path(file_path)
        import json

        return cls.from_array(json.loads(file_path.read_text()))
