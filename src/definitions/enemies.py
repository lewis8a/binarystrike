"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the definition for creatures.
"""
from typing import Dict, Any

from src.states.entities import entities_states

Enemies: Dict[int, Dict[str, Any]] = {
    379: {
        "texture_id": "Enemy2",
        "walk_speed": 15,
        "animation_defs": {
            "walk": {"frames": [0, 1, 2, 3, 4, 5, 6, 7], "interval": 0.25},
            "shoot": {"frames": [0, 1, 2, 3], "interval": 0.15},
            "idle": {"frames": [0, 1, 2, 3, 4, 5, 6, 7 ,8], "interval": 0.25},
            "dead": {"frames": [0, 1, 2, 3], "interval": 0.25},
        },
        "states": {
            "idle": entities_states.EIdleState,
            "walk": entities_states.EWalkState,
            "shoot": entities_states.EShootState,
            },
        "first_state": "walk",
    },
}