# Path to assets
from os import walk

assets_path = 'spotter/assets'
avatars = next(walk(f'{assets_path}/heroes'), (None, None, []))[2]
files = list(map(lambda name: f'{assets_path}/heroes/{name}', avatars))
