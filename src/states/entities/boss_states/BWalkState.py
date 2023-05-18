"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

Author: Kevin Márquez
marquezberriosk@gmail.com

Author: Lewis Ochoa
lewis8a@gmail.com

This file contains the class BWalkState for Bosses.
"""

from numpy import random

from src.states.entities.BaseEntityState import BaseEntityState
from src.states.entities.IAEnemies import IAEnemies


class BWalkState(BaseEntityState, IAEnemies):
    def enter(self, flipped: bool) -> None:
        self.entity.change_animation("walk")
        self.entity.flipped = flipped
        self.entity.vx = -self.entity.walk_speed
        if not self.entity.flipped:
            self.entity.vx *= -1

    def update(self, dt: float) -> None:
        self.entity.wait_time -= dt
        if self.can_see_player() and self.entity.wait_time <= 0:
            self.entity.change_state("shoot", self.entity.flipped)
        else:
            p = random.rand()
            if 0 < p < 0.05:
                self.entity.change_state("idle", self.entity.flipped)
            else:
                if self.check_boundary():
                    self.entity.vx *= -1
                    self.entity.flipped = not self.entity.flipped