"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the definition for tiles.
"""
from typing import Dict, Any

TILES: Dict[int, Dict[str, Any]] = {
    # Ground
    0: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    1: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    2: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    3: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    4: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    5: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    6: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    7: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    216: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    217: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    218: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    219: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    220: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    221: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    222: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    223: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    288: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    289: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    290: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    291: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    292: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    293: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    508: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    509: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    510: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    511: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    580: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    581: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    652: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    653: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    # Blocks
    # 6: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    # 17: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    # 41: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
}
