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
import settings

from typing import Dict, Any
from gale.animation import Animation
from gale.input_handler import InputData
from gale.state import BaseState
from gale.text import Text, render_text


class StartState(BaseState):

    def enter(self,**enter_params: Dict[str, Any]) -> None:
        # A surface that supports alpha for the screen
        self.screen_alpha_surface = pygame.Surface(
            (settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT), pygame.SRCALPHA
        )

        # Current Menu Select
        self.current_menu_item = 2

        # Play Menu Music
        pygame.mixer.music.load(settings.BASE_DIR / "assets/music/menu.ogg")
        pygame.mixer.music.play(loops=-1)

        # Set the volume for this sounds
        settings.SOUNDS["menu_select"].set_volume(0.3)
        settings.SOUNDS["menu_play"].set_volume(0.3)
        settings.SOUNDS["menu_enter"].set_volume(0.3)

    def render(self, surface: pygame.Surface) -> None:
        # Colored Background
        surface.fill((0, 0, 0))
        
        # Background
        background = pygame.transform.scale(settings.TEXTURES["background_0"],(settings.VIRTUAL_WIDTH,settings.VIRTUAL_HEIGHT))
        surface.blit(
            background,
            (0,
            0),
        )

        # Bynary Strike Logo
        logo = pygame.transform.scale(settings.TEXTURES["binary_strike"],(180,120))
        surface.blit(
            logo,
            (settings.VIRTUAL_WIDTH // 5,
            settings.VIRTUAL_HEIGHT // 16),
        )

        # Bar
        bar = pygame.transform.scale(settings.TEXTURES["bar"],(290,25))
        surface.blit(
            bar,
            (5,
            settings.VIRTUAL_HEIGHT // 1.34),
        )

        # Buttons
        if self.current_menu_item == 1:
            settings_btn = pygame.transform.scale(settings.TEXTURES["settings_btn_1"],(20,20))
            btn1_x = -48
            btn1_y = 50
            margin1 = 5
        else:
            settings_btn = pygame.transform.scale(settings.TEXTURES["settings_btn_0"],(13,13))
            btn1_x = -40
            btn1_y = 55
            margin1 = 0
        if self.current_menu_item == 2:
            play_btn = pygame.transform.scale(settings.TEXTURES["play_btn_1"],(20,20))
            btn2_x = -42
            btn2_y = 50
            margin2 = 5
        else:
            play_btn = pygame.transform.scale(settings.TEXTURES["play_btn_0"],(13,13))
            btn2_x = -30
            btn2_y = 55
            margin2 = 0
        if self.current_menu_item == 3:
            info_btn = pygame.transform.scale(settings.TEXTURES["info_btn_1"],(20,20))
            btn3_x = -45
            btn3_y = 50
            margin3 = 7
        else:
            info_btn = pygame.transform.scale(settings.TEXTURES["info_btn_0"],(13,13))
            btn3_x = -42
            btn3_y = 55
            margin3 = 0
        surface.blit(
                settings_btn,
                (settings.VIRTUAL_WIDTH // 5 + btn1_x,
                settings.VIRTUAL_HEIGHT // 2 + btn1_y),
            )
        surface.blit(
                play_btn,
                (settings.VIRTUAL_WIDTH // 1.9 + btn2_x,
                settings.VIRTUAL_HEIGHT // 2 + btn2_y),
            )
        surface.blit(
                info_btn,
                (settings.VIRTUAL_WIDTH // 1.2 + btn3_x,
                settings.VIRTUAL_HEIGHT // 2 + btn3_y),
            )

        # Text Options
        text_color = (
                (99, 155, 255, 255) if self.current_menu_item == 1 else (255, 255, 255, 255)
            )
        font_size = (
                settings.FONTS["title_small_medium"] if self.current_menu_item == 1 else settings.FONTS["title_small"]
            )
        render_text(
            surface,
            "Options",
            font_size,
            settings.VIRTUAL_WIDTH // 5 + margin1,
            settings.VIRTUAL_HEIGHT // 2 + 60,
            text_color,
            center = True,
            shadowed = True,
        )

        # Text Play
        text_color = (
                (99, 155, 255, 255) if self.current_menu_item == 2 else (255, 255, 255, 255)
            )
        font_size = (
                settings.FONTS["title_medium"] if self.current_menu_item == 2 else settings.FONTS["title_small"]
            )
        render_text(
            surface,
            "Play",
            font_size,
            settings.VIRTUAL_WIDTH // 1.9 + margin2,
            settings.VIRTUAL_HEIGHT // 2 + 60,
            text_color,
            center = True,
            shadowed = True,
        )

        # Text Credits
        text_color = (
                (99, 155, 255, 255) if self.current_menu_item == 3 else (255, 255, 255, 255)
            )
        font_size = (
                settings.FONTS["title_small_medium"] if self.current_menu_item == 3 else settings.FONTS["title_small"]
            )
        render_text(
            surface,
            "Credits",
            font_size,
            settings.VIRTUAL_WIDTH // 1.2 + margin3,
            settings.VIRTUAL_HEIGHT // 2 + 60,
            text_color,
            center = True,
            shadowed = True,
        )
    
    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id in ("move_left") and input_data.pressed:    
            if self.current_menu_item == 3:
                self.current_menu_item = 2
                settings.SOUNDS["menu_select"].stop()
                settings.SOUNDS["menu_select"].play()
            elif self.current_menu_item == 2:
                self.current_menu_item = 1
                settings.SOUNDS["menu_select"].stop()
                settings.SOUNDS["menu_select"].play()
            elif self.current_menu_item == 1:
                settings.SOUNDS["menu_change"].stop()
                settings.SOUNDS["menu_change"].play()
        if input_id in ("move_right") and input_data.pressed:
            if self.current_menu_item == 1:
                self.current_menu_item = 2
                settings.SOUNDS["menu_select"].stop()
                settings.SOUNDS["menu_select"].play()
            elif self.current_menu_item == 2:
                self.current_menu_item = 3
                settings.SOUNDS["menu_select"].stop()
                settings.SOUNDS["menu_select"].play()
            elif self.current_menu_item == 3:
                settings.SOUNDS["menu_change"].stop()
                settings.SOUNDS["menu_change"].play()
        elif input_id == "enter" and input_data.pressed:
            if self.current_menu_item == 1:
                settings.SOUNDS["menu_enter"].stop()
                settings.SOUNDS["menu_enter"].play()
                #self.state_machine.change("options")
            if self.current_menu_item == 2:
                settings.SOUNDS["menu_play"].stop()
                settings.SOUNDS["menu_play"].play()
                self.state_machine.change("color")
            if self.current_menu_item == 3:
                settings.SOUNDS["menu_enter"].stop()
                settings.SOUNDS["menu_enter"].play()
                self.state_machine.change("dialogue",previous="start",next="credits",part=1)