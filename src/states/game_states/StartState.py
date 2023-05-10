"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Kevin Márquez
marquezberriosk@gmail.com

Author: Lewis Ochoa
lewis8a@gmail.com

This file contains the class StartState.
"""
import pygame

from gale.animation import Animation
from gale.input_handler import InputData
from gale.state import BaseState
from gale.text import Text, render_text
from gale.timer import Timer

import settings


class StartState(BaseState):

    def enter(self) -> None:
        self.title = Text(
            "Binary Strike",
            settings.FONTS["medium"],
            settings.VIRTUAL_WIDTH / 4, 
            settings.VIRTUAL_HEIGHT / 2,
            (255, 255, 255),
            shadowed=True,
        )

        # A surface that supports alpha for the screen
        self.screen_alpha_surface = pygame.Surface(
            (settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT), pygame.SRCALPHA
        )

        pygame.mixer.music.load(settings.BASE_DIR / "assets/music/menu.ogg")
        pygame.mixer.music.play(loops=-1)

    def exit(self) -> None:
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()

    def render(self, surface: pygame.Surface) -> None:
        surface.fill((0, 0, 0))
        self.title.render(surface)
        render_text(
            surface,
            "Press Enter",
            settings.FONTS["small"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT // 2 + 40,
            (197, 195, 198),
            center=True,
            shadowed=True,
        )
    
    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "enter" and input_data.pressed:
            self.state_machine.change("begin")