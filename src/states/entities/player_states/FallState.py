"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

Author: Kevin Márquez
marquezberriosk@gmail.com

Author: Lewis Ochoa
lewis8a@gmail.com

This file contains the class FallState for player.
"""
from gale.input_handler import InputHandler, InputData

import settings
from src.states.entities.BaseEntityState import BaseEntityState
from src.Projectile import Projectile

class FallState(BaseEntityState):
    def enter(self) -> None:
        self.entity.change_animation("jump")
        self.looking_up = False
        self.looking_down = False
        self.looking_left = False
        self.looking_right = True
        InputHandler.register_listener(self)

    def exit(self) -> None:
        InputHandler.unregister_listener(self)

    def update(self, dt: float) -> None:
        self.entity.vy += settings.GRAVITY * dt

        # If there is a collision on the right, correct x. Else, correct x if there is collision on the left.
        self.entity.handle_tilemap_collision_on_right() or self.entity.handle_tilemap_collision_on_left()

        if self.entity.handle_tilemap_collision_on_bottom():
            self.entity.vy = 0
            if self.entity.vx > 0:
                self.entity.change_state("walk", "right")
            elif self.entity.vx < 0:
                self.entity.change_state("walk", "left")
            else:
                self.entity.change_state("idle")

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
        
        elif input_id == "jump" and input_data.pressed:
            if not self.entity.double_jump:
                self.entity.change_state("jump")
                self.entity.double_jump = True
        
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
            
        elif input_id == "shoot" and input_data.pressed:
            bullet = ""
            if self.looking_up and self.looking_left: # Up and letf
                bullet = Projectile(self.entity.x + self.entity.width/2 - 4,
                                    self.entity.y,
                                    8, 8, -settings.PROJECTILE_SPEED, -settings.PROJECTILE_SPEED,
                                    self.entity.play_state.camera)
            elif self.looking_up and self.looking_right: # Up and right
                bullet = Projectile(self.entity.x + self.entity.width/2 - 4,
                                    self.entity.y + self.entity.height,
                                    8, 8, settings.PROJECTILE_SPEED, -settings.PROJECTILE_SPEED,
                                    self.entity.play_state.camera)
            elif self.looking_down and self.looking_left: # Down and left
                bullet = Projectile(self.entity.x + self.entity.width/2 - 4,
                                    self.entity.y,
                                    8, 8, -settings.PROJECTILE_SPEED, settings.PROJECTILE_SPEED,
                                    self.entity.play_state.camera)
            elif self.looking_down and self.looking_right: # Down and right
                bullet = Projectile(self.entity.x + self.entity.width/2 - 4,
                                    self.entity.y + self.entity.height,
                                    8, 8, settings.PROJECTILE_SPEED, settings.PROJECTILE_SPEED,
                                    self.entity.play_state.camera)
            elif self.looking_up:
                bullet = Projectile(self.entity.x + self.entity.width/2 - 4,
                                    self.entity.y,
                                    8, 8, 0, -settings.PROJECTILE_SPEED,
                                    self.entity.play_state.camera)
            elif self.looking_down:
                bullet = Projectile(self.entity.x + self.entity.width/2 - 4,
                                    self.entity.y + self.entity.height,
                                    8, 8, 0, settings.PROJECTILE_SPEED,
                                    self.entity.play_state.camera)
            elif self.looking_left:
                bullet = Projectile(self.entity.x,
                                    self.entity.y + self.entity.height/2 - 4,
                                    8, 8, -settings.PROJECTILE_SPEED, 0,
                                    self.entity.play_state.camera)
            else:
                bullet = Projectile(self.entity.x + self.entity.width/4,
                                    self.entity.y + self.entity.height/5,
                                    8, 8, settings.PROJECTILE_SPEED, 0,
                                    self.entity.play_state.camera)
            self.entity.play_state.bullets.append(bullet)
