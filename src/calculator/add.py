import numpy as np

from ._image import Image

__all__ = ["add"]


def add(image1: Image, image2: Image) -> Image:
    """Add the two provided images element-wise.

    :param image1: The first image to be added.

    :param image2: The second image to be aded.

    :returns: A new Image object holding the sum of the provided images.

    Examples
    --------
    >>> from calculator import add, Image
    >>> image1 = Image.from_array([[1, 2], [3, 4]])
    >>> image2 = Image.from_array([[1, 1], [1, 1]])
    >>> image3 = add(image1, image2)
    >>> image3.data
    array([[2, 3],
           [4, 5]])
    """
    _check_images_compatibility(image1, image2)
    return Image.from_array(image1.data + image2.data)


def _check_images_compatibility(image1: Image, image2: Image):
    try:
        np.broadcast_shapes(image1.data.shape, image2.data.shape)
    except ValueError:
        raise ValueError(
            "Provided images have incompatile shapes.\n"
            f"Image 1 is {image1.data.shape}.\n"
            f"Image 2 is {image2.data.shape}."
        )
