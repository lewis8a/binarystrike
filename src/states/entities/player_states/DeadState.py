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

from typing import Dict, Any
from numpy import random

from gale.timer import Timer

from src.states.entities.BaseEntityState import BaseEntityState


class DeadState(BaseEntityState):
    def enter(self, **enter_params: Dict[str, Any]) -> None:
        self.on_finish = enter_params.get("on_finish")
        randomJumpSound = random.randint(1,3)
        settings.SOUNDS[f"death{randomJumpSound}"].set_volume(0.4)
        settings.SOUNDS[f"death{randomJumpSound}"].stop()
        settings.SOUNDS[f"death{randomJumpSound}"].play()
        self.finish = False
        self.entity.is_dead = False
        self.entity.vx = 0
        self.entity.vy = 0

        if self.entity.y >= self.entity.tilemap.height:
            self.on_finish()
        else:            
            Timer.after(0.65, self.on_finish)
            
            self.entity.change_animation("dead")
    
    def exit(self) -> None:
        Timer.clear()
        x, y = self.entity.last_floor_position
        self.entity.y = y
        self.entity.x = x
        self.entity.go_invulnerable()
    
    def render(self, surface: pygame.Surface) -> None:
        pass