"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

Author: Kevin Márquez
marquezberriosk@gmail.com

Author: Lewis Ochoa
lewis8a@gmail.com

This file contains the class AnimatedGameItem.
"""
from typing import Dict, Callable, TypeVar, Any, Optional

from src.GameObject import GameObject
from src import mixins

class AnimatedGameItem(GameObject, mixins.AnimatedMixin):
    def __init__(
        self,
        collidable: bool,
        consumable: bool,
        item_name: str,
        animation_defs: Dict[str, Any],
        on_collide: Optional[Callable[[TypeVar("AnimatedGameItem"), Any], Any]] = None,
        on_consume: Optional[Callable[[TypeVar("AnimatedGameItem"), Any], Any]] = None,
        *args,
        **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self.collidable = collidable
        self.consumable = consumable
        self._on_collide = on_collide
        self._on_consume = on_consume
        self.type = item_name
        self.current_animation = None
        self.current_animation_id = ""
        self.animations = {}
        self.generate_animations(animation_defs)
        self.frame_index = -1
        self.multi_texture = False
        self.y -= 9
        self.powerup = None
        
        if self.type == "key":
            self.in_play = False
        
        elif self.type == "boxpowerup":
            self.in_play = True
            self.activate = False

        self.change_animation("idle")



    # def respawn(self, x: Optional[float] = None, y: Optional[float] = None) -> None:
    #     if x is not None:
    #         self.x = x
    #     if y is not None:
    #         self.y = y
    #     self.in_play = True

    def on_collide(self, another: Any, **kwargs: Optional[Dict[str, Any]]) -> Any:
        if not self.collidable or self._on_collide is None:
            return None
        return self._on_collide(self, another, **kwargs)

    def on_consume(self, consumer: Any, **kwargs: Optional[Dict[str, Any]]) -> Any:
        if not self.consumable or self._on_consume is None:
            return None
        self.in_play = False
        return self._on_consume(self, consumer, **kwargs)
