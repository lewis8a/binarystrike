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

        self.state = enter_params.get("ss")
        self.counter = 3
        self.x_live = 7
        self.y_live = 20

        if self.state.player.touch_boss:
            self.state.player.lives -= 5
            self.state.player.touch_boss = False
        else:
            self.state.player.lives -= 1

        if self.state.player.lives <= 0:
            self.state_machine.change(
                "end",
                score=self.state.player.score,
                level=self.state.level
            )
        else:
            def final_call():
                self.state.player.change_state("idle")
                self.state_machine.change(
                    "play",
                    ss=self.state
                )

            def back_count_1():
                # Entry sound
                self.counter = "Go!"
                Timer.after(0.35,final_call)

            def back_count_2():
                # Entry sound
                self.counter -= 1
                Timer.after(0.35,back_count_1)

            def back_count_3():
                # Entry sound
                self.counter -= 1
                Timer.after(0.35,back_count_2)

            def entry_arrive():
                self.finish_tween = True
                settings.SOUNDS["reborn"].stop()
                if settings.SOUND:
                    settings.SOUNDS["reborn"].play()

                Timer.after(0.3, back_count_3)

            Timer.tween(
                1,
                [
                    (self, {"transition_alpha": 175}),
                    (self, {"circle": max(settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)})
                ],
                on_finish=entry_arrive
            )

    def exit(self) -> None:
        x, y = self.state.player.last_floor_position
        self.state.player.vy = 0
        self.state.player.vx = 0
        self.state.player.y = y
        self.state.player.x = x
        self.state.player.go_invulnerable()

    def render(self, surface: pygame.Surface) -> None:
        world_surface = pygame.Surface((self.state.tilemap.width, self.state.tilemap.height))
        self.state.game_level.render(world_surface)
        for bullet in self.state.player.bullets:
            bullet.render(world_surface)
        
        surface.blit(world_surface, (-self.state.camera.x, -self.state.camera.y))

        render_text(
            surface,
            f"Score: {self.state.player.score}",
            settings.FONTS["xs"],
            5,
            5,
            (255, 255, 255),
            shadowed=True,
        )

        render_text(
            surface,
            f"Time: {self.state.timer}",
            settings.FONTS["xs"],
            settings.VIRTUAL_WIDTH - 50,
            5,
            (255, 255, 255),
            shadowed=True,
        )

        stop = min(8, self.state.player.lives)
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