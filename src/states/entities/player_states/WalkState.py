"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class WalkState for player.
"""
from gale.input_handler import InputHandler, InputData

import settings
from src.states.entities.BaseEntityState import BaseEntityState
from src.Projectile import Projectile


class WalkState(BaseEntityState):
    def enter(self, direction: str) -> None:
        self.entity.flipped = direction == "left"
        self.entity.vx = settings.PLAYER_SPEED
        if self.entity.flipped:
            self.entity.vx *= -1
        self.entity.change_animation("walk")
        InputHandler.register_listener(self)

    def exit(self) -> None:
        InputHandler.unregister_listener(self)

    def update(self, dt: float) -> None:
        if not self.entity.check_floor():
            self.entity.change_state("fall")

        # If there is a collision on the right, correct x. Else, correct x if there is collision on the left.
        self.entity.handle_tilemap_collision_on_right() or self.entity.handle_tilemap_collision_on_left()

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "move_left":
            if input_data.pressed:
                self.entity.vx = -settings.PLAYER_SPEED
                self.entity.flipped = True
            elif input_data.released and self.entity.vx <= 0:
                self.entity.change_state("idle")
        elif input_id == "move_right":
            if input_data.pressed:
                self.entity.vx = settings.PLAYER_SPEED
                self.entity.flipped = False
            elif input_data.released and self.entity.vx >= 0:
                self.entity.change_state("idle")
        elif input_id == "look_up":
            if input_data.pressed:
                self.entity.change_animation("walk-up")
            else:
                self.entity.change_animation("walk")
        elif input_id == "look_down":
            if input_data.pressed:
                self.entity.change_animation("walk-down")
            else:
                self.entity.change_animation("walk")
        elif input_id == "jump" and input_data.pressed:
            self.entity.double_jump = False
            self.entity.change_state("jump")
        elif input_id == "shoot" and input_data.pressed:
            bullet = ""
            if self.entity.current_animation_id == "walk-up":
                if self.entity.flipped == True:
                    bullet = Projectile(self.entity.x,
                                        self.entity.y + self.entity.height/3,
                                        8, 8, -settings.PROJECTILE_SPEED, -settings.PROJECTILE_SPEED,
                                        settings.TEXTURES["bullet1"], self.entity.play_state.camera)
                else:
                    bullet = Projectile(self.entity.x + self.entity.width/1.5,
                                        self.entity.y + self.entity.height/3.5,
                                        8, 8, settings.PROJECTILE_SPEED, -settings.PROJECTILE_SPEED,
                                        settings.TEXTURES["bullet1"], self.entity.play_state.camera)
            elif self.entity.current_animation_id == "walk-down":
                if self.entity.flipped == True:
                    bullet = Projectile(self.entity.x,
                                        self.entity.y + self.entity.height/3,
                                        8, 8, -settings.PROJECTILE_SPEED, settings.PROJECTILE_SPEED,
                                        settings.TEXTURES["bullet1"], self.entity.play_state.camera)
                else:
                    bullet = Projectile(self.entity.x + self.entity.width/1.5,
                                        self.entity.y + self.entity.height/3,
                                        8, 8, settings.PROJECTILE_SPEED, settings.PROJECTILE_SPEED,
                                        settings.TEXTURES["bullet1"], self.entity.play_state.camera)
            elif self.entity.flipped == True:
                bullet = Projectile(self.entity.x,
                                    self.entity.y + self.entity.height/4,
                                    8, 8, -settings.PROJECTILE_SPEED, 0,
                                    settings.TEXTURES["bullet1"], self.entity.play_state.camera)
            else:
                bullet = Projectile(self.entity.x + self.entity.width/1.5,
                                    self.entity.y + self.entity.height/4,
                                    8, 8, settings.PROJECTILE_SPEED, 0,
                                    settings.TEXTURES["bullet1"], self.entity.play_state.camera)
            self.entity.play_state.bullets.append(bullet)
