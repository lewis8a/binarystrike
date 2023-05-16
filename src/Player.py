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

import settings

class Player(GameEntity):
    def __init__(self, x: int, y: int, game_level: TypeVar("GameLevel")) -> None:
        super().__init__(
            x,
            y,
            20,
            34,
            f"khan{settings.PLAYER_COLOR}",
            False,
            False,
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
                "idle-up": {"frames": [1]},
                "walk": {"frames": [2, 3, 4, 5, 6, 7, 8, 9], "interval": 0.06},
                "walk-up": {"frames": [10, 11, 12, 13, 14, 15, 16, 17], "interval": 0.06},
                "walk-down": {"frames": [18, 19, 20, 21, 22, 23, 24, 25], "interval": 0.06},
                "jump": {"frames": [26, 27, 29, 30, 32], "interval": 0.08},
                "dead": {"frames": [34, 35, 36, 37, 38], "interval": 0.25, "loops": 0},
            },
        )
        self.invulnerable = False
        self.invulnerable_time = 3
        self.invulnerable_count = 0
        self.lives = 3
        self.score = 0
        self.double_jump = False
        self.last_floor_position = (x, y)

    def go_invulnerable(self) -> None:
        self.invulnerable = True
        self.invulnerable_count = self.invulnerable_time

    def update(self, dt: float) -> None:
        if self.invulnerable:
            self.invulnerable_count -= dt
            if self.invulnerable_count <= 0:
                self.invulnerable = False
            
        super().update(dt)
