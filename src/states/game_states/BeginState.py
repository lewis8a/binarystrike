"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Kevin Márquez
marquezberriosk@gmail.com

Author: Lewis Ochoa
lewis8a@gmail.com

This file contains the class BeginState.
"""
from typing import Dict, Any

import pygame

from gale.state import BaseState
from gale.text import render_text
from gale.timer import Timer

import settings

class BeginState(BaseState):
    def enter(self, **enter_params: Dict[str, Any]) -> None:
        self.level = enter_params.get("level", 3)
        self.transition_alpha = 255
        self.display_text = True
        self.circle = max(settings.VIRTUAL_HEIGHT, settings.VIRTUAL_WIDTH) * 1.25

        # A surface that supports alpha for the screen
        self.screen_alpha_surface = pygame.Surface(
            (settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT), pygame.SRCALPHA
        )
        def arrive_after():
            # Then, animate the text going disapear
            self.display_text = False
            self.state_machine.change("play", level=self.level)

        #Fade out
        Timer.after(
                2,
                arrive_after
            )

    def render(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(
            self.screen_alpha_surface,
            (0, 0, 0, self.transition_alpha),
            (0,0),
            self.circle,
        )

        if self.display_text:
            render_text(
                self.screen_alpha_surface,
                f"Level {self.level}",
                settings.FONTS["medium"],
                settings.VIRTUAL_WIDTH / 2 - 50,
                settings.VIRTUAL_HEIGHT/ 2 - 10,
                (255, 255, 255),
                shadowed=False,
            )

        surface.blit(self.screen_alpha_surface, (0, 0))