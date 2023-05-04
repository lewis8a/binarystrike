"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

Author: Kevin Márquez
marquezberriosk@gmail.com

Author: Lewis Ochoa
lewis8a@gmail.com

This file contains the base class Tile.
"""
from typing import Dict

from src.GameObject import GameObject


class Tile(GameObject):
    def __init__(
        self,
        i: int,
        j: int,
        width: int,
        height: int,
        frame_index: int,
        soliness: Dict[str, bool],
        num_level:int,
    ) -> None:
        self.i = i
        self.j = j
        super().__init__(
            self.j * width,
            self.i * height,
            width,
            height,
            f"tile_{num_level}",
            frame_index,
            soliness,
        )
