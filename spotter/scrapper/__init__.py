from io import BytesIO

import requests
from PIL import Image

from spotter import assets_path

# Language
language = 'english'
# Endpoints
endpoints = {
    "heroes": f'https://www.dota2.com/datafeed/herolist?language={language}',
    "hero": f'https://www.dota2.com/datafeed/herolist?language={language}&hero_id=',
    "avatar": 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/'
}


# Scrap the web for hero avatars
def create_data_set():
    heroes_response = requests.get(endpoints["heroes"])
    heroes = heroes_response.json()["result"]["data"]["heroes"]
    for hero in heroes:
        avatar_name = hero["name"].split('npc_dota_hero_')[1]
        avatar_url = f'{endpoints["avatar"]}{avatar_name}.png'
        image_stream = BytesIO(requests.get(avatar_url).content)
        avatar = Image.open(image_stream)
        path_to_assets = f'{assets_path}/heroes/{avatar_name}.png'
        avatar.save(path_to_assets)
