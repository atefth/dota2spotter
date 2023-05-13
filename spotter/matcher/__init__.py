import numpy as np

from image_match.goldberg import ImageSignature

from spotter import files, avatars


def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx


def matches(avatar):
    gis = ImageSignature()
    a = gis.generate_signature(avatar)
    distances = []
    for file in files:
        b = gis.generate_signature(file)
        distances.append(gis.normalized_distance(a, b))
    return find_nearest(distances, value=0.4)


# Exactly match the scrapped hero avatar with the one from the captured screen
def detect(radiant, dire):
    print("Radiant")
    for hero in radiant:
        print(avatars[matches(hero)])

    print("Dire")
    for hero in dire:
        print(avatars[matches(hero)])
