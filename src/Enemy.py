"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

Author: Kevin Márquez
marquezberriosk@gmail.com

Author: Lewis Ochoa
lewis8a@gmail.com

This file contains the class Enemy.
"""
from typing import TypeVar

from src.GameEntity import GameEntity


class Enemy(GameEntity):
    def __init__(
        self,
        x: float,
        y,
        width: float,
        height: float,
        game_level: TypeVar("GameLevel"),
        **definition
    ) -> None:
        ss = {
            "idle": lambda sm: definition["states"]["idle"](self, sm),
            "walk": lambda sm: definition["states"]["walk"](self, sm),
            "shoot": lambda sm: definition["states"]["shoot"](self, sm),
            "dead": lambda sm: definition["states"]["dead"](self, sm),
        }
        super().__init__(
            x,
            y,
            width,
            height,
            definition["texture_id"],
            True,
            True,
            game_level,
            states = ss,
            animation_defs=definition["animation_defs"],
        )
        self.collidable = True
        self.points = definition["points"]
        self.time_to_rest = definition["time_to_rest"]
        self.wait_time = 0
        self.texture_base = definition["texture_id"]
        self.walk_speed = definition["walk_speed"]
        self.state_machine.change(definition["first_state"], self.flipped)
