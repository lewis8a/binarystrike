"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

Author: Kevin Márquez
marquezberriosk@gmail.com

Author: Lewis Ochoa
lewis8a@gmail.com

This file contains the definition for creatures.
"""
from typing import Dict, Any

from src.states.entities import entities_states

Enemies: Dict[int, Dict[str, Any]] = {
    0: {
        "texture_id": "enemy1",
        "walk_speed": 15,
        "time_to_rest": 3,
        "points": 100,
        "animation_defs": {
            "walk": {"frames": [0, 1, 2, 3, 4, 5, 6], "interval": 0.15},
            "shoot": {"frames": [0, 1, 2, 3], "interval": 0.15},
            "idle": {"frames": [0, 1, 2, 3, 4, 5, 6], "interval": 0.15},
            "dead": {"frames": [0, 1, 2, 3], "interval": 0.15},
        },
        "states": {
            "idle": entities_states.EIdleState,
            "walk": entities_states.EWalkState,
            "shoot": entities_states.EShootState,
            "dead": entities_states.EDeadState,
            },
        "first_state": "walk",
    },
    1: {
        "texture_id": "enemy2",
        "walk_speed": 15,
        "time_to_rest": 3,
        "points": 115,
        "animation_defs": {
            "walk": {"frames": [0, 1, 2, 3, 4, 5, 6, 7], "interval": 0.15},
            "shoot": {"frames": [0, 1, 2, 3], "interval": 0.15},
            "idle": {"frames": [0, 1, 2, 3, 4, 5, 6, 7 ,8], "interval": 0.15},
            "dead": {"frames": [0, 1, 2, 3], "interval": 0.15},
        },
        "states": {
            "idle": entities_states.EIdleState,
            "walk": entities_states.EWalkState,
            "shoot": entities_states.EShootState,
            "dead": entities_states.EDeadState,
            },
        "first_state": "walk",
    },
    2: {
        "texture_id": "enemy3",
        "walk_speed": 15,
        "time_to_rest": 3,
        "points": 80,
        "animation_defs": {
            "walk": {"frames": [0, 1, 2, 3, 4, 5, 6, 7], "interval": 0.15},
            "shoot": {"frames": [0, 1, 2, 3], "interval": 0.15},
            "idle": {"frames": [0, 1, 2, 3, 4, 5], "interval": 0.15},
            "dead": {"frames": [0, 1, 2, 3,4], "interval": 0.15},
        },
        "states": {
            "idle": entities_states.EIdleState,
            "walk": entities_states.EWalkState,
            "shoot": entities_states.EShootState,
            "dead": entities_states.EDeadState,
            },
        "first_state": "walk",
    },
    2: {
        "texture_id": "enemy3",
        "walk_speed": 15,
        "time_to_rest": 3,
        "points": 80,
        "animation_defs": {
            "walk": {"frames": [0, 1, 2, 3, 4, 5, 6, 7], "interval": 0.15},
            "shoot": {"frames": [0, 1, 2, 3], "interval": 0.15},
            "idle": {"frames": [0, 1, 2, 3, 4, 5], "interval": 0.15},
            "dead": {"frames": [0, 1, 2, 3,4], "interval": 0.15},
        },
        "states": {
            "idle": entities_states.EIdleState,
            "walk": entities_states.EWalkState,
            "shoot": entities_states.EShootState,
            "dead": entities_states.EDeadState,
            },
        "first_state": "walk",
    },
}