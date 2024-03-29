"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

Author: Kevin Márquez
marquezberriosk@gmail.com

Author: Lewis Ochoa
lewis8a@gmail.com

This file contains the class BDeadState for Bosses.
"""

import pygame
import settings

from numpy import random

from gale.timer import Timer

from src.states.entities.BaseEntityState import BaseEntityState


class BDeadState(BaseEntityState):
    def enter(self) -> None:
        self.entity.collidable = False
        # Play sound enemy die
        randomJumpSound = random.randint(4,8)
        settings.SOUNDS[f"death{randomJumpSound}"].set_volume(0.4)
        settings.SOUNDS[f"death{randomJumpSound}"].stop()
        if settings.SOUND:
            settings.SOUNDS[f"death{randomJumpSound}"].play()
        self.finish = False
        def arrive() -> None:
            self.finish = True
        
        len_frames = len(self.entity.animations["dead"].frames) / 10
        Timer.after(len_frames, arrive)
        
        self.entity.change_animation("dead")
        self.entity.vx = 0
        self.entity.vy = 0
    
    def update(self, dt: float) -> None:
        if self.finish:
            self.entity.is_dead = True
    
    def render(self, surface: pygame.Surface) -> None:
        pass