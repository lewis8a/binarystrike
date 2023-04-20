import pathlib

import pygame

from gale import frames
from gale import input_handler

from src import loaders

input_handler.InputHandler.set_keyboard_action(input_handler.KEY_ESCAPE, "quit")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_p, "pause")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_RETURN, "enter")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_KP_ENTER, "enter")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_RIGHT, "move_right")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_d, "move_right")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_LEFT, "move_left")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_a, "move_left")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_SPACE, "jump")
input_handler.InputHandler.set_mouse_click_action(input_handler.MOUSE_BUTTON_1, "jump")

# Size we want to emulate
VIRTUAL_WIDTH = 400
VIRTUAL_HEIGHT = 192

# Size of our actual window
WINDOW_WIDTH = VIRTUAL_WIDTH * 2.4
WINDOW_HEIGHT = VIRTUAL_HEIGHT * 2.4

PLAYER_SPEED = 80

GRAVITY = 400

NUM_LEVELS = 1

# Goal score
GOAL_SCORE = 35

BASE_DIR = pathlib.Path(__file__).parent

LevelLoader = loaders.TmxLevelLoader

TEXTURES = {
    "tiles": pygame.image.load(BASE_DIR / "assets" / "graphics" / "tilesets" / "Tileset.png"),
    "khan": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "enemies" / "enemie_2.png"),
}

FRAMES = {
    "tiles": frames.generate_frames(TEXTURES["tiles"], 16, 16),
    "khan": frames.generate_frames(TEXTURES["khan"], 72, 72),
}

TILEMAPS = {i: BASE_DIR / "tilemaps" / f"level{i}" for i in range(1, NUM_LEVELS + 1)}

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