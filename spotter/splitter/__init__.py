from PIL import Image, ImageEnhance

from spotter import assets_path

offset = {
    "radiant": {
        "top": 7,
        "left": 165
    },
    "dire": {
        "top": 7,
        "left": 1140
    }
}
hero_width = 120
padding = 4


# Match hero avatar
async def extract_avatars(team, img):
    heroes = []
    j = 0
    # hero_height = img.height
    hero_height = 64
    if team == "dire":
        j = 5
    for i in range(0, 5):
        hero_box = (
            offset[team]["left"] + i * hero_width + i * padding,
            offset[team]["top"],
            offset[team]["left"] + i * hero_width + i * padding + hero_width,
            offset[team]["top"] + hero_height
        )
        hero = img.crop(hero_box).resize((262, 150)).crop((3, 3, 254, 144))
        img_enhancer = ImageEnhance.Brightness(hero)
        factor = 1
        enhanced_output = img_enhancer.enhance(factor)
        path = f'{assets_path}/tmp/{i + 1 + j}.png'
        enhanced_output.save(path)
        heroes.append(path)
    return heroes


# Probe and extract currently picked heroes
async def probe(source):
    img = Image.open(source)
    normalized = img.resize((1920, 1080))
    radiant_heroes = await extract_avatars("radiant", normalized)
    dire_heroes = await extract_avatars("dire", normalized)
    return radiant_heroes, dire_heroes
