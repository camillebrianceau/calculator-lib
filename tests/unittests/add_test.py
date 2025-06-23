import numpy as np
from numpy.testing import assert_array_equal


def test_image_addition(tmp_path):
    from calculator._image import Image
    from calculator.add import add

    (tmp_path / "image1.img").write_text("[[1, 2], [3, 4]]")
    (tmp_path / "image2.img").write_text("[[1, -1], [2, 0]]")

    img = add(
        Image.from_file(tmp_path / "image1.img"),
        Image.from_file(tmp_path / "image2.img"),
    )

    assert_array_equal(
        img._data,
        np.array([[2, 1], [5, 4]]),
    )
