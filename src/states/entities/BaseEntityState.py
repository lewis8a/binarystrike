"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

Author: Kevin Márquez
marquezberriosk@gmail.com

Author: Lewis Ochoa
lewis8a@gmail.com

This file contains the base class BaseEntityState.
"""
from typing import TypeVar

from gale.state import BaseState, StateMachine


class BaseEntityState(BaseState):
    def __init__(
        self, entity: TypeVar("GameEntity"), state_machine: StateMachine
    ) -> None:
        super().__init__(state_machine)
        self.entity = entity
