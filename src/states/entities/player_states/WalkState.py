"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

Author: Kevin Márquez
marquezberriosk@gmail.com

Author: Lewis Ochoa
lewis8a@gmail.com

This file contains the class WalkState for player.
"""

from typing import Dict, Any

from gale.input_handler import InputHandler, InputData

import settings
from src.states.entities.BaseEntityState import BaseEntityState
from src.Projectile import Projectile


class WalkState(BaseEntityState):
    def enter(self, **enter_params: Dict[str, Any]) -> None:
        self.looking_up = enter_params.get("up", False)
        self.looking_down = enter_params.get("down", False)
        self.looking_left = enter_params.get("left", False)
        self.looking_right = enter_params.get("right", False)
        self.entity.flipped = enter_params.get("direction") == "left"
        self.entity.vx = settings.PLAYER_SPEED
        if self.entity.flipped:
            self.entity.vx *= -1

        if self.looking_up and (self.looking_left or self.looking_right):
            self.entity.change_animation("walk-up")
        elif self.looking_down and (self.looking_left or self.looking_right):
            self.entity.change_animation("walk-down")
        else:
            self.entity.change_animation("walk")

        InputHandler.register_listener(self)

    def exit(self) -> None:
        InputHandler.unregister_listener(self)

    def update(self, dt: float) -> None:
        if not self.entity.check_floor():
            self.entity.change_state(
                "fall",
                up=self.looking_up,
                down=self.looking_down,
                left=self.looking_left,
                right=self.looking_right,
            )

        # If there is a collision on the right, correct x. Else, correct x if there is collision on the left.
        self.entity.handle_tilemap_collision_on_right() or self.entity.handle_tilemap_collision_on_left()

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "move_left":
            if input_data.pressed:
                self.entity.vx = -settings.PLAYER_SPEED
                self.entity.flipped = True
                self.looking_left = True
            elif input_data.released and self.entity.vx <= 0:
                self.looking_left = False
                self.entity.change_state("idle",up=self.looking_up)
        elif input_id == "move_right":
            if input_data.pressed:
                self.entity.vx = settings.PLAYER_SPEED
                self.entity.flipped = False
                self.looking_right = True
            elif input_data.released and self.entity.vx >= 0:
                self.entity.change_state("idle",up=self.looking_up)
                self.looking_right = False
        elif input_id == "look_up":
            if input_data.pressed:
                self.looking_up = True
                self.entity.change_animation("walk-up")
            else:
                self.looking_up = False
                self.entity.change_animation("walk")
        elif input_id == "look_down":
            if input_data.pressed:
                self.looking_down = True
                self.entity.change_animation("walk-down")
            else:
                self.looking_down = False
                self.entity.change_animation("walk")
        elif input_id == "jump" and input_data.pressed:
            self.entity.double_jump = False
            self.entity.change_state(
                "jump",
                up=self.looking_up,
                down=self.looking_down,
                left=self.looking_left,
                right=self.looking_right,
                )
        elif input_id == "shoot" and input_data.pressed:
            bullet = ""
            settings.SOUNDS["gun5"].stop()
            settings.SOUNDS["gun5"].play()
            if self.entity.current_animation_id == "walk-up":
                if self.entity.flipped == True:
                    bullet = Projectile(self.entity.x,
                                        self.entity.y + self.entity.height/3,
                                        8, 8, -settings.PROJECTILE_SPEED, -settings.PROJECTILE_SPEED,
                                        settings.TEXTURES["bullet_player"], self.entity.play_state.camera)
                else:
                    bullet = Projectile(self.entity.x + self.entity.width/1.5,
                                        self.entity.y + self.entity.height/3.5,
                                        8, 8, settings.PROJECTILE_SPEED, -settings.PROJECTILE_SPEED,
                                        settings.TEXTURES["bullet_player"], self.entity.play_state.camera)
            elif self.entity.current_animation_id == "walk-down":
                if self.entity.flipped == True:
                    bullet = Projectile(self.entity.x,
                                        self.entity.y + self.entity.height/3,
                                        8, 8, -settings.PROJECTILE_SPEED, settings.PROJECTILE_SPEED,
                                        settings.TEXTURES["bullet_player"], self.entity.play_state.camera)
                else:
                    bullet = Projectile(self.entity.x + self.entity.width/1.5,
                                        self.entity.y + self.entity.height/3,
                                        8, 8, settings.PROJECTILE_SPEED, settings.PROJECTILE_SPEED,
                                        settings.TEXTURES["bullet_player"], self.entity.play_state.camera)
            elif self.entity.flipped == True:
                bullet = Projectile(self.entity.x,
                                    self.entity.y + self.entity.height/4,
                                    8, 8, -settings.PROJECTILE_SPEED, 0,
                                    settings.TEXTURES["bullet_player"], self.entity.play_state.camera)
            else:
                bullet = Projectile(self.entity.x + self.entity.width/1.5,
                                    self.entity.y + self.entity.height/4,
                                    8, 8, settings.PROJECTILE_SPEED, 0,
                                    settings.TEXTURES["bullet_player"], self.entity.play_state.camera)
            self.entity.play_state.bullets.append(bullet)
