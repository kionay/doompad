from typing import Tuple

from PIL import Image, ImageGrab

ASCII_CHARS = ["*", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]

WIDTH = 400
HEIGHT = 120


def generate_screenshots():
    while True:
        screenshot = ImageGrab.grab()
        yield screenshot


def image_to_ascii(image: Image) -> str:
    image = image.resize((WIDTH, HEIGHT))
    image = image.convert("L")
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 25]
    return ascii_str


def generate_ascii_screengrab():
    for screenshot in generate_screenshots():
        screenshot_as_ascii = image_to_ascii(screenshot)
        ascii_screenshot_with_newlines = ""
        for index in range(0, len(screenshot_as_ascii), WIDTH):
            ascii_screenshot_with_newlines += (
                screenshot_as_ascii[index : index + WIDTH] + "\n"
            )
        yield ascii_screenshot_with_newlines
