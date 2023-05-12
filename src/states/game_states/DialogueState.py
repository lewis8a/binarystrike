"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Kevin Márquez
marquezberriosk@gmail.com

Author: Lewis Ochoa
lewis8a@gmail.com

This file contains the class DialogueState.
"""
from typing import Dict, Any

import pygame

from gale.state import BaseState
from gale.text import render_text
from gale.timer import Timer

import settings
from src.Player import Player
from src.Camera import Camera
from src.GameLevel import GameLevel


class DialogueState(BaseState):
    def enter(self, **enter_params: Dict[str, Any]) -> None:
        self.display_text = True
        self.transition_alpha = 255
        self.oldState = enter_params.get("previous", "start")
        self.newState = enter_params.get("next", "start")

        # A surface that supports alpha for the screen
        self.screen_alpha_surface = pygame.Surface(
            (settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT), pygame.SRCALPHA
        )
        
        # Camera position
        self.camera = enter_params.get(
            "camera", Camera(0, 0, settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT)
        )

        # Initial position and text to display
        if self.oldState == "init":
            self.dialogue = "intro"
            self.initY = 2.5
            self.margin = 40
            self.font1 = settings.FONTS["title_large"]
            self.font2 = settings.FONTS["title_medium"]
            self.font3 = settings.FONTS["title_medium"]
            self.timeEnd = 1
        if self.oldState == "start" and self.newState == "begin":
            self.dialogue = "predialogue"
            self.initY = 6.5
            self.margin = 25
            self.font1 = settings.FONTS["large"]
            self.font2 = settings.FONTS["text_small"]
            self.font3 = settings.FONTS["text_small"]
            self.timeEnd = 2

        def arrive_after():
            # Then, animate the text going disapear
            self.display_text = False
            Timer.tween(
               0.5,
               [(self, {"transition_alpha": 0})],
               # We are ready to play
               on_finish=lambda: self.state_machine.change(
                   self.newState,
               ),
            )

        #Fade out
        Timer.after(
                self.timeEnd,
                arrive_after
            )

    def render(self, surface: pygame.Surface) -> None:
        if self.display_text:
            render_text(
                self.screen_alpha_surface,
                settings.DIALOGUE[f"{self.dialogue}_0"],
                self.font1,
                settings.VIRTUAL_WIDTH / 2,
                settings.VIRTUAL_HEIGHT/ self.initY,
                (255, 255, 255),
                shadowed=True,
                center=True,
            )

            render_text(
                self.screen_alpha_surface,
                settings.DIALOGUE[f"{self.dialogue}_1"],
                self.font2,
                settings.VIRTUAL_WIDTH / 2,
                settings.VIRTUAL_HEIGHT/ self.initY + self.margin * 1,
                (255, 255, 255),
                shadowed=True,
                center=True,
            )

            render_text(
                self.screen_alpha_surface,
                settings.DIALOGUE[f"{self.dialogue}_2"],
                self.font3,
                settings.VIRTUAL_WIDTH / 2,
                settings.VIRTUAL_HEIGHT/ self.initY + self.margin * 2,
                (255, 255, 255),
                shadowed=True,
                center=True,
            )

            render_text(
                self.screen_alpha_surface,
                settings.DIALOGUE[f"{self.dialogue}_3"],
                self.font3,
                settings.VIRTUAL_WIDTH / 2,
                settings.VIRTUAL_HEIGHT/ self.initY + self.margin * 3,
                (255, 255, 255),
                shadowed=True,
                center=True,
            )

            render_text(
                self.screen_alpha_surface,
                settings.DIALOGUE[f"{self.dialogue}_4"],
                self.font3,
                settings.VIRTUAL_WIDTH / 2,
                settings.VIRTUAL_HEIGHT/ self.initY + self.margin * 4,
                (255, 255, 255),
                shadowed=True,
                center=True,
            )

            render_text(
                self.screen_alpha_surface,
                settings.DIALOGUE[f"{self.dialogue}_5"],
                self.font3,
                settings.VIRTUAL_WIDTH / 2,
                settings.VIRTUAL_HEIGHT/ self.initY + self.margin * 5,
                (255, 255, 255),
                shadowed=True,
                center=True,
            )

        surface.blit(self.screen_alpha_surface, (0, 0))