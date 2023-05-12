"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

Author: Kevin Márquez
marquezberriosk@gmail.com

Author: Lewis Ochoa
lewis8a@gmail.com

This file contains the class DeadState for player.
"""

from numpy import random

import settings
from src.states.entities.BaseEntityState import BaseEntityState


class DeadState(BaseEntityState):
    def enter(self) -> None:
        randomJumpSound = random.randint(1,3)
        settings.SOUNDS[f"death{randomJumpSound}"].set_volume(0.4)
        settings.SOUNDS[f"death{randomJumpSound}"].stop()
        settings.SOUNDS[f"death{randomJumpSound}"].play()
        self.entity.is_dead = True