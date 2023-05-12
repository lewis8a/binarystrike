"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Kevin Márquez
marquezberriosk@gmail.com

Author: Lewis Ochoa
lewis8a@gmail.com

This file contains the class Projectile.
"""

from typing import Any

import pygame
import settings

from src.Camera import Camera

class Projectile:
    def __init__(self, x: int, y: int, w: int, h: int,
                 vx: int, vy: int, texture, camera: Camera) -> None:
        self.x = x
        self.y = y
        self.width = w
        self.height = h

        self.vx = vx
        self.vy = vy
        
        self.camera = camera

        self.texture = texture
        self.frame = 0
        self.in_play = True

    def get_collision_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def collides(self, another: Any) -> bool:
        return self.get_collision_rect().colliderect(another.get_collision_rect())

    def update(self, dt: float) -> None:
        if self.in_play:
            r = self.get_collision_rect()
            if r.right < self.camera.x or r.bottom < self.camera.y or r.top > self.camera.y + self.camera.height or r.left > self.camera.x + self.camera.width:
                self.in_play = False
            self.x += self.vx * dt
            self.y += self.vy * dt

    def render(self, surface):
        surface.blit(self.texture, (self.x, self.y))