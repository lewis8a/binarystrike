"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Kevin Márquez
marquezberriosk@gmail.com

Author: Lewis Ochoa
lewis8a@gmail.com

This file contains the class PausaState.
"""
from typing import Dict, Any

import pygame

from gale.input_handler import InputData
from gale.state import BaseState
from gale.text import render_text

import settings


class PausaState(BaseState):
    def enter(self, **enter_params: Dict[str, Any]) -> None:
        self.timer = enter_params.get("timer")
        self.level = enter_params.get("level")
        self.camera = enter_params.get("camera")
        self.game_level = enter_params.get("game_level")
        self.bullets = enter_params.get("bullets")
        self.player = self.game_level.player
        self.tilemap = self.game_level.tilemap
        # Entry sound
        settings.SOUNDS["menu-play"].stop()
        settings.SOUNDS["menu-play"].play()
        # Reproducir música de pausa

    def exit(self) -> None:
        # Detener música de pausa
        # Exit sound
        settings.SOUNDS["menu-play"].stop()
        settings.SOUNDS["menu-play"].play()
        pass

    def update(self, dt: float) -> None:
        pass

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
            settings.FONTS["small"],
            5,
            5,
            (255, 255, 255),
            shadowed=True,
        )

        render_text(
            surface,
            f"Time: {self.timer}",
            settings.FONTS["small"],
            settings.VIRTUAL_WIDTH - 80,
            5,
            (255, 255, 255),
            shadowed=True,
        )

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "pause" and input_data.pressed:
            self.state_machine.change(
                "play",
                player=self.player,
                timer=self.timer,
                level=self.level,
                camera=self.camera,
                game_level=self.game_level,
                bullets=self.bullets,
            )
