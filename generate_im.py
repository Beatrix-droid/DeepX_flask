import numpy as np
from PIL import Image

def save_from_arr(array, path):

    """ takes image array and checks if needs rescaling"""

    if not np.max(array) > 1:
        array = 255 * array
    array = array.astype("uint8")
    image = Image.fromarray(array)
    image.save(path)
