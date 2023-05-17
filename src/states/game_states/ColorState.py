"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Kevin Márquez
marquezberriosk@gmail.com

Author: Lewis Ochoa
lewis8a@gmail.com

This file contains the class ColorState.
"""
import pygame
import settings

from typing import Dict, Any
from gale.animation import Animation
from gale.input_handler import InputData
from gale.state import BaseState
from gale.text import Text, render_text
from gale.timer import Timer


class ColorState(BaseState):

    def enter(self,**enter_params: Dict[str, Any]) -> None:
        # A surface that supports alpha for the screen
        self.screen_alpha_surface = pygame.Surface(
            (settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT), pygame.SRCALPHA
        )

        # Current Menu Select
        self.current_menu_item = 2

        # Current color
        self.current_color = 1

        # Set the volume for this sounds
        settings.SOUNDS["menu_character"].set_volume(0.3)
        settings.SOUNDS["menu_play"].set_volume(0.3)

        #Khan texture
        self.khan_texture = settings.TEXTURES[f"khan{self.current_color}"]
        self.khan_animation = Animation(settings.FRAMES[f"khan{self.current_color}"][2:25], 0.06)

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
        
        # Window
        window = pygame.transform.scale(settings.TEXTURES["window"],(180,170))
        surface.blit(
            window,
            (settings.VIRTUAL_WIDTH // 5,
            settings.VIRTUAL_HEIGHT // 16),
        )

        # Title
        render_text(
            surface,
            "Select your favorite color",
            settings.FONTS["title_xs"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT // 5.5,
            (255, 255, 255, 255),
            center = True,
            shadowed = True,
        )

        # Buttons
        if self.current_menu_item < 2:
            backward_btn = pygame.transform.scale(settings.TEXTURES["backward_btn_1"],(20,20))
        else:
            backward_btn = pygame.transform.scale(settings.TEXTURES["backward_btn_0"],(20,20))
        if self.current_menu_item == 2:
            ok_btn = pygame.transform.scale(settings.TEXTURES["ok_btn_1"],(25,25))
        else:
            ok_btn = pygame.transform.scale(settings.TEXTURES["ok_btn_0"],(25,25))
        if self.current_menu_item > 2:
            forward_btn = pygame.transform.scale(settings.TEXTURES["forward_btn_1"],(20,20))
        else:
            forward_btn = pygame.transform.scale(settings.TEXTURES["forward_btn_0"],(20,20))
        surface.blit(
                backward_btn,
                (settings.VIRTUAL_WIDTH // 4.5,
                settings.VIRTUAL_HEIGHT // 2),
            )
        surface.blit(
                ok_btn,
                (settings.VIRTUAL_WIDTH // 2.15,
                settings.VIRTUAL_HEIGHT // 1.3),
            )
        surface.blit(
                forward_btn,
                (settings.VIRTUAL_WIDTH // 1.4,
                settings.VIRTUAL_HEIGHT // 2),
            )
        #Khan texture
        self.khan_texture = settings.TEXTURES[f"khan{self.current_color}"]
        
        #Khan
        surface.blit(
            self.khan_texture,
            (settings.VIRTUAL_WIDTH // 2.15, settings.VIRTUAL_HEIGHT // 2.3),
            self.khan_animation.get_current_frame(),
        )
    
    def update(self, dt: float) -> None:
        self.khan_animation.update(dt)

    def exit(self) -> None:
        # Stop Menu Music nad unload
        if settings.MUSIC:
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id in ("move_left") and input_data.pressed:    
            self.current_menu_item = 1
            if self.current_color > 1:
                self.current_color = self.current_color - 1
            else:
                self.current_color = 10
            settings.SOUNDS["menu_character"].stop()
            if settings.SOUND:
                settings.SOUNDS["menu_character"].play()
            Timer.tween(
                0.2,
                [(self, {"current_menu_item": 2})],
            )
        if input_id in ("move_right") and input_data.pressed:
            self.current_menu_item = 3
            if self.current_color < 10:
                self.current_color = self.current_color + 1
            else:
                self.current_color = 1
            settings.SOUNDS["menu_character"].stop()
            if settings.SOUND:
                settings.SOUNDS["menu_character"].play()
            Timer.tween(
                0.2,
                [(self, {"current_menu_item": 2})],
            )
        elif input_id == "enter" and input_data.pressed:
            settings.SOUNDS["menu_play"].stop()
            if settings.SOUND:
                settings.SOUNDS["menu_play"].play()
            settings.PLAYER_COLOR = self.current_color
            self.state_machine.change("dialogue",previous="start",next="begin")