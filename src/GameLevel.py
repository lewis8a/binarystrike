"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

Author: Kevin Márquez
marquezberriosk@gmail.com

Author: Lewis Ochoa
lewis8a@gmail.com

This file contains the class GameLevel.
"""

from typing import Any, Dict
from numpy import sqrt

import pygame

import settings
from src.Camera import Camera
from src.Enemy import Enemy
from src.Boss import Boss
from src.GamePowerup import GamePowerup
from src.GameBox import GameBox
from src.definitions import enemies, items


class GameLevel:
    def __init__(self, num_level: int, camera: Camera) -> None:
        self.tilemap = None
        self.enemies = []
        self.boss = None
        self.enemies_bullets = []
        self.items = []
        self.camera = camera
        self.player = None
        settings.LevelLoader().load(self, settings.TILEMAPS[num_level], num_level)

    def add_item(self, item_data: Dict[str, Any]) -> None:
        definition = items.ITEMS[item_data["item_name"]][item_data["frame_index"]]
        definition.update(item_data)
        if item_data["item_name"] == "boxpowerup":
            item = GameBox(**definition)
        elif item_data["item_name"] == "key":
            item = GamePowerup(**definition)
            
        self.items.append(item)
    
    def link_key_to_box(self) -> None:
        for box in self.items:
            if not isinstance(box, GameBox):
                continue
            
            for powerup in self.items:
                if not isinstance(powerup, GamePowerup):
                    continue
                if powerup.x == box.x:
                    box.powerup = powerup
                    powerup.box = box
                    break

    def add_enemy(self, Enemy_data: Dict[str, Any]) -> None:
        definition = enemies.Enemies[Enemy_data["tile_index"]]
        self.enemies.append(
            Enemy(
                Enemy_data["x"],
                Enemy_data["y"],
                Enemy_data["width"],
                Enemy_data["height"],
                self,
                **definition,
            )
        )
    
    def add_boss(self, Enemy_data: Dict[str, Any]) -> None:
        definition = enemies.Enemies[Enemy_data["tile_index"]]
        self.boss = Boss(
                Enemy_data["x"],
                Enemy_data["y"],
                self,
                **definition,
            )

    def update(self, dt: float) -> None:
        self.tilemap.set_render_boundaries(self.camera.get_rect())

        for i in range(len(self.items) - 1, -1, -1):
            self.items[i].update(dt)
            if not self.items[i].in_play:
                if self.items[i].collides(self.player) and isinstance(self.items[i],GamePowerup):
                    self.items[i].box.change_animation("close")
                    self.items[i].in_play = False

        for i in range(len(self.enemies) - 1, -1, -1):
            if not self.enemies[i].is_dead:
                self.enemies[i].update(dt)
                if (
                    self.enemies[i].collides(self.player) and
                    self.enemies[i].collidable and not
                    self.player.invulnerable and not
                    self.player.is_dead):
                        self.player.is_dead = True
                        self.player.score += self.enemies[i].points
                        self.enemies[i].change_state("dead")
            else:
                del self.enemies[i]

        for i in range(len(self.enemies_bullets) - 1, -1, -1):
            if self.enemies_bullets[i].collides(self.player) and not self.player.invulnerable:
                self.enemies_bullets[i].in_play = False
                self.player.is_dead = True
            if self.enemies_bullets[i].in_play:
                self.enemies_bullets[i].update(dt)
            else:
                del self.enemies_bullets[i]
        
        if not self.boss.is_dead:
            dif_x = self.player.x - self.boss.x
            dif_y = self.player.y - self.boss.y
            r = sqrt(dif_x*dif_x + dif_y*dif_y)
        
            if r < settings.VIRTUAL_WIDTH:
                self.boss.update(dt)
                if self.boss.collides(self.player) and self.boss.collidable and not self.player.invulnerable:
                    self.player.is_dead = True
                    self.player.touch_boss = True

    def render(self, surface: pygame.Surface) -> None:
        self.tilemap.render(surface)
        for bullet in self.enemies_bullets:
            bullet.render(surface)
        for enemy in self.enemies:
            enemy.render(surface)
        for item in self.items:
            if item.in_play:
                item.render(surface)
        
        self.boss.render(surface)
