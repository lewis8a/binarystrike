"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Kevin Márquez
marquezberriosk@gmail.com

Author: Lewis Ochoa
lewis8a@gmail.com

This file contains the class SettingState.
"""
import pygame
import settings

from typing import Dict, Any
from gale.animation import Animation
from gale.input_handler import InputData
from gale.state import BaseState
from gale.text import Text, render_text
from gale.timer import Timer


class SettingState(BaseState):

    def enter(self,**enter_params: Dict[str, Any]) -> None:
        # A surface that supports alpha for the screen
        self.screen_alpha_surface = pygame.Surface(
            (settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT), pygame.SRCALPHA
        )

        # Current Menu Select
        self.current_menu_item = 1

        # Current Button Select
        self.select_menu_item = 0

        #Current Settings
        self.music_menu_item = settings.MUSIC
        self.sound_menu_item = settings.SOUND

        # Set the volume for this sounds
        settings.SOUNDS["menu_change"].set_volume(0.3)
        settings.SOUNDS["menu_select"].set_volume(0.3)
        settings.SOUNDS["menu_return"].set_volume(0.3)

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
        window = pygame.transform.scale(settings.TEXTURES["window_2"],(180,170))
        surface.blit(
            window,
            (settings.VIRTUAL_WIDTH // 5,
            settings.VIRTUAL_HEIGHT // 16),
        )

        # Title
        render_text(
            surface,
            "Settings",
            settings.FONTS["title_small"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT // 8.5,
            (255, 255, 255, 255),
            center = True,
            shadowed = True,
        )

        # Buttons
        if self.select_menu_item < 0:
            backward_btn = pygame.transform.scale(settings.TEXTURES["backward_btn_1"],(20,20))
        else:
            backward_btn = pygame.transform.scale(settings.TEXTURES["backward_btn_0"],(20,20))
        if self.select_menu_item > 0:
            forward_btn = pygame.transform.scale(settings.TEXTURES["forward_btn_1"],(20,20))
        else:
            forward_btn = pygame.transform.scale(settings.TEXTURES["forward_btn_0"],(20,20))
        
        if self.current_menu_item == 1:
            surface.blit(
                backward_btn,
                (settings.VIRTUAL_WIDTH // 4.3,
                settings.VIRTUAL_HEIGHT // 5.3),
            )
            surface.blit(
                forward_btn,
                (settings.VIRTUAL_WIDTH // 1.5,
                settings.VIRTUAL_HEIGHT // 5.3),
            )
        if self.current_menu_item == 2:
            surface.blit(
                backward_btn,
                (settings.VIRTUAL_WIDTH // 4.3,
                settings.VIRTUAL_HEIGHT // 3),
            )
            surface.blit(
                forward_btn,
                (settings.VIRTUAL_WIDTH // 1.5,
                settings.VIRTUAL_HEIGHT // 3),
            )
        if self.current_menu_item == 3:
            surface.blit(
                backward_btn,
                (settings.VIRTUAL_WIDTH // 4.3,
                settings.VIRTUAL_HEIGHT // 2.1),
            )
            surface.blit(
                forward_btn,
                (settings.VIRTUAL_WIDTH // 1.5,
                settings.VIRTUAL_HEIGHT // 2.1),
            )
        if self.current_menu_item == 4:
            surface.blit(
                backward_btn,
                (settings.VIRTUAL_WIDTH // 4.3,
                settings.VIRTUAL_HEIGHT // 1.6),
            )
            surface.blit(
                forward_btn,
                (settings.VIRTUAL_WIDTH // 1.5,
                settings.VIRTUAL_HEIGHT // 1.6),
            )

        # Bar
        surface.blit(
            pygame.transform.scale(settings.TEXTURES["bar_2"],(100,25)),
            (settings.VIRTUAL_WIDTH // 3,
            settings.VIRTUAL_HEIGHT // 1.3),
        )

        # Text Options
        text_color = (
                (99, 155, 255, 255) if self.current_menu_item == 5 else (255, 255, 255, 255)
            )
        text_music = (
                "ON" if settings.MUSIC else "OFF"
            )
        text_sound = (
                "ON" if settings.SOUND else "OFF"
            )

        # Text
        render_text(
            surface,
            "Back",
            settings.FONTS["title_small"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT // 1.22,
            text_color,
            center = True,
            shadowed = True,
        )

        render_text(
            surface,
            text_music,
            settings.FONTS["title_medium"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT // 4.5,
            (255, 255, 255, 255),
            center = True,
            shadowed = True,
        )

        render_text(
            surface,
            text_sound,
            settings.FONTS["title_medium"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT // 2.7,
            (255, 255, 255, 255),
            center = True,
            shadowed = True,
        )

        render_text(
            surface,
            f"Gravity  {settings.GRAVITY}",
            settings.FONTS["title_small"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT // 1.9,
            (255, 255, 255, 255),
            center = True,
            shadowed = True,
        )

        # Icons
        if self.music_menu_item:
            music_btn = pygame.transform.scale(settings.TEXTURES["music_btn_1"],(20,20))
        else:
            music_btn = pygame.transform.scale(settings.TEXTURES["music_btn_0"],(20,20))
        if self.sound_menu_item:
            sound_btn = pygame.transform.scale(settings.TEXTURES["sound_btn_1"],(20,20))
        else:
            sound_btn = pygame.transform.scale(settings.TEXTURES["sound_btn_0"],(20,20))

        surface.blit(
            music_btn,
            (settings.VIRTUAL_WIDTH // 3,
            settings.VIRTUAL_HEIGHT // 5.5),
        )

        surface.blit(
            sound_btn,
            (settings.VIRTUAL_WIDTH // 3,
            settings.VIRTUAL_HEIGHT // 3),
        )

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id in ("move_left") and input_data.pressed:    
            self.select_menu_item = -1
            settings.SOUNDS["menu_change"].stop()
            if settings.SOUND:
                settings.SOUNDS["menu_change"].play()
            self.switch()
            Timer.tween(
                0.2,
                [(self, {"select_menu_item": 0})],
            )
        if input_id in ("move_right") and input_data.pressed:
            self.select_menu_item = 1
            settings.SOUNDS["menu_change"].stop()
            if settings.SOUND:
                settings.SOUNDS["menu_change"].play()
            self.switch()
            Timer.tween(
                0.2,
                [(self, {"select_menu_item": 0})],
            )
        if input_id in ("look_down") and input_data.pressed:
            if self.current_menu_item < 5:
                self.current_menu_item = self.current_menu_item + 1
            settings.SOUNDS["menu_select"].stop()
            if settings.SOUND:
                settings.SOUNDS["menu_select"].play()
        
        if input_id in ("look_up") and input_data.pressed:
            if self.current_menu_item > 1:
                self.current_menu_item = self.current_menu_item - 1
            settings.SOUNDS["menu_select"].stop()
            if settings.SOUND:
                settings.SOUNDS["menu_select"].play()
        
        if input_id == "enter" and input_data.pressed and self.current_menu_item == 5:
            self.state_machine.change("start")
    
    def switch (self) -> None:
        if self.current_menu_item == 1:
            if self.music_menu_item:
                self.music_menu_item = 0
                settings.MUSIC = 0
                # Stop music and unload
                pygame.mixer.music.unload()
                pygame.mixer.music.stop()
            else:
                self.music_menu_item = 1
                settings.MUSIC = 1
                # Play music
                pygame.mixer.music.load(settings.BASE_DIR / "assets/music/menu.ogg")
                pygame.mixer.music.play(loops=-1)
        if self.current_menu_item == 2:
            if self.sound_menu_item:
                self.sound_menu_item = 0
                settings.SOUND = 0
            else:
                self.sound_menu_item = 1
                settings.SOUND = 1
        if self.current_menu_item == 3:
            if settings.GRAVITY > 50 and self.select_menu_item < 1:
                settings.GRAVITY = settings.GRAVITY - 50
            if settings.GRAVITY < 10000 and self.select_menu_item > 0:
                settings.GRAVITY = settings.GRAVITY + 50
