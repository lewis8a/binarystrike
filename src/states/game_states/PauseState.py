"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Kevin Márquez
marquezberriosk@gmail.com

Author: Lewis Ochoa
lewis8a@gmail.com

This file contains the class PauseState.
"""
from typing import Dict, Any

import pygame

from gale.input_handler import InputHandler, InputData
from gale.state import BaseState
from gale.text import render_text
from gale.timer import Timer

import settings


class PauseState(BaseState):
    def enter(self, **enter_params: Dict[str, Any]) -> None:
        self.finish_tween = False
        self.circle = 0
        self.transition_alpha = 0
        # A surface that supports alpha for the screen
        self.screen_alpha_surface = pygame.Surface(
            (settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT), pygame.SRCALPHA
        )        
        
        self.timer = enter_params.get("timer")
        self.level = enter_params.get("level")
        self.camera = enter_params.get("camera")
        self.game_level = enter_params.get("game_level")
        self.bullets = enter_params.get("bullets")
        self.pos_music = enter_params.get("pos_music")
        self.player = self.game_level.player
        self.tilemap = self.game_level.tilemap
        
        if type(self.player.state_machine.current).__name__ == "WalkState":
            self.player.change_state("idle")
        # Avoid entries
        InputHandler.unregister_listener(self.player.state_machine.current)

        # Entry sound
        settings.SOUNDS["menu_play"].stop()
        settings.SOUNDS["menu_play"].play()
        # Pause music
        pygame.mixer.music.load(settings.BASE_DIR / "assets/music/pause.ogg")
        pygame.mixer.music.set_volume(0.8)
        pygame.mixer.music.play(loops=-1)

        def arrive():
            self.finish_tween = True

        Timer.tween(
            1,
            [
                (self, {"transition_alpha": 175}),
                (self, {"circle": max(settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)})
            ],
            on_finish=arrive
        )

        self.x_live = 7
        self.y_live = 20

    def exit(self) -> None:
        # Registering for entries
        InputHandler.register_listener(self.player.state_machine.current)

        # Stop music
        pygame.mixer.music.unload()
        pygame.mixer.music.stop()
        # Exit sound
        settings.SOUNDS["menu_play"].stop()
        settings.SOUNDS["menu_play"].play()

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
            settings.FONTS["xs"],
            5,
            5,
            (255, 255, 255),
            shadowed=True,
        )

        render_text(
            surface,
            f"Time: {self.timer}",
            settings.FONTS["xs"],
            settings.VIRTUAL_WIDTH - 80,
            5,
            (255, 255, 255),
            shadowed=True,
        )

        stop = min(8, self.player.lives)
        for i in range(0, stop):
            surface.blit(settings.TEXTURES["lives"],
                         (self.x_live + self.x_live*i, self.y_live))

        pygame.draw.circle(
            self.screen_alpha_surface,
            (0, 0, 0, self.transition_alpha),
            (settings.WINDOW_WIDTH / 2, settings.WINDOW_HEIGHT / 2),
            self.circle,
        )

        if self.finish_tween:
            render_text(
                self.screen_alpha_surface,
                "Pause",
                settings.FONTS["title_medium"],
                settings.VIRTUAL_WIDTH/2 - 25,
                settings.VIRTUAL_HEIGHT/2 - 10,
                (255, 255, 255),
                shadowed=True,
            )

            render_text(
                self.screen_alpha_surface,
                f"Level {self.level}",
                settings.FONTS["title_small"],
                settings.VIRTUAL_WIDTH/2 - 20,
                settings.VIRTUAL_HEIGHT/2 + 10,
                (255, 255, 255),
                shadowed=True,
            )

        surface.blit(self.screen_alpha_surface, (0, 0))

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "pause" and input_data.pressed and self.finish_tween:
            self.state_machine.change(
                "play",
                player=self.player,
                timer=self.timer,
                level=self.level,
                camera=self.camera,
                game_level=self.game_level,
                bullets=self.bullets,
                pos_music = self.pos_music
            )
