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

# Input Handlers
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_ESCAPE, "quit")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_p, "pause")
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
pygame.init()
WINDOW_WIDTH = pygame.display.Info().current_w
WINDOW_HEIGHT = pygame.display.Info().current_h

# Basic game settings
PLAYER_SPEED = 80
GRAVITY = 400
NUM_LEVELS = 3
PROJECTILE_SPEED = 170
RANGE_VISION = 100
GOAL_SCORE = 35
TIME = 500

# Path of resources
BASE_DIR = pathlib.Path(__file__).parent

# Level Loader
LevelLoader = loaders.TmxLevelLoader

# Textures
TEXTURES = {
    "background_0": pygame.image.load(BASE_DIR / "assets" / "graphics" / "backgrounds" / "0.jpg"),
    "binary_strike": pygame.image.load(BASE_DIR / "assets" / "graphics" / "logo" / "BinaryStrike.png"),
    "tile_1": pygame.image.load(BASE_DIR / "assets" / "graphics" / "tilesets" / "tileset_1.png"),
    "tile_2": pygame.image.load(BASE_DIR / "assets" / "graphics" / "tilesets" / "tileset_2.png"),
    "tile_3": pygame.image.load(BASE_DIR / "assets" / "graphics" / "tilesets" / "tileset_3.png"),
    "khan": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "khanlockwood" / "khan_1.png"),
    "bullet_player": pygame.image.load(BASE_DIR / "assets" / "graphics" / "objects" / "BulletPlayer.png"),
    "bullet_enemy": pygame.image.load(BASE_DIR / "assets" / "graphics" / "objects" / "BulletEnemy.png"),
    "enemy2_walk": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "enemies" / "enemy2" / "Walk.png"),
    "enemy2_shoot": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "enemies" / "enemy2" / "Shot.png"),
    "enemy2_idle": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "enemies" / "enemy2" / "Idle.png"),
    "enemy2_dead": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "enemies" / "enemy2" / "Dead.png"),
    "play_btn_0": pygame.image.load(BASE_DIR / "assets" / "graphics" / "ui" / "play_btn_0.png"),
    "play_btn_1": pygame.image.load(BASE_DIR / "assets" / "graphics" / "ui" / "play_btn_1.png"),
    "settings_btn_0": pygame.image.load(BASE_DIR / "assets" / "graphics" / "ui" / "settings_btn_0.png"),
    "settings_btn_1": pygame.image.load(BASE_DIR / "assets" / "graphics" / "ui" / "settings_btn_1.png"),
    "info_btn_0": pygame.image.load(BASE_DIR / "assets" / "graphics" / "ui" / "info_btn_0.png"),
    "info_btn_1": pygame.image.load(BASE_DIR / "assets" / "graphics" / "ui" / "info_btn_1.png"),
    "bar": pygame.image.load(BASE_DIR / "assets" / "graphics" / "ui" / "bar.png"),
}

# Frames
FRAMES = {
    "tile_1": frames.generate_frames(TEXTURES["tile_1"], 16, 16),
    "tile_2": frames.generate_frames(TEXTURES["tile_2"], 16, 16),
    "tile_3": frames.generate_frames(TEXTURES["tile_3"], 16, 16),
    "khan": frames.generate_frames(TEXTURES["khan"], 20, 34),
    "bullet_player": frames.generate_frames(TEXTURES["bullet_player"], 8, 8),
    "bullet_enemy": frames.generate_frames(TEXTURES["bullet_enemy"], 5, 5),
    "enemy2_walk": frames.generate_frames(TEXTURES["enemy2_walk"], 20, 34),
    "enemy2_shoot": frames.generate_frames(TEXTURES["enemy2_shoot"], 20, 34),
    "enemy2_idle": frames.generate_frames(TEXTURES["enemy2_idle"], 20, 34),
    "enemy2_dead": frames.generate_frames(TEXTURES["enemy2_dead"], 51, 51),
}

# Tile maps of levels
TILEMAPS = {i: BASE_DIR / "tilemaps" / f"level_{i}" for i in range(1, NUM_LEVELS + 1)}
pygame.mixer.init()

# Music and sound effects
SOUNDS = {
    "menu": pygame.mixer.Sound(BASE_DIR / "assets" / "music" / "menu.ogg"),
    "menu-play": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "menu" / "menu_play.mp3"),
    "level1": pygame.mixer.Sound(BASE_DIR / "assets" / "music" / "level1.ogg"),
    "level2": pygame.mixer.Sound(BASE_DIR / "assets" / "music" / "level2.ogg"),
    "level3": pygame.mixer.Sound(BASE_DIR / "assets" / "music" / "level3.ogg"),
    "blood1": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "blood" / "blood_1.mp3"),
    "blood2": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "blood" / "blood_2.mp3"),
    "blood3": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "blood" / "blood_3.mp3"),
    "blood4": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "blood" / "blood_4.mp3"),
    "gun1": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "gun" / "gun1_shoot.wav"),
    "gun2": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "gun" / "gun2_shoot.wav"),
    "gun3": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "gun" / "gun3_shoot.wav"),
    "gun4": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "gun" / "gun4_shoot.wav"),
    "gun5": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "gun" / "gun5_shoot.wav"),
    "jump1": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "khanlockwood" / "jumping_1.wav"),
    "jump2": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "khanlockwood" / "jumping_2.wav"),
    "jump3": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "khanlockwood" / "jumping_3.wav"),
    "jump4": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "khanlockwood" / "jumping_4.wav"),
    "menu_change": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "menu" / "menu_change.mp3"),
    "menu_character": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "menu" / "menu_character.mp3"),
    "menu_enter": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "menu" / "menu_enter.mp3"),
    "menu_play": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "menu" / "menu_play.mp3"),
    "menu_return": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "menu" / "menu_return.mp3"),
    "menu_select": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "menu" / "menu_select.mp3"),
}

# Fonts
pygame.font.init()
FONTS = {
    "small": pygame.font.Font(BASE_DIR / "fonts" / "text.otf", 12),
    "medium": pygame.font.Font(BASE_DIR / "fonts" / "text.otf",24),
    "title_small": pygame.font.Font(BASE_DIR / "fonts" / "title.ttf",16),
    "title_small_medium": pygame.font.Font(BASE_DIR / "fonts" / "title.ttf",20),
    "title_medium": pygame.font.Font(BASE_DIR / "fonts" / "title.ttf",24),
    "title_large": pygame.font.Font(BASE_DIR / "fonts" / "title.ttf",32),
}