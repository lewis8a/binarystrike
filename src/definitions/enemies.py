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

from src.states.entities import boss_states, entities_states

Enemies: Dict[int, Dict[str, Any]] = {
    0: {
        "texture_id": "enemy1",
        "walk_speed": 15,
        "time_to_rest": 3.25,
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
        "time_to_rest": 4,
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
        "time_to_rest": 3.5,
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
    20: {
        "texture_id": "boss1",
        "live_points": 50,
        "width": 40,
        "height": 50,
        "multi_texture": True,
        "flipped": True,
        "walk_speed": 22,
        "time_to_rest": 2.75,
        "points": 500,
        "animation_defs": { # Falta
            "dead": {"frames": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "interval": 0.15},
            "idle": {"frames": [0, 1, 2, 3, 4], "interval": 0.15},
            "immune": {"frames": [0, 1, 2, 3, 4, 5, 6, 7], "interval": 0.1},
            "shoot": {"frames": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "interval": 0.1},
            "walk": {"frames": [0, 1, 2, 3, 4, 5, 6, 7], "interval": 0.2},
        },
        "states": {
            "idle": boss_states.BIdleState,
            "walk": boss_states.BWalkState,
            "shoot": boss_states.BShootState,
            "dead": boss_states.BDeadState,
        },
        "first_state": "idle",
    },
}