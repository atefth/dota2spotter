# Path to assets
import os

assets_path = 'spotter/assets'
avatars = os.listdir(assets_path+"/heroes")
files = [f'{assets_path}/heroes/{name}' for name in avatars]