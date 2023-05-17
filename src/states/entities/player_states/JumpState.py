"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

Author: Kevin Márquez
marquezberriosk@gmail.com

Author: Lewis Ochoa
lewis8a@gmail.com

This file contains the class JumpState for player.
"""

from typing import Dict, Any
from numpy import random

from gale.input_handler import InputHandler, InputData

import settings
from src.states.entities.BaseEntityState import BaseEntityState


class JumpState(BaseEntityState):
    def enter(self, **enter_params: Dict[str, Any]) -> None:
        self.entity.change_animation("jump")
        self.looking_up = enter_params.get("up", False)
        self.looking_down = enter_params.get("down", False)
        self.looking_left = enter_params.get("left", False)
        self.looking_right = enter_params.get("right", False)
        self.entity.vy = -settings.GRAVITY / 2
        InputHandler.register_listener(self)
        randomJumpSound = random.randint(1,4)
        settings.SOUNDS[f"jump{randomJumpSound}"].set_volume(0.3)
        settings.SOUNDS[f"jump{randomJumpSound}"].stop()
        if settings.SOUND:
            settings.SOUNDS[f"jump{randomJumpSound}"].play()

    def exit(self) -> None:
        InputHandler.unregister_listener(self)

    def update(self, dt: float) -> None:
        self.entity.vy += settings.GRAVITY * dt

        # If there is a collision on the right, correct x. Else, correct x if there is collision on the left.
        self.entity.handle_tilemap_collision_on_right() or self.entity.handle_tilemap_collision_on_left()

        if self.entity.handle_tilemap_collision_on_top():
            self.entity.vy = 0
        
        if not self.entity.check_floor_on_jump():
            self.entity.change_state(
                "fall",
                up=self.looking_up,
                down=self.looking_down,
                left=self.looking_left,
                right=self.looking_right,
                )

        if self.entity.vy >= 0:
            self.entity.change_state(
                "fall",
                up=self.looking_up,
                down=self.looking_down,
                left=self.looking_left,
                right=self.looking_right,
                )

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "move_left":
            if input_data.pressed:
                self.entity.vx = -settings.PLAYER_SPEED
                self.entity.flipped = True
                self.looking_left = True
            elif input_data.released and self.entity.vx <= 0:
                self.entity.vx = 0
                self.looking_left = False

        elif input_id == "move_right":
            if input_data.pressed:
                self.entity.vx = settings.PLAYER_SPEED
                self.entity.flipped = False
                self.looking_right = True
            elif input_data.released and self.entity.vx >= 0:
                self.entity.vx = 0
                self.looking_right = False
        
        elif input_id == "look_up":
            if input_data.pressed:
                self.looking_up = True
            else:
                self.looking_up = False
            
        elif input_id == "look_down":
            if input_data.pressed:
                self.looking_down = True
            else:
                self.looking_down = False
