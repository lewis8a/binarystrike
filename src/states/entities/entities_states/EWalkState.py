"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class EWalkState.
"""

from numpy import random

from src.states.entities.BaseEntityState import BaseEntityState
from src.states.entities.IAEnemies import IAEnemies


class EWalkState(BaseEntityState, IAEnemies):
    def enter(self, flipped: bool) -> None:
        self.entity.change_animation("walk")
        self.entity.flipped = flipped
        self.entity.vx = -self.entity.walk_speed
        if not self.entity.flipped:
            self.entity.vx *= -1

    def update(self, dt: float) -> None:
        p = random.rand()
        if 0 < p < 0.05:
            self.entity.change_state("idle", self.entity.flipped)
        if 0.1 < p < 4:
            self.entity.change_state("shoot", self.entity.flipped)
        else:
            if self.check_boundary():
                self.entity.vx *= -1
                self.entity.flipped = not self.entity.flipped
