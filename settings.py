import pathlib

import pygame

from gale import frames
from gale import input_handler

input_handler.InputHandler.set_keyboard_action(input_handler.KEY_ESCAPE, 'quit')

# Size we want to emulate
VIRTUAL_WIDTH = 320
VIRTUAL_HEIGHT = 180

# Size of our actual window
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

BASE_DIR = pathlib.Path(__file__).parent

# Register your textures from the graphics folder, for instance:
# TEXTURES = {
#     'my_texture': pygame.image.load(BASE_DIR / "assets" / "graphics" / "my_texture.png")
# }
TEXTURES = {}

# Register your frames, for instance:
# FRAMES = {
#     'my_frames': frames.generate_frames(TEXTURES['my_texture'], 16, 16)
# }
FRAMES = {}

pygame.mixer.init()

# Register your sound from the sounds folder, for instance:
# SOUNDS = {
#     'my_sound': pygame.mixer.Sound(BASE_DIR / "assets"  / "sounds" / "my_sound.wav"),
# }
SOUNDS = {}

pygame.font.init()

# Register your fonts from the fonts folder, for instance:
# FONTS = {
#     'small': pygame.font.Font(BASE_DIR / "assets"  / "fonts" / "font.ttf", 8)
# }
FONTS = {}
