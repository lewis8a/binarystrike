"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Kevin Márquez
marquezberriosk@gmail.com

Author: Lewis Ochoa
lewis8a@gmail.com

This file contains the class EndState.
"""
import pygame
import settings

from gale.state import BaseState
from gale.input_handler import InputData
from gale.text import render_text
from gale.timer import Timer
from typing import Dict, Any


class EndState(BaseState):
    def enter(self, **enter_params: Dict[str, Any]) -> None:
        self.level = enter_params.get("level")
        self.score = enter_params.get("score")
        
        #Khan texture
        self.khan_texture = settings.TEXTURES[f"khan{settings.PLAYER_COLOR}"]

        # Stop music and unload
        if settings.MUSIC:
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
        
        if settings.SOUND:
            settings.SOUNDS["level_failed"].play()
        
        Timer.tween(
            4,
            [(self, {})],
            on_finish = self.arrive,
        )

    def exit(self) -> None:
        # Registering for entries
        Timer.clear()
        settings.SOUNDS["level_failed"].stop()
        settings.SOUNDS["game_over"].stop()

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "enter" and input_data.pressed:
            self.state_machine.change("start")

    def render(self, surface: pygame.Surface) -> None:
        surface.fill((0, 0, 0))

        render_text(
            surface,
            "Mission Failed!",
            settings.FONTS["text_medium"],
            settings.VIRTUAL_WIDTH // 2,
            20,
            (255, 255, 255),
            center=True,
            shadowed=True,
        )

        render_text(
            surface,
            "Game Over",
            settings.FONTS["title_large"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT // 2 - 30,
            (255, 255, 255),
            center=True,
            shadowed=True,
        )

        render_text(
            surface,
            f"Final Score: {self.score}",
            settings.FONTS["small"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT - 50,
            (255, 255, 255),
            shadowed=True,
            center=True,
        )

        render_text(
            surface,
            "Press Enter to start the adventure again!",
            settings.FONTS["text_small"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT - 20,
            (255, 255, 255),
            center=True,
            shadowed=True,
        )

        #Khan
        surface.blit(
            self.khan_texture,
            (settings.VIRTUAL_WIDTH // 2.15, settings.VIRTUAL_HEIGHT // 2.3),
            settings.FRAMES[f"khan{settings.PLAYER_COLOR}"][38],
        )

    def arrive(self):
        if settings.SOUND:
            settings.SOUNDS["game_over"].play()
