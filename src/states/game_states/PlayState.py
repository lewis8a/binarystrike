"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Kevin Márquez
marquezberriosk@gmail.com

Author: Lewis Ochoa
lewis8a@gmail.com

This file contains the class PlayState.
"""
from typing import Dict, Any

import pygame
import settings

from gale.input_handler import InputHandler, InputData
from gale.state import BaseState
from gale.text import render_text
from gale.timer import Every, After, Tween
from numpy import random
from src.Camera import Camera
from src.GameLevel import GameLevel
from src.Player import Player
from src.GameBox import GameBox
from src.GamePowerup import GamePowerup

class State:
    def __init__(self) -> None:
        self.player = None
        self.timer = None
        self.level = None
        self.camera = None
        self.game_level = None
        self.pos_music = None
        self.tilemap = None
        self.timers = None
        self.x_live = 7
        self.y_live = 20

class PlayState(BaseState):
    def enter(self, **enter_params: Dict[str, Any]) -> None:
        self.state = enter_params.get("ss")
        #self.state.player = enter_params.get("player")
        #self.timer = enter_params.get("timer")#, settings.TIME)
        #self.state.level = enter_params.get("level", 1)
        #self.camera = enter_params.get(
        #    "camera", Camera(0, 0, settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT)
        #)
        #self.state.game_level = enter_params.get("game_level", GameLevel(self.state.level, self.camera))
        #self.pos_music = enter_params.get("pos_music", 0.0)
        #self.tilemap = self.state.game_level.tilemap
        #self.x_live = 7
        #self.y_live = 20
        pygame.mixer.music.set_volume(0.3)


        if self.state is None:
            self.state = State()
            self.state.level = 1
            self.state.camera = Camera(0, 0, settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT)
            self.state.game_level = GameLevel(self.state.level, self.state.camera)
            self.state.pos_music = 0.0
            self.state.tilemap = self.state.game_level.tilemap
            self.state.timers = []

        # Play sound player voice
        randomStartSound = random.randint(1,8)
        settings.SOUNDS[f"start{randomStartSound}"].set_volume(0.8)
        settings.SOUNDS[f"start{randomStartSound}"].stop()
        if settings.SOUND:
            settings.SOUNDS[f"start{randomStartSound}"].play()

        if self.state.level == 1:
            if self.state.player == None:
                self.state.player = Player(2 * 16, settings.VIRTUAL_HEIGHT - 16*2, self.state.game_level, {"dead": self.after_die})
                self.state.player.change_state("idle")
                self.state.game_level.player = self.state.player
            
            if settings.MUSIC:
                pygame.mixer.music.load(settings.BASE_DIR / "assets/music/level1.ogg")
        elif self.state.level == 2:
            if self.state.player == None:
                self.state.player = Player(16 * 2, 16 * 2, self.state.game_level, {"dead": self.after_die})
                self.state.player.change_state("idle")
                self.state.player.score = enter_params.get("score", 0)
                self.state.player.lives = enter_params.get("lives", 3)
                self.state.game_level.player = self.state.player
            if settings.MUSIC:
                pygame.mixer.music.load(settings.BASE_DIR / "assets/music/level2.ogg")
        elif self.state.level == 3:
            if self.state.player == None:
                self.state.player = Player(16 * 2, 16 * 2, self.state.game_level, {"dead": self.after_die})
                self.state.player.change_state("idle")
                self.state.player.score = enter_params.get("score", 0)
                self.state.player.lives = enter_params.get("lives", 3)
                self.state.game_level.player = self.state.player
            if settings.MUSIC:
                pygame.mixer.music.load(settings.BASE_DIR / "assets/music/level3.ogg")
        elif self.state.level == 4:
            if self.state.player == None:
                self.state.player = Player(16 * 2, 16 * 2, self.state.game_level, {"dead": self.after_die})
                self.state.player.change_state("idle")
                self.state.player.score = enter_params.get("score", 0)
                self.state.player.lives = enter_params.get("lives", 3)
                self.state.game_level.player = self.state.player
            if settings.MUSIC:
                pygame.mixer.music.load(settings.BASE_DIR / "assets/music/finalboself.state.ogg")
        if settings.MUSIC:
            pygame.mixer.music.play(loops=-1, start=self.state.pos_music)


        if self.state.timer is None:
            self.state.timer = settings.TIME
            def countdown_timer():
                self.state.timer -= 1

                if self.state.timer == 11 and settings.SOUND:
                    settings.SOUNDS["level_time"].set_volume(0.5)
                    settings.SOUNDS["level_time"].play()

                if self.state.timer == 0:
                    InputHandler.unregister_listener(self.state.player.state_machine.current)
                    self.state_machine.change(
                        "end",
                        level = self.state.level,
                        score = self.state.player.score,
                    )

            self.state.timers.append(Every(1, countdown_timer))

    def exit(self) -> None:
        for i in range(len(self.state.game_level.enemies) - 1, -1, -1):
            if self.state.game_level.enemies[i].current_animation_id == "dead":
                del self.state.game_level.enemies[i]

        # Stop music and unload
        if settings.MUSIC:
            pygame.mixer.music.unload()
            pygame.mixer.music.stop()

    def update(self, dt: float) -> None:
        if self.state.player.is_dead:
            self.state.player.change_state("dead", on_finish=self.after_die)

        elif self.state.player.y >= self.state.player.tilemap.height:
            self.state.player.is_dead = True
        else:
            self.state.player.update(dt)

        for timer in self.state.timers:
            timer.update(dt)

        self.state.camera.x = max(
            0,
            min(
                self.state.player.x + 8 - settings.VIRTUAL_WIDTH // 2,
                self.state.tilemap.width - settings.VIRTUAL_WIDTH,
            ),
        )
        self.state.camera.y = max(
            0,
            min(
                self.state.player.y + 10 - settings.VIRTUAL_HEIGHT // 2,
                self.state.tilemap.height - settings.VIRTUAL_HEIGHT,
            ),
        )
        
        for i in range(len(self.state.player.bullets) - 1, -1, -1):
            for enemy in self.state.game_level.enemies:
                if enemy.current_animation_id != "dead" and self.state.player.bullets[i].collides(enemy):
                    self.state.player.bullets[i].in_play = False
                    enemy.change_state("dead")
                    self.state.player.score += enemy.points
            
            if self.state.game_level.boss.current_animation_id != "dead" and self.state.player.bullets[i].collides(self.state.game_level.boss):
                    self.state.player.bullets[i].in_play = False
                    self.state.player.score += self.state.game_level.boss.receive_damage(1)
            
            if self.state.player.bullets[i].in_play:
                self.state.player.bullets[i].update(dt)
            else:
                del self.state.player.bullets[i]
        
        if self.state.game_level.boss.is_dead:
            self.state_machine.change(
                "begin",
                level = self.state.level + 1,
                score = self.state.player.score,
                lives = self.state.player.lives,
            )

        self.state.game_level.update(dt)


        for item in self.state.game_level.items:
            if not item.in_play or not item.collidable:
                continue
            
            if self.state.player.collides(item):
                if isinstance(item, GamePowerup):
                    item.on_consume(self.state.player)
                elif isinstance(item, GameBox) and not item.activate:
                    item.on_collide(self.state.player)

    def render(self, surface: pygame.Surface) -> None:
        world_surface = pygame.Surface((self.state.tilemap.width, self.state.tilemap.height))
        self.state.game_level.render(world_surface)
        self.state.player.render(world_surface)
        for bullet in self.state.player.bullets:
            bullet.render(world_surface)

        surface.blit(world_surface, (-self.state.camera.x, -self.state.camera.y))

        render_text(
            surface,
            f"Score: {self.state.player.score}",
            settings.FONTS["xs"],
            5,
            5,
            (255, 255, 255),
            shadowed=True,
        )

        render_text(
            surface,
            f"Time: {self.state.timer}",
            settings.FONTS["xs"],
            settings.VIRTUAL_WIDTH - 50,
            5,
            (255, 255, 255),
            shadowed=True,
        )

        stop = min(8, self.state.player.lives)
        for i in range(0, stop):
            surface.blit(settings.TEXTURES["lives"],
                         (self.state.x_live + self.state.x_live*i, self.state.y_live))

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "pause" and input_data.pressed:            
            self.state_machine.change("pause", ss = self.state)
    
    def position_music(self) -> float:
        music_pos =  pygame.mixer.music.get_pos() / 1000
        if self.state.level == 1:
            if music_pos > 120:
                music_pos = music_pos % 120
        elif self.state.level == 2:
            if music_pos > 56:
                music_pos = music_pos % 56
        elif self.state.level == 3:
            if music_pos > 32:
                music_pos = music_pos % 32
        
        return music_pos

    # Callback after die player
    def after_die(self):
        self.state_machine.change("reborn", ss = self.state)