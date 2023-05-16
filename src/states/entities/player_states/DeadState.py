"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

Author: Kevin Márquez
marquezberriosk@gmail.com

Author: Lewis Ochoa
lewis8a@gmail.com

This file contains the class DeadState for player.
"""

import pygame
import settings

from numpy import random

from gale.timer import Timer

from src.states.entities.BaseEntityState import BaseEntityState


class DeadState(BaseEntityState):
    def enter(self) -> None:
        # Play sound player die
        randomJumpSound = random.randint(1,3)
        settings.SOUNDS[f"death{randomJumpSound}"].set_volume(0.4)
        settings.SOUNDS[f"death{randomJumpSound}"].stop()
        settings.SOUNDS[f"death{randomJumpSound}"].play()
        self.finish = False

        def arrive() -> None:
            self.finish = True
        
        Timer.after(0.75, arrive)
        
        self.entity.change_animation("dead")
        self.entity.is_dead = True
        self.entity.vx = 0
        self.entity.vy = 0
    
    def update(self, dt: float) -> None:
        if self.finish:
            self.entity.change_state("fall")
    
    def exit(self) -> None:
        x, y = self.entity.last_floor_position
        self.entity.y = y - settings.TILE_SIZE * 1.5
        self.entity.x = x
        self.entity.vy = -10
        self.entity.is_dead = False
    
    def render(self, surface: pygame.Surface) -> None:
        pass