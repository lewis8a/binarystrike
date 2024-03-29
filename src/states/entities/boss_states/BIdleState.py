"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

Author: Kevin Márquez
marquezberriosk@gmail.com

Author: Lewis Ochoa
lewis8a@gmail.com

This file contains the class BIdleState for Bosses.
"""
from numpy import random

from src.states.entities.BaseEntityState import BaseEntityState
from src.states.entities.IAEnemies import IAEnemies
from src.definitions import enemies


class BIdleState(BaseEntityState, IAEnemies):
    def enter(self, flipped: bool) -> None:
        self.entity.vx = 0
        self.entity.vy = 0
        self.entity.flipped = flipped
        self.entity.change_animation("idle")

    def exit(self) -> None:
        pass

    def update(self, dt: float) -> None:
        self.entity.wait_time -= dt
        if self.can_see_player() and self.entity.wait_time <= 0:
            self.entity.change_state("shoot", self.entity.flipped)
        else:
            p = random.rand()
            if p < 0.05:
                self.entity.vx = enemies.Enemies[1]["walk_speed"]
                self.entity.change_state("walk", self.entity.flipped)
            else:
                p = random.rand()
                if 0.1 < p < 0.125:
                    self.entity.flipped = not self.entity.flipped 
