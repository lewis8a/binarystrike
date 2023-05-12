"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

Author: Kevin Márquez
marquezberriosk@gmail.com

This file contains the class EShootState for Entities.
"""
from numpy import random, sqrt
from typing import Tuple
from src.states.entities.BaseEntityState import BaseEntityState
from src.states.entities.IAEnemies import IAEnemies
from src.definitions import enemies
from src.Projectile import Projectile

import settings


class EShootState(BaseEntityState, IAEnemies):
    def enter(self, flipped: bool) -> None:
        self.entity.vx = 0
        self.entity.vy = 0
        self.entity.flipped = flipped
        self.player = self.entity.game_level.player
        dif_x = self.player.x - self.entity.x
        if dif_x > 0 and self.entity.flipped:
            self.entity.flipped = not self.entity.flipped
        elif dif_x < 0 and not self.entity.flipped:
            self.entity.flipped = not self.entity.flipped
        self.entity.change_animation("shoot")

    def exit(self) -> None:
        pass

    def update(self, dt: float) -> None:
        if self.entity.frame_index >= 2:
            self.entity.wait_time = self.entity.time_to_rest
            randomJumpSound = random.randint(1,4)
            settings.SOUNDS[f"gun{randomJumpSound}"].stop()
            settings.SOUNDS[f"gun{randomJumpSound}"].play()
            vx, vy = self.speed_to_shoot()
            bullet = Projectile(self.entity.x,
                                self.entity.y + self.entity.height/3,
                                5, 5, vx, vy,
                                settings.TEXTURES["bullet_enemy"], self.entity.game_level.camera)
            self.entity.game_level.enemies_bullets.append(bullet)

            p = random.rand()
            if p < 0.3:
                self.entity.change_state("idle", self.entity.flipped)
            else:
                self.entity.vx = enemies.Enemies[379]["walk_speed"]
                self.entity.change_state("walk", self.entity.flipped)

    def speed_to_shoot(self) -> Tuple[int, int]:
        px = self.player.x + self.player.width/2
        py = self.player.y + self.player.height/2

        ex = self.entity.x + self.entity.width/3
        ey = self.entity.y + self.entity.height/3

        dif_x = px - ex
        dif_y = py - ey
        return (dif_x*1.25, dif_y*1.15)
