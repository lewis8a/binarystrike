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
            # states={
            #     state_name: lambda sm: state_class(self, sm)
            #     for state_name, state_class in definition["states"].items()
            # },
            animation_defs=definition["animation_defs"],
        )
        self.texture_base = definition["texture_id"]
        self.walk_speed = definition["walk_speed"]
        self.state_machine.change(definition["first_state"], self.flipped)
