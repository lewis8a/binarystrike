"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

Author: Kevin Márquez
marquezberriosk@gmail.com

Author: Lewis Ochoa
lewis8a@gmail.com

This file contains the DrawableMixin.
"""
import pygame

import settings

class DrawableMixin:
    def render(self, surface: pygame.Surface) -> None:
        texture = settings.TEXTURES[self.texture_id]
        frame = settings.FRAMES[self.texture_id][self.frame_index]
        image = pygame.Surface((frame.width, frame.height), pygame.SRCALPHA)
        image.blit(texture, (0, 0), frame)
        alpha = getattr(self, "alpha_value", 255)
        image.set_alpha(alpha)
        if self.flipped:
            image = pygame.transform.flip(image, True, False)

        # pl_x = getattr(self, "padding_x_left", 0)
        # pr_x = getattr(self, "padding_x_right", 0)
        # pu_y = getattr(self, "padding_y_up", 0)
        # pd_y = getattr(self, "padding_y_down", 0)

        # if hasattr(self, "alpha_value"):
        #     pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, self.width, self.height), 1)
        #     pygame.draw.rect(surface, (0, 255, 0), (self.x + pl_x, self.y + pu_y, self.width - pr_x, self.height - pd_y), 1)

        surface.blit(image, (self.x, self.y))
