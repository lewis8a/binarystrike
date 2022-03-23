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

import pygame

import settings
from src.Camera import Camera
from src.Enemy import Enemy
from src.GameItem import GameItem
from src.definitions import enemies, items


class GameLevel:
    def __init__(self, num_level: int, camera: Camera) -> None:
        self.tilemap = None
        self.Enemies = []
        self.items = []
        self.camera = camera
        settings.LevelLoader().load(self, settings.TILEMAPS[num_level], num_level)

    def add_item(self, item_data: Dict[str, Any]) -> None:
        definition = items.ITEMS[item_data["item_name"]][item_data["frame_index"]]
        definition.update(item_data)
        self.items.append(GameItem(**definition))

    def add_Enemy(self, Enemy_data: Dict[str, Any]) -> None:
        definition = enemies.Enemies[Enemy_data["tile_index"]]
        self.Enemies.append(
            Enemy(
                Enemy_data["x"],
                Enemy_data["y"],
                Enemy_data["width"],
                Enemy_data["height"],
                self,
                **definition,
            )
        )

    def update(self, dt: float) -> None:
        self.tilemap.set_render_boundaries(self.camera.get_rect())

        for creature in self.Enemies:
            creature.update(dt)

        # Remove dead Enemies
        self.Enemies = [
            creature for creature in self.Enemies if not creature.is_dead
        ]

    def render(self, surface: pygame.Surface) -> None:
        self.tilemap.render(surface)
        for creature in self.Enemies:
            creature.render(surface)
        for item in self.items:
            if item.in_play:
                item.render(surface)
