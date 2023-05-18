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
from src.AnimatedGameItem import AnimatedGameItem
from src.Player import Player
from src.states.entities import player_states

def pickup_key(key: AnimatedGameItem, player: Player, **kwargs: Dict[str,Any]):
    settings.SOUNDS["key"].stop()
    if settings.SOUND:
        settings.SOUNDS["key"].play()
    if(kwargs.get("level") <= settings.NUM_LEVELS):
        kwargs.get("state_machine").change(
            "begind",
            score=player.score,
            gems=player.coins_counter,
            level=kwargs.get("level"))
    else:
        kwargs.get("state_machine").change(
            "end",
            score=player.score,
            level=kwargs.get("level"))

def pickup_live_8(key: AnimatedGameItem, player: Player, **kwargs: Optional[Dict[str, Any]]):
    # settings.SOUNDS["key"].stop()
    # if settings.SOUND:
    #     settings.SOUNDS["key"].play()
    player.lives += 8

def pickup_live_16(key: AnimatedGameItem, player: Player, **kwargs: Optional[Dict[str, Any]]):
    # settings.SOUNDS["key"].stop()
    # if settings.SOUND:
    #     settings.SOUNDS["key"].play()
    player.lives += 16 

def activate_powerup(box_powerup: AnimatedGameItem, powerup: AnimatedGameItem) -> None:
    box_powerup.activate = True
    # play sound open powerup box
    # settings.SOUNDS["box"].stop()
    # if settings.SOUND:
    #     settings.SOUNDS["box"].play()
    def arrive():
        powerup.change_animation("dance")
        powerup.collidable = True
    
    powerup.in_play = True
    powerup.collidable = False
    final_y_key = powerup.y - 32
    Timer.tween(2, [ (powerup, {"y": final_y_key}) ], on_finish=arrive)

def hit_key_box_falling(box_powerup: AnimatedGameItem, powerup: AnimatedGameItem, player: Any):
    player.vy = 0
    player.y = box_powerup.y + player.height
    
    if not box_powerup.activate:
        activate_powerup(box_powerup, powerup)

def hit_key_box_jumping(box_powerup: AnimatedGameItem, powerup: AnimatedGameItem, player: Any):
    player.vy = 0
    player.y = box_powerup.y + box_powerup.height
    
    if not box_powerup.activate:
        activate_powerup(box_powerup, powerup)

def spawn_key(box_powerup: AnimatedGameItem, player: Any, **kwargs: Optional[Dict[str, Any]]):
    box_powerup.change_animation("open")
    if isinstance(player.state_machine.current, player_states.FallState):
        hit_key_box_falling(box_powerup, kwargs.get("powerup"), player)
    elif isinstance(player.state_machine.current, player_states.JumpState):
        hit_key_box_jumping(box_powerup, kwargs.get("powerup"), player)
    else:
        player.handle_tilemap_collision_on_right() or player.handle_tilemap_collision_on_left()
        if not box_powerup.activate:
            activate_powerup(box_powerup, kwargs.get("powerup"))
    
ITEMS: Dict[str, Dict[int, Dict[str, Any]]] = {
    "boxpowerup": {
        10: {
            "texture_id": "box_powerup",
            "solidness": dict(top=True, right=True, bottom=True, left=True),
            "consumable": False,
            "collidable": True,
            "on_collide": spawn_key,
            #"final_height": 16,
            #"original_height": 25,
            "height": 25,
            "width": 32,
            "animation_defs": {
                "open": {"frames": [0, 1, 2, 3, 4, 5, 6, 7], "interval": 0.15, "loops": 1},
                "idle": {"frames": [0]},
            },
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
