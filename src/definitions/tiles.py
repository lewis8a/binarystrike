"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

Author: Kevin Márquez
marquezberriosk@gmail.com

Author: Lewis Ochoa
lewis8a@gmail.com

This file contains the definition for tiles.
"""
from typing import Dict, Any

TILES_1: Dict[int, Dict[str, Any]] = {
    #Ground Level 1
    0: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    1: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    2: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    3: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    4: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    5: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    6: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    7: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    80: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    81: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    82: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    83: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
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
    366: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    367: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    368: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    369: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    508: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    509: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    510: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    511: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    516: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    517: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    518: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    519: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    580: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    581: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    588: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    589: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    652: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    653: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    660: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    661: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
}

TILES_2: Dict[int, Dict[str, Any]] = {
    # Ground Level 2
    6: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    7: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    8: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    9: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    10: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    11: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    16: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    17: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    34: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    35: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    42: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    43: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    44: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    45: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    46: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    47: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    48: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    49: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    52: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    53: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    60: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    61: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    62: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    63: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    64: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    65: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    70: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    71: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    78: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    79: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    80: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    81: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    82: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    83: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    96: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    97: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    98: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    99: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    100: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    101: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    102: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    103: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    108: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    109: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    110: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    111: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    112: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    113: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    114: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    115: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    116: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    117: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    118: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    119: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    120: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    121: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    122: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    123: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    124: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    125: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    126: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    127: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    128: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    129: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    130: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    131: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    132: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    133: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    134: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    135: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    136: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    137: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    138: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    139: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    140: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    141: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    142: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    143: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    144: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    145: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    146: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    147: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    148: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    149: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    150: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    151: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    152: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    153: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    154: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    155: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    156: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    157: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    158: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    159: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    160: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    161: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    168: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    169: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    170: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    171: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    172: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    173: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    178: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    179: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    204: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    205: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    206: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    207: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    208: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    209: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    210: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    211: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    222: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    223: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    224: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    225: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    226: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    227: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    228: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    229: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    230: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    231: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    232: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    233: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    240: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    241: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    242: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    243: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    244: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    245: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    258: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    259: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    260: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    261: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    262: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    263: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    264: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    265: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    270: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    271: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    272: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    273: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    274: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    275: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    276: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    277: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    278: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    279: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    280: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    282: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    283: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    284: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    285: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    286: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    287: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    288: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    289: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    290: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    291: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    292: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    293: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    294: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    295: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    296: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    297: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    298: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    299: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    300: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    301: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    302: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    303: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    304: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    305: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    306: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    307: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
}

TILES_3: Dict[int, Dict[str, Any]] = {
    # Ground Level 3
    0: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    1: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    2: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    10: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    11: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    12: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    17: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    18: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    19: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    27: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    28: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    37: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    38: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    39: {"solidness": dict(top=True, right=False, bottom=True, left=False)},
    51: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    52: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    53: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    54: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    55: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    63: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    65: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    66: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    67: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    70: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    71: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    72: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    74: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    75: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    78: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    79: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    91: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    92: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    93: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    95: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    143: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    144: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    145: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    149: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    150: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    151: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    167: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    193: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    194: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    195: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    196: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
}