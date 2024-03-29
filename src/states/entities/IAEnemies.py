"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

Author: Kevin Márquez
marquezberriosk@gmail.com

Author: Lewis Ochoa
lewis8a@gmail.com

This file contains the base class IAEnemies.
"""

from numpy import sqrt

from src.GameObject import GameObject

import settings

class IAEnemies():
    def __init__(self) -> None:
        pass

    def can_see_player(self) -> bool:
        player = self.entity.game_level.player
        ex = self.entity.x + self.entity.width/2
        ey = self.entity.y + self.entity.height/2

        px = player.x + player.width/2
        py = player.y + player.height/2

        dif_x = px - ex
        dif_y = py - ey
        dist = sqrt(dif_x*dif_x + dif_y*dif_y)

        return dist <= settings.RANGE_VISION

    
    def check_boundary(self) -> bool:
        world_width = self.entity.tilemap.width

        if self.entity.x + self.entity.width >= world_width:
            self.entity.x = world_width - self.entity.width
            return True
        elif self.entity.x <= 0:
            self.entity.x = 0
            return True

        if (
            self.entity.handle_tilemap_collision_on_left()
            or self.entity.handle_tilemap_collision_on_right()
        ):
            return True

        # Avoid falling
        can_fall = False
        if self.entity.vx > 0:
            # Snail row
            row = int(self.entity.tilemap.to_i(self.entity.y + 25))
            # Col of the right side of the snail
            col = int(self.entity.tilemap.to_j(self.entity.x + self.entity.width + 10))

            can_fall = not self.entity.tilemap.check_solidness_on(
                row + 1, col, GameObject.TOP
            )
        elif self.entity.vx < 0:
            # Snail row
            row = int(self.entity.tilemap.to_i(self.entity.y + 25))
            # Col of the left side of the snail
            col = int(self.entity.tilemap.to_j(self.entity.x - 5))

            can_fall = not self.entity.tilemap.check_solidness_on(
                row + 1, col, GameObject.TOP
            )

        return can_fall
