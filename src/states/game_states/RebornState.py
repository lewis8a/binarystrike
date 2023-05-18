"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Kevin Márquez
marquezberriosk@gmail.com

Author: Lewis Ochoa
lewis8a@gmail.com

This file contains the class RebornState.
"""
from typing import Dict, Any

import pygame

from gale.state import BaseState
from gale.text import render_text
from gale.timer import Timer

import settings


class RebornState(BaseState):
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
        self.counter = 3
        self.x_live = 7
        self.y_live = 20

        if self.player.touch_boss:
            self.player.lives -= 5
            self.player.touch_boss = False
        else:
            self.player.lives -= 1

        if self.player.lives <= 0:
            self.state_machine.change(
                "end",
                score=self.player.score,
                level=self.level
            )
        else:
            def final_arrive():
                
                self.player.change_state("idle")

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

            def back_count_1():
                # Entry sound
                self.counter -= 1

                Timer.after(0.35,final_arrive)

            def back_count_2():
                # Entry sound
                self.counter -= 1

                Timer.after(0.35,back_count_1)

            def entry_arrive():
                self.finish_tween = True
                settings.SOUNDS["reborn"].stop()
                if settings.SOUND:
                    settings.SOUNDS["reborn"].play()

                Timer.after(0.3, back_count_2)

            Timer.tween(
                1,
                [
                    (self, {"transition_alpha": 175}),
                    (self, {"circle": max(settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)})
                ],
                on_finish=entry_arrive
            )

    def render(self, surface: pygame.Surface) -> None:
        world_surface = pygame.Surface((self.tilemap.width, self.tilemap.height))
        self.game_level.render(world_surface)
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
            settings.VIRTUAL_WIDTH - 50,
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
                f"{self.counter}",
                settings.FONTS["title_medium"],
                settings.VIRTUAL_WIDTH/2 - 5,
                settings.VIRTUAL_HEIGHT/2 - 5,
                (255, 255, 255),
                shadowed=True,
            )

        surface.blit(self.screen_alpha_surface, (0, 0)) 