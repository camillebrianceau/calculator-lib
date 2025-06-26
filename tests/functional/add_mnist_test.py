from pathlib import Path

import pytest
from numpy.testing import assert_array_equal


@pytest.fixture
def private_data_dir():
    return Path("/builds/functional_tests_data")


def test_add_mnist(private_data_dir):
    from calculator import Image, add

    image1 = Image.from_file(private_data_dir / "image1.img")
    image2 = Image.from_file(private_data_dir / "image2.img")
    expected = Image.from_file(private_data_dir / "expected_sum_image.img")

    image3 = add(image1, image2)

    assert_array_equal(image3.data, expected.data)
