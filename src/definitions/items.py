"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

Author: Kevin Márquez
marquezberriosk@gmail.com

Author: Lewis Ochoa
lewis8a@gmail.com

This file contains the definition for items.
"""
from typing import Dict, Any, Optional

from gale.timer import Timer

import settings
from src.GamePowerup import GamePowerup
from src.GameBox import GameBox
from src.Player import Player
from src.states.entities import player_states

def pickup_live_8(key: GamePowerup, player: Player, **kwargs: Optional[Dict[str, Any]]):
    # settings.SOUNDS["key"].stop()
    # if settings.SOUND:
    #     settings.SOUNDS["key"].play()
    player.lives += 8

def pickup_live_16(key: GamePowerup, player: Player, **kwargs: Optional[Dict[str, Any]]):
    # settings.SOUNDS["key"].stop()
    # if settings.SOUND:
    #     settings.SOUNDS["key"].play()
    player.lives += 16 

def activate_powerup(box_powerup: GameBox, powerup: GamePowerup) -> None:
    box_powerup.activate = True
    # play sound open powerup box
    # settings.SOUNDS["box"].stop()
    # if settings.SOUND:
    #     settings.SOUNDS["box"].play()
    def arrive():
        powerup.change_animation("dance")
        powerup.collidable = True

    def after():
        Timer.tween(1, [ (powerup, {"y": final_y_key}) ], on_finish=arrive)
    
    powerup.in_play = True
    powerup.collidable = False
    final_y_key = powerup.y - 32
    Timer.after(1.2, after)

def spawn_key(box_powerup: GameBox, player: Any):
    box_powerup.change_animation("open")
    if not box_powerup.activate:
            activate_powerup(box_powerup, box_powerup.powerup)
    
ITEMS: Dict[str, Dict[int, Dict[str, Any]]] = {
    "boxpowerup": {
        10: {
            "texture_id": "box_powerup",
            "solidness": dict(top=True, right=True, bottom=True, left=True),
            "consumable": False,
            "collidable": True,
            "on_collide": spawn_key,
            "height": 25,
            "width": 32,
            "animation_defs": {
                "open": {"frames": [0, 1, 2, 3, 4, 5, 6, 7], "interval": 0.15, "loops": 1},
                "close": {"frames": [7, 6, 5, 4, 3, 2, 1, 0], "interval": 0.15, "loops": 1},
                "idle": {"frames": [0]},
            },
            "frame_index": -1,
        }
    },
    "key": {
        11: {
            "texture_id": "live_powerup",
            "solidness": dict(top=False, right=False, bottom=False, left=False),
            "consumable": True,
            "collidable": True,
            "on_consume": pickup_live_8,
            "height": 14,
            "width": 12,
            "animation_defs": {
                "dance": {"frames": [0, 1, 2, 3, 4, 5, 6, 7], "interval": 0.15},
                "idle": {"frames": [0]},
            },
            "frame_index": -1,
        },
        12: {
            "texture_id": "live_powerup",
            "solidness": dict(top=False, right=False, bottom=False, left=False),
            "consumable": True,
            "collidable": True, 
            "on_consume": pickup_live_16,
            "height": 14,
            "width": 12,
            "animation_defs": {
                "dance": {"frames": [0, 1, 2, 3, 4, 5, 6, 7], "interval": 0.15},
                "idle": {"frames": [0]},
            },
            "frame_index": -1,
        }
    },  
    # "coins": {
    #     62: {
    #         "texture_id": "tiles",
    #         "solidness": dict(top=False, right=False, bottom=False, left=False),
    #         "consumable": True,
    #         "collidable": True,
    #         "on_consume": pickup_green_coin,
    #     },
    # },
}
