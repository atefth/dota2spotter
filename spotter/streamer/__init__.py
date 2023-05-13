import pyautogui
import random
import time

from spotter import assets_path


# Capture screen and stream
def capture():
    while True:
        random_time = random.randint(1, 5)
        time.sleep(random_time)
        my_screenshot = pyautogui.screenshot()
        file_name = 'input.png'
        my_screenshot.save(f'{assets_path}/live/{file_name}')
