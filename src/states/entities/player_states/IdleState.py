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
from gale.input_handler import InputHandler, InputData

from src.states.entities.BaseEntityState import BaseEntityState
from src.Projectile import Projectile

import settings

class IdleState(BaseEntityState):
    def enter(self) -> None:
        self.entity.vx = 0
        self.entity.vy = 0
        self.entity.double_jump = False
        self.entity.change_animation("idle")
        InputHandler.register_listener(self)

    def exit(self) -> None:
        InputHandler.unregister_listener(self)

    def update(self, dt: float) -> None:
        if self.entity.handle_tilemap_collision_on_bottom():
            self.entity.vy = 0

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "move_left" and input_data.pressed:
            self.entity.flipped = True
            self.entity.change_state("walk", "left")
        elif input_id == "move_right" and input_data.pressed:
            self.entity.flipped = True
            self.entity.change_state("walk", "right")
        elif input_id == "look_up":
            if input_data.pressed:
                self.entity.change_animation("idle-up")
            else:
                self.entity.change_animation("idle")
        elif input_id == "jump" and input_data.pressed:
            self.entity.change_state("jump")
        elif input_id == "shoot" and input_data.pressed:
            bullet = ""
            settings.SOUNDS["gun5"].stop()
            settings.SOUNDS["gun5"].play()
            if self.entity.current_animation_id == "idle-up":
                if self.entity.flipped == True:
                    bullet = Projectile(self.entity.x + self.entity.width/4,
                                        self.entity.y,
                                        8, 8, 0, -settings.PROJECTILE_SPEED,
                                        settings.TEXTURES["bullet_player"], self.entity.play_state.camera)
                else:
                    bullet = Projectile(self.entity.x + self.entity.width/2.5,
                                        self.entity.y,
                                        8, 8, 0, -settings.PROJECTILE_SPEED,
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
