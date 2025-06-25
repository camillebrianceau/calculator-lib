from ._image import Image
from ._utils import check_images_compatibility

__all__ = ["subtract"]


def subtract(image1: Image, image2: Image) -> Image:
    """Subtract image2 from image2 element-wise.

    :param image1: The image to be subtracted from.

    :param image2: The image to subtract.

    :returns: A new Image object holding the subtraction of the provided images.

    Examples
    --------
    >>> from calculator import add, Image
    >>> image1 = Image.from_array([[1, 2], [3, 4]])
    >>> image2 = Image.from_array([[1, 1], [1, 1]])
    >>> image3 = subtract(image1, image2)
    >>> image3.data
    array([[0, 1],
           [2, 3]])
    """
    check_images_compatibility(image1, image2)
    return Image.from_array(image1.data - image2.data)
