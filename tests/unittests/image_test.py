import numpy as np
from calculator._image import Image


def test_image_instantiation():
    assert isinstance(Image(np.array([[1, 2], [3, 4]])), Image)


def test_image_data_set_correctly():
    from numpy.testing import assert_array_equal

    raw_data = np.array([[1, 2], [3, 4]])
    assert_array_equal(
        Image(raw_data)._data,
        raw_data,
    )


def test_bad_type_in_image_instantiation():
    import pytest

    with pytest.raises(
        TypeError,
        match="Image data should be a 2D Numpy array.",
    ):
        Image(10)
