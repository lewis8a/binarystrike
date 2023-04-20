"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

Author: Kevin Márquez
marquezberriosk@gmail.com

Author: Lewis Ochoa
lewis8a@gmail.com

This file contains the class Player.
"""
from typing import TypeVar

from src.GameEntity import GameEntity
from src.states.entities import player_states


class Player(GameEntity):
    def __init__(self, x: int, y: int, game_level: TypeVar("GameLevel")) -> None:
        super().__init__(
            x,
            y,
            72,
            72,
            "khan",
            game_level,
            states={
                "idle": lambda sm: player_states.IdleState(self, sm),
                "walk": lambda sm: player_states.WalkState(self, sm),
                "jump": lambda sm: player_states.JumpState(self, sm),
                "fall": lambda sm: player_states.FallState(self, sm),
                "dead": lambda sm: player_states.DeadState(self, sm),
            },
            animation_defs={
                "idle": {"frames": [0]},
                "walk": {"frames": [2, 3, 4, 5, 6, 7, 8, 9], "interval": 0.15},
                "jump": {"frames": [26, 27, 29, 30, 32], "interval": 0.15},
            },
        )
        self.score = 0
