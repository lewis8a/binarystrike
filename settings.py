"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

Author: Kevin Márquez
marquezberriosk@gmail.com

Author: Lewis Ochoa
lewis8a@gmail.com

This file contains the constants definitions for setup an other things.
"""

import pathlib

import pygame

from gale import frames
from gale import input_handler

from src import loaders

input_handler.InputHandler.set_keyboard_action(input_handler.KEY_ESCAPE, "quit")
#input_handler.InputHandler.set_keyboard_action(input_handler.KEY_p, "pause")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_RETURN, "enter")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_KP_ENTER, "enter")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_RIGHT, "move_right")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_d, "move_right")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_LEFT, "move_left")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_a, "move_left")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_UP, "look_up")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_w, "look_up")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_DOWN, "look_down")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_s, "look_down")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_SPACE, "jump")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_f, "shoot")

# Size we want to emulate
VIRTUAL_WIDTH = 300
VIRTUAL_HEIGHT = 192

# Size of our actual window
WINDOW_WIDTH = VIRTUAL_WIDTH * 3
WINDOW_HEIGHT = VIRTUAL_HEIGHT * 2.5

PLAYER_SPEED = 80

GRAVITY = 200

NUM_LEVELS = 3

PROJECTILE_SPEED = 170

# Goal score
GOAL_SCORE = 35

BASE_DIR = pathlib.Path(__file__).parent

LevelLoader = loaders.TmxLevelLoader

TEXTURES = {
    "tile_1": pygame.image.load(BASE_DIR / "assets" / "graphics" / "tilesets" / "tileset_1.png"),
    "tile_2": pygame.image.load(BASE_DIR / "assets" / "graphics" / "tilesets" / "tileset_2.png"),
    "khan": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "khanlockwood" / "khan_1.png"),
    "bullet1": pygame.image.load(BASE_DIR / "assets" / "graphics" / "objects" / "Bullet1.png"),
    "bulletenemy": pygame.image.load(BASE_DIR / "assets" / "graphics" / "objects" / "BulletEnemy.png"),
    "Enemy2-walk": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "enemies" / "enemy2" / "Walk.png"),
    "Enemy2-shoot": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "enemies" / "enemy2" / "Shot_1.png"),
    "Enemy2-idle": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "enemies" / "enemy2" / "Idle.png"),
    #"Enemy2-dead": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "enemies" / "enemy2" / "Dead.png"),
}

FRAMES = {
    "tile_1": frames.generate_frames(TEXTURES["tile_1"], 16, 16),
    "tile_2": frames.generate_frames(TEXTURES["tile_2"], 16, 16),
    "khan": frames.generate_frames(TEXTURES["khan"], 20, 34),
    "Enemy2-walk": frames.generate_frames(TEXTURES["Enemy2-walk"], 20, 34),
    "Enemy2-shoot": frames.generate_frames(TEXTURES["Enemy2-shoot"], 20, 34),
    "Enemy2-idle": frames.generate_frames(TEXTURES["Enemy2-idle"], 20, 34),
    #"Enemy2-dead": frames.generate_frames(TEXTURES["Enemy2-dead"], 51, 51),
    "bullet1": frames.generate_frames(TEXTURES["bullet1"], 8, 8),
    "bulletenemy": frames.generate_frames(TEXTURES["bulletenemy"], 6, 4),
}

TILEMAPS = {i: BASE_DIR / "tilemaps" / f"level_{i}" for i in range(1, NUM_LEVELS + 1)}
pygame.mixer.init()

SOUNDS = {
    "menu": pygame.mixer.Sound(BASE_DIR / "assets" / "music" / "menu.ogg"),
    "level1": pygame.mixer.Sound(BASE_DIR / "assets" / "music" / "level1.ogg"),
    "level2": pygame.mixer.Sound(BASE_DIR / "assets" / "music" / "level2.ogg"),
    "level3": pygame.mixer.Sound(BASE_DIR / "assets" / "music" / "level3.ogg"),
    "gun": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "gun" / "gun5_shoot.wav"),
}

pygame.font.init()

FONTS = {
    "small": pygame.font.Font(BASE_DIR / "fonts" / "font.ttf", 8),
    "medium": pygame.font.Font(BASE_DIR / "fonts" / "font.ttf", 16),
}