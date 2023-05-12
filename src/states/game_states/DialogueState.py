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
        # Basic settings
        self.display_text = True
        self.timeEnd = 0
        self.transition_alpha = 255
        self.oldState = enter_params.get("previous", "start")
        self.newState = enter_params.get("next", "start")
        self.part = enter_params.get("part", "1")
        
        # A surface that supports alpha for the screen
        self.screen_alpha_surface = pygame.Surface(
            (settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT), pygame.SRCALPHA
        )
        
        # Camera position
        self.camera = enter_params.get(
            "camera", Camera(0, 0, settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT)
        )

        # Set the volumne for this sounds
        settings.SOUNDS["menu_play"].set_volume(0.3)

        # Initial position and text to display
        if self.oldState == "init":
            self.dialogue = "intro"
            self.initY = 2.5
            self.margin = 40
            self.font1 = settings.FONTS["title_large"]
            self.font2 = settings.FONTS["title_medium"]
            self.font3 = settings.FONTS["title_medium"]
            settings.SOUNDS["menu_play"].stop()
            settings.SOUNDS["menu_play"].play()
            self.timeEnd = 1
        elif self.oldState == "start" and self.newState == "begin":
            self.dialogue = "predialogue"
            self.initY = 6.5
            self.margin = 25
            self.font1 = settings.FONTS["large"]
            self.font2 = settings.FONTS["text_small"]
            self.font3 = settings.FONTS["text_small"]
            self.timeEnd = 1
        elif self.oldState == "start" and self.newState == "credits":
            # Play Menu Music
            pygame.mixer.music.load(settings.BASE_DIR / "assets/music/credits.ogg")
            pygame.mixer.music.play(loops=-1)
            self.oldState = "credits"
            self.newState = "dialogue"
            self.dialogue = f"credits{self.part}"
            self.initY = 6.5
            self.margin = 25
            self.font1 = settings.FONTS["title_large"]
            self.font2 = settings.FONTS["text_medium_large"]
            self.font3 = settings.FONTS["small_medium"]
            self.timeEnd = 8
        elif self.oldState == "credits" and self.newState == "dialogue" and self.part < 11:
            self.oldState = "credits"
            if self.part == 10:
                self.newState = "start"
            else:
                self.newState = "dialogue"
            self.part = self.part + 1
            self.dialogue = f"credits{self.part}"
            self.initY = 6.5
            self.margin = 25
            self.font1 = settings.FONTS["title_large"]
            self.font2 = settings.FONTS["text_medium_large"]
            self.font3 = settings.FONTS["small_medium"]
            self.timeEnd = 8

        def arrive_after():
            # Then, animate the text going disapear
            self.display_text = False
            Timer.tween(
               0.5,
               [(self, {"transition_alpha": 0})],
               # We are ready to play
               on_finish=lambda: self.state_machine.change(
                   self.newState, previous = self.oldState, next = self.newState, part = self.part
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