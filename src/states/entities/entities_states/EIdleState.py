"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

Author: Kevin Márquez
marquezberriosk@gmail.com

This file contains the class IdleState for Entities.
"""
from numpy import random

from src.states.entities.BaseEntityState import BaseEntityState

class EIdleState(BaseEntityState):
    def enter(self, flipped: bool) -> None:
        self.entity.vx = 0
        self.entity.vy = 0
        self.entity.flipped = flipped
        self.entity.change_animation("idle")

    def exit(self) -> None:
        pass

    def update(self, dt: float) -> None:
        p = random.rand()
        if 0 < p < 0.3:
            self.entity.state_machine.change("walk", self.entity.flipped)
        elif 0.3 <= p < 0.5:
            print("Cambiando a shoot")
        elif 0.5 <= p <= 0.6:
            print("Persigo")
        else:
            p = random.rand()
            if 0.2 < p < 0.3:
                self.entity.flipped = not self.entity.flipped 
