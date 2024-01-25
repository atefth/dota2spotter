import asyncio

from PIL import Image

from spotter import splitter, assets_path, streamer
from spotter import scrapper
from spotter import matcher

# Read image
src = f'{assets_path}/scenarios/two.jpeg'


# async def main():
def main():

    # TODO: Run this once
    # scrapper.create_data_set()

    # radiant, dire = await splitter.probe(src)
    radiant, dire = splitter.probe(src)
    # for hero in radiant:
    #     hero.show()
    #
    # for hero in dire:
    #     hero.show()


    matcher.detect(radiant, dire)
    # streamer.capture()

if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    main()
