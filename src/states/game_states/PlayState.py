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

from gale.input_handler import InputHandler, InputData
from gale.state_machine import BaseState
from gale.text import render_text
from gale.timer import Timer

import settings
from src.Camera import Camera
from src.GameLevel import GameLevel
from src.Player import Player


class PlayState(BaseState):
    def enter(self, **enter_params: Dict[str, Any]) -> None:
        self.player = enter_params.get("player")
        self.timer = enter_params.get("timer", 60)
        self.level = enter_params.get("level", 1)
        self.camera = enter_params.get(
            "camera", Camera(0, 0, settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT)
        )
        
        self.game_level = enter_params.get("game_level")

        if self.game_level is None:
            self.game_level = GameLevel(self.level, self.camera)

        self.tilemap = self.game_level.tilemap
        if self.level == 1:
            self.player = Player(0, settings.VIRTUAL_HEIGHT - 16 * 6, self.game_level)

        self.player.change_state("idle")

        pygame.mixer.music.load(settings.BASE_DIR / "assets/music/level1.ogg")
        pygame.mixer.music.play(loops=-1)

        def countdown_timer():
            self.timer -= 1

            # if 0 < self.timer <= 5:
            #     settings.SOUNDS["timer"].play()

            if self.timer == 0:
                self.player.change_state("dead")

        Timer.every(1, countdown_timer)
        InputHandler.register_listener(self)

    def exit(self) -> None:
        InputHandler.unregister_listener(self)
        Timer.clear()

    def update(self, dt: float) -> None:
        if self.player.is_dead:
            pass
            # pygame.mixer.music.stop()
            # pygame.mixer.music.unload()
            # settings.SOUNDS["game_over"].stop()
            # settings.SOUNDS["game_over"].play()
            # self.state_machine.change("game_over", self.player, self.level)

        self.player.update(dt)
    
        if self.player.y >= self.player.tilemap.height:
            self.player.change_state("dead")

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

        self.game_level.update(dt)

        # for creature in self.game_level.creatures:
        #     if self.player.collides(creature):
        #         self.player.change_state("dead")

        # for item in self.game_level.items:
        #     if not item.in_play or not item.collidable:
        #         continue
            
        #     if self.player.collides(item):
        #         if item.type == "key":
        #             item.on_consume(self.player, level = self.level + 1, state_machine = self.state_machine)
        #         elif item.type == "key_block" and not item.activate:
        #             key_object = [key for key in self.game_level.items if  key.type == "key" and key.y == item.y and key.x == item.x]
        #             item.on_collide(self.player, item_key = key_object[0])
        #         else:
        #             item.on_collide(self.player)
        #             item.on_consume(self.player)
        # goal_score_by_level = settings.GOAL_SCORE * self.level
        # if self.player.score >= goal_score_by_level and not self.key:
        #     self.key = True
        #     # Clean coins of world
        #     self.game_level.items = [key for key in self.game_level.items if key.type == "key" or key.type == "key_block"]
        #     # Frezzing time
        #     time = self.timer
        #     Timer.clear()
        #     self.timer = time
        #     # Play sound
        #     settings.SOUNDS["goal_score"].stop()
        #     settings.SOUNDS["goal_score"].play()
        #     settings.SOUNDS["timer"].play()
        #     # Spawn key block
        #     keys_objects = [key for key in self.game_level.items if key.type == "key_block"]
        #     for key_object in keys_objects:
        #         key_object.in_play = True

    def render(self, surface: pygame.Surface) -> None:
        world_surface = pygame.Surface((self.tilemap.width, self.tilemap.height))
        self.game_level.render(world_surface)
        self.player.render(world_surface)
        surface.blit(world_surface, (-self.camera.x, -self.camera.y))

        # render_text(
        #     surface,
        #     f"Score: {self.player.score}",
        #     settings.FONTS["small"],
        #     5,
        #     5,
        #     (255, 255, 255),
        #     shadowed=True,
        # )

        # render_text(
        #     surface,
        #     f"Time: {self.timer}",
        #     settings.FONTS["small"],
        #     settings.VIRTUAL_WIDTH - 60,
        #     5,
        #     (255, 255, 255),
        #     shadowed=True,
        # )

    def on_input(self, input_id: str, input_data: InputData) -> None:
        pass
        # if input_id == "pause" and input_data.pressed:
        #     self.state_machine.change(
        #         "pause",
        #         level=self.level,
        #         camera=self.camera,
        #         game_level=self.game_level,
        #         player=self.player,
        #         timer=self.timer,
        #     )
