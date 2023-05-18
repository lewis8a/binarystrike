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
from gale.timer import Timer
from numpy import random
from src.Camera import Camera
from src.GameLevel import GameLevel
from src.Player import Player


class PlayState(BaseState):
    def enter(self, **enter_params: Dict[str, Any]) -> None:
        self.player = enter_params.get("player")
        self.timer = enter_params.get("timer", settings.TIME)
        self.level = enter_params.get("level", 1)
        self.camera = enter_params.get(
            "camera", Camera(0, 0, settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT)
        )
        self.game_level = enter_params.get("game_level", GameLevel(self.level, self.camera))
        self.bullets = enter_params.get("bullets", [])
        self.pos_music = enter_params.get("pos_music", 0.0)
        pygame.mixer.music.set_volume(0.3)

        self.tilemap = self.game_level.tilemap

        # Play sound player voice
        randomStartSound = random.randint(1,8)
        settings.SOUNDS[f"start{randomStartSound}"].set_volume(0.8)
        settings.SOUNDS[f"start{randomStartSound}"].stop()
        if settings.SOUND:
            settings.SOUNDS[f"start{randomStartSound}"].play()

        if self.level == 1:
            if hasattr(self.player, "play_state"):
                delattr(self.player, "play_state")
            else:
                self.player = Player(16, settings.VIRTUAL_HEIGHT - 16*2, self.game_level)
                self.player.change_state("idle")
                self.game_level.player = self.player
            if settings.MUSIC:
                pygame.mixer.music.load(settings.BASE_DIR / "assets/music/level1.ogg")
        elif self.level == 2:
            if hasattr(self.player, "play_state"):
                delattr(self.player, "play_state")
            else:
                self.player = Player(16 * 2, 16 * 2, self.game_level)
                self.player.change_state("idle")
                self.game_level.player = self.player
            if settings.MUSIC:
                pygame.mixer.music.load(settings.BASE_DIR / "assets/music/level2.ogg")
        elif self.level == 3:
            if hasattr(self.player, "play_state"):
                delattr(self.player, "play_state")
            else:
                self.player = Player(16 * 2, 16 * 2, self.game_level)
                self.player.change_state("idle")
                self.game_level.player = self.player
            if settings.MUSIC:
                pygame.mixer.music.load(settings.BASE_DIR / "assets/music/level3.ogg")
        elif self.level == 4:
            if hasattr(self.player, "play_state"):
                delattr(self.player, "play_state")
            else:
                self.player = Player(16 * 2, 16 * 2, self.game_level)
                self.player.change_state("idle")
                self.game_level.player = self.player
            if settings.MUSIC:
                pygame.mixer.music.load(settings.BASE_DIR / "assets/music/finalboss.ogg")
        if settings.MUSIC:
            pygame.mixer.music.play(loops=-1, start=self.pos_music)
        
        self.player.play_state = self

        def countdown_timer():
            self.timer -= 1

            if self.timer == 11:
                self.endTime = False
                settings.SOUNDS["level_time"].set_volume(0.5)
                if settings.SOUND:
                    settings.SOUNDS["level_time"].play()

            if self.timer == 0:
                InputHandler.unregister_listener(self.player.state_machine.current)
                self.state_machine.change(
                    "end",
                    level = self.level,
                    score = self.player.score,
                )

        Timer.every(1, countdown_timer)

        self.x_live = 7
        self.y_live = 20

    def exit(self) -> None:
        Timer.clear()
        for i in range(len(self.game_level.enemies) - 1, -1, -1):
            if self.game_level.enemies[i].current_animation_id == "dead":
                del self.game_level.enemies[i]

        # Stop music and unload
        if settings.MUSIC:
            pygame.mixer.music.unload()
            pygame.mixer.music.stop()

    def update(self, dt: float) -> None:
        if self.player.is_dead:            
            def after_die():
                self.state_machine.change(
                    "reborn",
                    timer = self.timer,
                    level = self.level,
                    camera = self.camera,
                    game_level = self.game_level,
                    bullets = self.bullets,
                    pos_music = self.position_music(),
                )

            self.player.change_state("dead", on_finish = after_die)

        elif self.player.y >= self.player.tilemap.height:
            self.player.is_dead = True
        else:
            self.player.update(dt)

        self.camera.x = max(
            0,
            min(
                self.player.x + 8 - settings.VIRTUAL_WIDTH // 2,
                self.tilemap.width - settings.VIRTUAL_WIDTH,
            ),
        )
        self.camera.y = max(
            0,
            min(
                self.player.y + 10 - settings.VIRTUAL_HEIGHT // 2,
                self.tilemap.height - settings.VIRTUAL_HEIGHT,
            ),
        )
        
        for i in range(len(self.bullets) - 1, -1, -1):
            for enemy in self.game_level.enemies:
                if enemy.current_animation_id != "dead" and self.bullets[i].collides(enemy):
                    self.bullets[i].in_play = False
                    enemy.change_state("dead")
                    self.player.score += enemy.points
            
            if self.game_level.boss.current_animation_id != "dead" and self.bullets[i].collides(self.game_level.boss):
                    self.bullets[i].in_play = False
                    self.player.score += self.game_level.boss.receive_damage(1)
            
            if self.bullets[i].in_play:
                self.bullets[i].update(dt)
            else:
                del self.bullets[i]
        
        if self.game_level.boss.is_dead:
            self.state_machine.change(
                "begin",
                level = self.level + 1,
            )

        self.game_level.update(dt)


        for item in self.game_level.items:
            if not item.in_play or not item.collidable:
                continue
            
            if self.player.collides(item):
                if item.type == "key":
                    item.on_consume(self.player)
                elif item.type == "boxpowerup" and not item.activate:
                    item.on_collide(self.player, powerup = item.powerup)

    def render(self, surface: pygame.Surface) -> None:
        world_surface = pygame.Surface((self.tilemap.width, self.tilemap.height))
        self.game_level.render(world_surface)
        self.player.render(world_surface)
        for bullet in self.bullets:
            bullet.render(world_surface)

        surface.blit(world_surface, (-self.camera.x, -self.camera.y))
        

        render_text(
            surface,
            f"Score: {self.player.score}",
            settings.FONTS["xs"],
            5,
            5,
            (255, 255, 255),
            shadowed=True,
        )

        render_text(
            surface,
            f"Time: {self.timer}",
            settings.FONTS["xs"],
            settings.VIRTUAL_WIDTH - 50,
            5,
            (255, 255, 255),
            shadowed=True,
        )

        stop = min(8, self.player.lives)
        for i in range(0, stop):
            surface.blit(settings.TEXTURES["lives"],
                         (self.x_live + self.x_live*i, self.y_live))

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "pause" and input_data.pressed:            
            self.state_machine.change(
                "pause",
                timer = self.timer,
                level = self.level,
                camera = self.camera,
                game_level = self.game_level,
                bullets = self.bullets,
                pos_music = self.position_music()
            )
    
    def position_music(self) -> float:
        music_pos =  pygame.mixer.music.get_pos() / 1000
        if self.level == 1:
            if music_pos > 120:
                music_pos = music_pos % 120
        elif self.level == 2:
            if music_pos > 56:
                music_pos = music_pos % 56
        elif self.level == 3:
            if music_pos > 32:
                music_pos = music_pos % 32
        
        return music_pos
