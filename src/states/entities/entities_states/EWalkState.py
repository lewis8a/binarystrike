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
        print("Entrando en walk")
        self.entity.change_animation("walk")
        self.entity.flipped = flipped
        self.entity.vx = -self.entity.walk_speed
        if not self.entity.flipped:
            self.entity.vx *= -1

    def update(self, dt: float) -> None:
        p = random.rand()
        if 0 < p < 0.05:
            print("Cambiando a Iddle")
            self.entity.state_machine.change("idle", self.entity.flipped)
        else:
            if self.check_boundary():
                self.entity.vx *= -1
                self.entity.flipped = not self.entity.flipped
