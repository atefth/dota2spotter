import numpy as np

from ..goldberg import ImageSignature
from PIL import Image, ImageEnhance
from spotter import files, avatars
import cv2 as cv2

from skimage.metrics import structural_similarity as ssim


def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx


def matches(avatar):
    """
    gis = ImageSignature()
    a = gis.generate_signature(avatar)
    distances = []
    for file in files:
        b = gis.generate_signature(file)
        distances.append(gis.normalized_distance(a, b))
    """
    ## Alternate
    # https://stackoverflow.com/questions/69338654/find-similar-image-if-resolution-was-changed
    distances = []
    ava = cv2.imread(avatar, cv2.IMREAD_GRAYSCALE)
    for file in files:
        test_ava = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
        test_ava = cv2.resize(test_ava, (ava.shape[1], ava.shape[0]), interpolation=cv2.INTER_NEAREST)
        distance = s1 = ssim(ava, test_ava)
        distances.append(distance)
    return find_nearest(distances, value=0.4)


# Exactly match the scrapped hero avatar with the one from the captured screen
def detect(radiant, dire):
    print("Radiant")
    radiants = []
    dires = []
    for hero in radiant:
        radiants.append(avatars[matches(hero)])
        # print(avatars[matches(hero)])

    print("Dire")
    for hero in dire:
        dires.append(avatars[matches(hero)])
        # print(avatars[matches(hero)])

    print("Rad:", radiants)
    print("Dir:", dires)
