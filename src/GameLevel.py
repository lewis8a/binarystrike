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
from src.Enemie import Enemie
from src.GameItem import GameItem
from src.definitions import enemies, items


class GameLevel:
    def __init__(self, num_level: int, camera: Camera) -> None:
        self.tilemap = None
        self.enemies = []
        self.items = []
        self.camera = camera
        settings.LevelLoader().load(self, settings.TILEMAPS[num_level])

    def add_item(self, item_data: Dict[str, Any]) -> None:
        definition = items.ITEMS[item_data["item_name"]][item_data["frame_index"]]
        definition.update(item_data)
        self.items.append(GameItem(**definition))

    def add_enemie(self, enemie_data: Dict[str, Any]) -> None:
        definition = enemies.ENEMIES[enemie_data["tile_index"]]
        self.enemies.append(
            Enemie(
                enemie_data["x"],
                enemie_data["y"],
                enemie_data["width"],
                enemie_data["height"],
                self,
                **definition,
            )
        )

    def update(self, dt: float) -> None:
        self.tilemap.set_render_boundaries(self.camera.get_rect())

        for creature in self.enemies:
            creature.update(dt)

        # Remove dead enemies
        self.enemies = [
            creature for creature in self.enemies if not creature.is_dead
        ]

    def render(self, surface: pygame.Surface) -> None:
        self.tilemap.render(surface)
        for creature in self.enemies:
            creature.render(surface)
        for item in self.items:
            if item.in_play:
                item.render(surface)
