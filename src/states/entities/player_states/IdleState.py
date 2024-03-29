"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

Author: Kevin Márquez
marquezberriosk@gmail.com

Author: Lewis Ochoa
lewis8a@gmail.com

This file contains the class IdleState for player.
"""

from typing import Dict, Any

from gale.input_handler import InputHandler, InputData

from src.states.entities.BaseEntityState import BaseEntityState
from src.Projectile import Projectile

import settings

class IdleState(BaseEntityState):
    def enter(self, **enter_params: Dict[str, Any]) -> None:
        self.looking_up = enter_params.get("up", False)
        self.entity.padding_x_left = 5
        self.entity.padding_y_up = 5
        self.entity.vx = 0
        self.entity.vy = 0
        self.entity.double_jump = False
        if self.looking_up:
            self.entity.change_animation("idle-up")
        else:
            self.entity.change_animation("idle")
            
        InputHandler.register_listener(self)

    def exit(self) -> None:
        InputHandler.unregister_listener(self)
        self.entity.padding_x_left = 0
        self.entity.padding_y_up = 0

    def update(self, dt: float) -> None:
        if self.entity.handle_tilemap_collision_on_bottom():
            self.entity.vy = 0

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "move_left" and input_data.pressed:
            self.entity.flipped = True
            self.entity.change_state(
                "walk",
                direction="left",
                up=self.looking_up,
                down=False,
                left=True,
                right=False,
                )
        elif input_id == "move_right" and input_data.pressed:
            self.entity.flipped = True
            self.entity.change_state(
                "walk",
                direction="right",
                up=self.looking_up,
                down=False,
                left=False,
                right=True,
                )
        elif input_id == "look_up":
            if input_data.pressed:
                self.entity.change_animation("idle-up")
                self.looking_up = True
            else:
                self.entity.change_animation("idle")
                self.looking_up = False
        elif input_id == "jump" and input_data.pressed:
            self.entity.change_state(
                "jump",
                up=self.looking_up,
                down=False,
                left=False,
                right=False,
                )
        elif input_id == "shoot" and input_data.pressed:
            bullet = ""
            settings.SOUNDS["gun5"].stop()
            if settings.SOUND:
                settings.SOUNDS["gun5"].play()
            if self.entity.current_animation_id == "idle-up":
                if self.entity.flipped == True:
                    bullet = Projectile(self.entity.x + self.entity.width/4,
                                        self.entity.y,
                                        8, 8, 0, -settings.PROJECTILE_SPEED,
                                        settings.TEXTURES["bullet_player"], self.entity.game_level.camera)
                else:
                    bullet = Projectile(self.entity.x + self.entity.width/2.5,
                                        self.entity.y,
                                        8, 8, 0, -settings.PROJECTILE_SPEED,
                                        settings.TEXTURES["bullet_player"], self.entity.game_level.camera)
            elif self.entity.flipped == True:
                bullet = Projectile(self.entity.x,
                                    self.entity.y + self.entity.height/4,
                                    8, 8, -settings.PROJECTILE_SPEED, 0,
                                    settings.TEXTURES["bullet_player"], self.entity.game_level.camera)
            else:
                bullet = Projectile(self.entity.x + self.entity.width/1.5,
                                    self.entity.y + self.entity.height/4,
                                    8, 8, settings.PROJECTILE_SPEED, 0,
                                    settings.TEXTURES["bullet_player"], self.entity.game_level.camera)
            self.entity.bullets.append(bullet)
