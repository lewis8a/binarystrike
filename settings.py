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

WINDOW_WIDTH = VIRTUAL_WIDTH * 3 # pygame.display.Info().current_w
WINDOW_HEIGHT = VIRTUAL_HEIGHT * 2.5 #pygame.display.Info().current_h

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
    "pause": pygame.mixer.Sound(BASE_DIR / "assets" / "music" / "pause.ogg"),
    "credits": pygame.mixer.Sound(BASE_DIR / "assets" / "music" / "credits.ogg"),
    "level1": pygame.mixer.Sound(BASE_DIR / "assets" / "music" / "level1.ogg"),
    "level2": pygame.mixer.Sound(BASE_DIR / "assets" / "music" / "level2.ogg"),
    "level3": pygame.mixer.Sound(BASE_DIR / "assets" / "music" / "level3.ogg"),
    "level_failed": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "level" / "level_failed.mp3"),
    "level_time": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "level" / "level_time.mp3"),
    "level_win": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "level" / "level_win.mp3"),
    "blood1": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "blood" / "blood_1.mp3"),
    "blood2": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "blood" / "blood_2.mp3"),
    "blood3": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "blood" / "blood_3.mp3"),
    "blood4": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "blood" / "blood_4.mp3"),
    "gun1": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "gun" / "gun1_shoot.wav"),
    "gun2": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "gun" / "gun2_shoot.wav"),
    "gun3": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "gun" / "gun3_shoot.wav"),
    "gun4": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "gun" / "gun4_shoot.wav"),
    "gun5": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "gun" / "gun5_shoot.wav"),
    "death1": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "khanlockwood" / "death_1.wav"),
    "death2": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "khanlockwood" / "death_2.wav"),
    "death3": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "khanlockwood" / "death_3.wav"),
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
    "xs": pygame.font.Font(BASE_DIR / "fonts" / "info.ttf", 10),
    "small": pygame.font.Font(BASE_DIR / "fonts" / "info.ttf", 16),
    "small_medium": pygame.font.Font(BASE_DIR / "fonts" / "info.ttf",20),
    "medium": pygame.font.Font(BASE_DIR / "fonts" / "info.ttf",24),
    "medium_large": pygame.font.Font(BASE_DIR / "fonts" / "info.ttf",28),
    "large": pygame.font.Font(BASE_DIR / "fonts" / "info.ttf",32),
    "text_small": pygame.font.Font(BASE_DIR / "fonts" / "text.ttf", 16),
    "text_small_medium": pygame.font.Font(BASE_DIR / "fonts" / "text.ttf",20),
    "text_medium": pygame.font.Font(BASE_DIR / "fonts" / "text.ttf",24),
    "text_medium_large": pygame.font.Font(BASE_DIR / "fonts" / "text.ttf",28),
    "text_large": pygame.font.Font(BASE_DIR / "fonts" / "text.ttf",32),
    "title_small": pygame.font.Font(BASE_DIR / "fonts" / "title.ttf",16),
    "title_small_medium": pygame.font.Font(BASE_DIR / "fonts" / "title.ttf",20),
    "title_medium": pygame.font.Font(BASE_DIR / "fonts" / "title.ttf",24),
    "title_medium_large": pygame.font.Font(BASE_DIR / "fonts" / "title.ttf",28),
    "title_large": pygame.font.Font(BASE_DIR / "fonts" / "title.ttf",32),
}

# Dialogue
DIALOGUE = {
    "intro_0" : "ALKELE GAMES",
    "intro_1" : "Presents",
    "intro_2" : "",
    "intro_3" : "",
    "intro_4" : "",
    "intro_5" : "",
    "predialogue_0" : "The Beginning",
    "predialogue_1" : "In a world where darkness threatens to devour",
    "predialogue_2" : "everything in its path, a hero rises up to meet the",
    "predialogue_3" : "challenge and bring the light of hope",
    "predialogue_4" : "to those who need it most.",
    "predialogue_5" : "We only know that his name is... Khan Lockwood",
    "credits1_0" : "CREDITS",
    "credits1_1" : "Contributors",
    "credits1_2" : "Alejandro Mujica",
    "credits1_3" : "Derwins Ochoa",
    "credits1_4" : "",
    "credits1_5" : "",
    "credits2_0" : "CREDITS",
    "credits2_1" : "Developers",
    "credits2_2" : "Kevin Marquez",
    "credits2_3" : "Lewis Ochoa",
    "credits2_4" : "",
    "credits2_5" : "",
    "credits3_0" : "CREDITS",
    "credits3_1" : "Graphics",
    "credits3_2" : "Anokolisa",
    "credits3_3" : "BDragon1727",
    "credits3_4" : "Craftpix",
    "credits3_5" : "Freepik",
    "credits4_0" : "CREDITS",
    "credits4_1" : "Graphics",
    "credits4_2" : "Kenney Vleugels",
    "credits4_3" : "Lewis Ochoa",
    "credits4_4" : "OddPotatoGift",
    "credits4_5" : "",
    "credits5_0" : "CREDITS",
    "credits5_1" : "Level Design",
    "credits5_2" : "Derwins Ochoa",
    "credits5_3" : "Kevin Marquez",
    "credits5_4" : "Lewis Ochoa",
    "credits5_5" : "",
    "credits6_0" : "CREDITS",
    "credits6_1" : "Soundtrack",
    "credits6_2" : "Luis Zuno (Ansimuz)",
    "credits6_3" : "",
    "credits6_4" : "",
    "credits6_5" : "",
    "credits7_0" : "CREDITS",
    "credits7_1" : "Sound Effects",
    "credits7_2" : "Fesliyanstudios",
    "credits7_3" : "Jurij Kornukov",
    "credits7_4" : "SnakeF8 (F8 Studios)",
    "credits7_5" : "UNIVERSFIELD",
    "credits8_0" : "CREDITS",
    "credits8_1" : "Text Fonts",
    "credits8_2" : "Glitter Dazed",
    "credits8_3" : "Jayde Garrow",
    "credits8_4" : "Spideray's Fonts",
    "credits8_5" : "",
    "credits9_0" : "CREDITS",
    "credits9_1" : "Voice Actors",
    "credits9_2" : "Alex Brodie",
    "credits9_3" : "Dillon Becker",
    "credits9_4" : "Karen Cenon",
    "credits9_5" : "Ian Lampert",
    "credits10_0" : "CREDITS",
    "credits10_1" : "Voice Actors",
    "credits10_2" : "Meghan Christian",
    "credits10_3" : "Sean Lenhart",
    "credits10_4" : "",
    "credits10_5" : "",
    "credits11_0" : "ALKELE GAMES",
    "credits11_1" : "Universidad de Los Andes",
    "credits11_2" : "Faculty of Engineering",
    "credits11_3" : "Video Game Programming",
    "credits11_4" : "Venezuela 2023",
    "credits11_5" : "All Rights Reserved",
}