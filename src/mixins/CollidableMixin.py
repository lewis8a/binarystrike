"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

Author: Kevin Márquez
marquezberriosk@gmail.com

Author: Lewis Ochoa
lewis8a@gmail.com

This file contains the CollidableMixin.
"""
from typing import Any

import pygame

class CollidableMixin:
    def get_collision_rect(self) -> pygame.Rect:
        pl_x = getattr(self, "padding_x_left", 0)
        pr_x = getattr(self, "padding_x_right", 0)
        pu_y = getattr(self, "padding_y_up", 0)
        pd_y = getattr(self, "padding_y_down", 0)
        return pygame.Rect(self.x + pl_x, self.y + pu_y, self.width - pr_x, self.height - pd_y)

    def collides(self, another: Any) -> bool:
        return self.get_collision_rect().colliderect(another.get_collision_rect())
