"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

Author: Kevin Márquez
marquezberriosk@gmail.com

Author: Lewis Ochoa
lewis8a@gmail.com

This file contains the main declaration of the game Binary Strike.
"""
import settings
from src.Binarystrike import Binarystrike

if __name__ == '__main__':
    game = Binarystrike(
        "Binary Strike",
        settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT,
        settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT
    )
    game.exec()