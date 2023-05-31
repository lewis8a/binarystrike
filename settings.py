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
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_j, "jump")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_f, "shoot")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_k, "shoot")

# Tile size
TILE_SIZE = 16

# Size we want to emulate
VIRTUAL_WIDTH = 300
VIRTUAL_HEIGHT = 192

# Size of our actual window (Aspect ratio 16:9)
pygame.init()
WINDOW_WIDTH = pygame.display.Info().current_w
WINDOW_HEIGHT = (9/16) * pygame.display.Info().current_w
SAFEZONE = 0

# Basic game settings
PLAYER_SPEED = 80
PLAYER_COLOR = 1
GRAVITY = 350
NUM_LEVELS = 4
PROJECTILE_SPEED = 170
RANGE_VISION = 100
GOAL_SCORE = 35
TIME = 300
MUSIC = 1
SOUND = 1

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
    "tile_4": pygame.image.load(BASE_DIR / "assets" / "graphics" / "tilesets" / "tileset_4.png"),
    "khan1": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "khanlockwood" / "khan_1.png"),
    "khan2": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "khanlockwood" / "khan_2.png"),
    "khan3": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "khanlockwood" / "khan_3.png"),
    "khan4": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "khanlockwood" / "khan_4.png"),
    "khan5": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "khanlockwood" / "khan_5.png"),
    "khan6": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "khanlockwood" / "khan_6.png"),
    "khan7": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "khanlockwood" / "khan_7.png"),
    "khan8": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "khanlockwood" / "khan_8.png"),
    "khan9": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "khanlockwood" / "khan_9.png"),
    "khan10": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "khanlockwood" / "khan_10.png"),
    "khan11": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "khanlockwood" / "khan_11.png"),
    "khan12": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "khanlockwood" / "khan_12.png"),
    "khan13": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "khanlockwood" / "khan_13.png"),
    "khan14": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "khanlockwood" / "khan_14.png"),
    "khan15": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "khanlockwood" / "khan_15.png"),
    "khan16": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "khanlockwood" / "khan_16.png"),
    "khan17": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "khanlockwood" / "khan_17.png"),
    "khan18": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "khanlockwood" / "khan_18.png"),
    "khan19": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "khanlockwood" / "khan_19.png"),
    "khan20": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "khanlockwood" / "khan_20.png"),
    "khan21": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "khanlockwood" / "khan_21.png"),
    "khan22": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "khanlockwood" / "khan_22.png"),
    "khan23": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "khanlockwood" / "khan_23.png"),
    "khan24": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "khanlockwood" / "khan_24.png"),
    "khan25": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "khanlockwood" / "khan_25.png"),
    "khan26": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "khanlockwood" / "khan_26.png"),
    "khan27": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "khanlockwood" / "khan_27.png"),
    "khan28": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "khanlockwood" / "khan_28.png"),
    "khan29": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "khanlockwood" / "khan_29.png"),
    "khan30": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "khanlockwood" / "khan_30.png"),
    "bullet_player": pygame.image.load(BASE_DIR / "assets" / "graphics" / "objects" / "BulletPlayer.png"),
    "bullet_enemy": pygame.image.load(BASE_DIR / "assets" / "graphics" / "objects" / "BulletEnemy.png"),
    "enemy1_walk": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "enemies" / "enemy1" / "Walk.png"),
    "enemy1_shoot": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "enemies" / "enemy1" / "Shot.png"),
    "enemy1_idle": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "enemies" / "enemy1" / "Idle.png"),
    "enemy1_dead": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "enemies" / "enemy1" / "Dead.png"),
    "enemy2_walk": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "enemies" / "enemy2" / "Walk.png"),
    "enemy2_shoot": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "enemies" / "enemy2" / "Shot.png"),
    "enemy2_idle": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "enemies" / "enemy2" / "Idle.png"),
    "enemy2_dead": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "enemies" / "enemy2" / "Dead.png"),
    "enemy3_walk": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "enemies" / "enemy3" / "Walk.png"),
    "enemy3_shoot": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "enemies" / "enemy3" / "Shot.png"),
    "enemy3_idle": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "enemies" / "enemy3" / "Idle.png"),
    "enemy3_dead": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "enemies" / "enemy3" / "Dead.png"),
    "play_btn_0": pygame.image.load(BASE_DIR / "assets" / "graphics" / "ui" / "play_btn_0.png"),
    "play_btn_1": pygame.image.load(BASE_DIR / "assets" / "graphics" / "ui" / "play_btn_1.png"),
    "settings_btn_0": pygame.image.load(BASE_DIR / "assets" / "graphics" / "ui" / "settings_btn_0.png"),
    "settings_btn_1": pygame.image.load(BASE_DIR / "assets" / "graphics" / "ui" / "settings_btn_1.png"),
    "info_btn_0": pygame.image.load(BASE_DIR / "assets" / "graphics" / "ui" / "info_btn_0.png"),
    "info_btn_1": pygame.image.load(BASE_DIR / "assets" / "graphics" / "ui" / "info_btn_1.png"),
    "ok_btn_0": pygame.image.load(BASE_DIR / "assets" / "graphics" / "ui" / "ok_btn_0.png"),
    "ok_btn_1": pygame.image.load(BASE_DIR / "assets" / "graphics" / "ui" / "ok_btn_1.png"),
    "backward_btn_0": pygame.image.load(BASE_DIR / "assets" / "graphics" / "ui" / "backward_btn_0.png"),
    "backward_btn_1": pygame.image.load(BASE_DIR / "assets" / "graphics" / "ui" / "backward_btn_1.png"),
    "forward_btn_0": pygame.image.load(BASE_DIR / "assets" / "graphics" / "ui" / "forward_btn_0.png"),
    "forward_btn_1": pygame.image.load(BASE_DIR / "assets" / "graphics" / "ui" / "forward_btn_1.png"),
    "music_btn_0": pygame.image.load(BASE_DIR / "assets" / "graphics" / "ui" / "music_btn_0.png"),
    "music_btn_1": pygame.image.load(BASE_DIR / "assets" / "graphics" / "ui" / "music_btn_1.png"),
    "sound_btn_0": pygame.image.load(BASE_DIR / "assets" / "graphics" / "ui" / "sound_btn_0.png"),
    "sound_btn_1": pygame.image.load(BASE_DIR / "assets" / "graphics" / "ui" / "sound_btn_1.png"),
    "settings_btn_0": pygame.image.load(BASE_DIR / "assets" / "graphics" / "ui" / "settings_btn_0.png"),
    "settings_btn_1": pygame.image.load(BASE_DIR / "assets" / "graphics" / "ui" / "settings_btn_1.png"),
    "bar": pygame.image.load(BASE_DIR / "assets" / "graphics" / "ui" / "bar.png"),
    "bar_2": pygame.image.load(BASE_DIR / "assets" / "graphics" / "ui" / "bar_2.png"),
    "window": pygame.image.load(BASE_DIR / "assets" / "graphics" / "ui" / "window.png"),
    "window_2": pygame.image.load(BASE_DIR / "assets" / "graphics" / "ui" / "window_2.png"),
    "lives": pygame.image.load(BASE_DIR / "assets" / "graphics" / "objects" / "Lives.png"),
    "boss1_dead": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "boss" / "boss1" / "Dead.png"),
    "boss1_idle": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "boss" / "boss1" / "Idle.png"),
    "boss1_immune": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "boss" / "boss1" / "Immune.png"),
    "boss1_shoot": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "boss" / "boss1" / "Shot.png"),
    "boss1_walk": pygame.image.load(BASE_DIR / "assets" / "graphics" / "characters" / "boss" / "boss1" / "Walk.png"),
    "live_powerup": pygame.image.load(BASE_DIR / "assets" / "graphics" / "objects" / "Card.png"),
    "box_powerup": pygame.image.load(BASE_DIR / "assets" / "graphics" / "objects" / "Chest.png"),
}

# Frames
FRAMES = {
    "tile_1": frames.generate_frames(TEXTURES["tile_1"], 16, 16),
    "tile_2": frames.generate_frames(TEXTURES["tile_2"], 16, 16),
    "tile_3": frames.generate_frames(TEXTURES["tile_3"], 16, 16),
    "tile_4": frames.generate_frames(TEXTURES["tile_4"], 16, 16),
    "khan1": frames.generate_frames(TEXTURES["khan1"], 20, 34),
    "khan2": frames.generate_frames(TEXTURES["khan2"], 20, 34),
    "khan3": frames.generate_frames(TEXTURES["khan3"], 20, 34),
    "khan4": frames.generate_frames(TEXTURES["khan4"], 20, 34),
    "khan5": frames.generate_frames(TEXTURES["khan5"], 20, 34),
    "khan6": frames.generate_frames(TEXTURES["khan6"], 20, 34),
    "khan7": frames.generate_frames(TEXTURES["khan7"], 20, 34),
    "khan8": frames.generate_frames(TEXTURES["khan8"], 20, 34),
    "khan9": frames.generate_frames(TEXTURES["khan9"], 20, 34),
    "khan10": frames.generate_frames(TEXTURES["khan10"], 20, 34),
    "khan11": frames.generate_frames(TEXTURES["khan11"], 20, 34),
    "khan12": frames.generate_frames(TEXTURES["khan12"], 20, 34),
    "khan13": frames.generate_frames(TEXTURES["khan13"], 20, 34),
    "khan14": frames.generate_frames(TEXTURES["khan14"], 20, 34),
    "khan15": frames.generate_frames(TEXTURES["khan15"], 20, 34),
    "khan16": frames.generate_frames(TEXTURES["khan16"], 20, 34),
    "khan17": frames.generate_frames(TEXTURES["khan17"], 20, 34),
    "khan18": frames.generate_frames(TEXTURES["khan18"], 20, 34),
    "khan19": frames.generate_frames(TEXTURES["khan19"], 20, 34),
    "khan20": frames.generate_frames(TEXTURES["khan20"], 20, 34),
    "khan21": frames.generate_frames(TEXTURES["khan21"], 20, 34),
    "khan22": frames.generate_frames(TEXTURES["khan22"], 20, 34),
    "khan23": frames.generate_frames(TEXTURES["khan23"], 20, 34),
    "khan24": frames.generate_frames(TEXTURES["khan24"], 20, 34),
    "khan25": frames.generate_frames(TEXTURES["khan25"], 20, 34),
    "khan26": frames.generate_frames(TEXTURES["khan26"], 20, 34),
    "khan27": frames.generate_frames(TEXTURES["khan27"], 20, 34),
    "khan28": frames.generate_frames(TEXTURES["khan28"], 20, 34),
    "khan29": frames.generate_frames(TEXTURES["khan29"], 20, 34),
    "khan30": frames.generate_frames(TEXTURES["khan30"], 20, 34),
    "bullet_player": frames.generate_frames(TEXTURES["bullet_player"], 8, 8),
    "bullet_enemy": frames.generate_frames(TEXTURES["bullet_enemy"], 5, 5),
    "enemy1_walk": frames.generate_frames(TEXTURES["enemy1_walk"], 20, 34),
    "enemy1_shoot": frames.generate_frames(TEXTURES["enemy1_shoot"], 20, 34),
    "enemy1_idle": frames.generate_frames(TEXTURES["enemy1_idle"], 20, 34),
    "enemy1_dead": frames.generate_frames(TEXTURES["enemy1_dead"], 20, 34),
    "enemy2_walk": frames.generate_frames(TEXTURES["enemy2_walk"], 20, 34),
    "enemy2_shoot": frames.generate_frames(TEXTURES["enemy2_shoot"], 20, 34),
    "enemy2_idle": frames.generate_frames(TEXTURES["enemy2_idle"], 20, 34),
    "enemy2_dead": frames.generate_frames(TEXTURES["enemy2_dead"], 20, 34),
    "enemy3_walk": frames.generate_frames(TEXTURES["enemy3_walk"], 20, 34),
    "enemy3_shoot": frames.generate_frames(TEXTURES["enemy3_shoot"], 20, 34),
    "enemy3_idle": frames.generate_frames(TEXTURES["enemy3_idle"], 20, 34),
    "enemy3_dead": frames.generate_frames(TEXTURES["enemy3_dead"], 20, 34),
    "boss1_dead": frames.generate_frames(TEXTURES["boss1_dead"], 40, 50),
    "boss1_idle": frames.generate_frames(TEXTURES["boss1_idle"], 40, 50),
    "boss1_immune": frames.generate_frames(TEXTURES["boss1_immune"], 40, 50),
    "boss1_shoot": frames.generate_frames(TEXTURES["boss1_shoot"], 40, 50),
    "boss1_walk": frames.generate_frames(TEXTURES["boss1_walk"], 40, 50),
    "live_powerup": frames.generate_frames(TEXTURES["live_powerup"], 12, 14),
    "box_powerup": frames.generate_frames(TEXTURES["box_powerup"], 32, 26),
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
    "boss1": pygame.mixer.Sound(BASE_DIR / "assets" / "music" / "boss1.ogg"),
    "boss2": pygame.mixer.Sound(BASE_DIR / "assets" / "music" / "boss2.ogg"),
    "boss3": pygame.mixer.Sound(BASE_DIR / "assets" / "music" / "boss3.ogg"),
    "finalboss": pygame.mixer.Sound(BASE_DIR / "assets" / "music" / "finalboss.ogg"),
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
    "death4": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "enemies" / "death_1.wav"),
    "death5": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "enemies" / "death_2.wav"),
    "death6": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "enemies" / "death_3.wav"),
    "death7": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "enemies" / "death_4.wav"),
    "death8": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "enemies" / "death_5.wav"),
    "jump1": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "khanlockwood" / "jumping_1.wav"),
    "jump2": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "khanlockwood" / "jumping_2.wav"),
    "jump3": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "khanlockwood" / "jumping_3.wav"),
    "jump4": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "khanlockwood" / "jumping_4.wav"),
    "start1": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "khanlockwood" / "start_1.wav"),
    "start2": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "khanlockwood" / "start_2.wav"),
    "start3": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "khanlockwood" / "start_3.wav"),
    "start4": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "khanlockwood" / "start_4.wav"),
    "start5": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "khanlockwood" / "start_5.wav"),
    "start6": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "khanlockwood" / "start_6.wav"),
    "start7": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "khanlockwood" / "start_7.wav"),
    "start8": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "khanlockwood" / "start_8.wav"),
    "game_over": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "khanlockwood" / "gameover.wav"),
    "menu_change": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "menu" / "menu_change.mp3"),
    "menu_character": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "menu" / "menu_character.mp3"),
    "menu_enter": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "menu" / "menu_enter.mp3"),
    "menu_play": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "menu" / "menu_play.mp3"),
    "menu_return": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "menu" / "menu_return.mp3"),
    "menu_select": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "menu" / "menu_select.mp3"),
    "reborn": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "khanlockwood" / "321go.wav"),
    "take-lives": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "powerup" / "powerup_3.mp3"),
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
    "text_xs": pygame.font.Font(BASE_DIR / "fonts" / "text.ttf", 12),
    "text_small": pygame.font.Font(BASE_DIR / "fonts" / "text.ttf", 16),
    "text_small_medium": pygame.font.Font(BASE_DIR / "fonts" / "text.ttf",20),
    "text_medium": pygame.font.Font(BASE_DIR / "fonts" / "text.ttf",24),
    "text_medium_large": pygame.font.Font(BASE_DIR / "fonts" / "text.ttf",28),
    "text_large": pygame.font.Font(BASE_DIR / "fonts" / "text.ttf",32),
    "title_xs": pygame.font.Font(BASE_DIR / "fonts" / "title.ttf",12),
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
    "credits3_5" : "Fightswithbears",
    "credits4_0" : "CREDITS",
    "credits4_1" : "Graphics",
    "credits4_2" : "Freepik",
    "credits4_3" : "Kenney Vleugels",
    "credits4_4" : "Lewis Ochoa",
    "credits4_5" : "OddPotatoGift",
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

#Name of the levels
NAME = {
    "level_1" : "Shadow Forest",
    "level_2" : "City Of Steel Craftsmen",
    "level_3" : "Land Of Infinite Corrosion",
    "level_4" : "Bash Corporation",
}