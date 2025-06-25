import numpy as np

from ._image import Image

__all__ = ["check_images_compatibility"]


def check_images_compatibility(image1: Image, image2: Image):
    try:
        np.broadcast_shapes(image1.data.shape, image2.data.shape)
    except ValueError:
        raise ValueError(
            "Provided images have incompatile shapes.\n"
            f"Image 1 is {image1.data.shape}.\n"
            f"Image 2 is {image2.data.shape}."
        )
