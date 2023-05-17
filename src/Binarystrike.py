"""
PVG 2023
Project: Binary Strike (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

Author: Kevin Márquez
marquezberriosk@gmail.com

Author: Lewis Ochoa
lewis8a@gmail.com

"""
import pygame

from gale.game import Game
from gale.input_handler import InputData
from gale.state import StateMachine

from src.states import game_states


class Binarystrike(Game):
    def init(self) -> None:
        self.state_machine = StateMachine({
            "begin": game_states.BeginState,
            "play": game_states.PlayState,
            "dialogue": game_states.DialogueState,
            "pause": game_states.PauseState,
            "start": game_states.StartState,
            "color": game_states.ColorState,
            "reborn": game_states.RebornState,
            "end": game_states.EndState,
            "setting": game_states.SettingState,
        })
        self.state_machine.change("dialogue",previous="init",next="start")

    def update(self, dt: float) -> None:
        self.state_machine.update(dt)

    def render(self, surface: pygame.Surface) -> None:
        self.state_machine.render(surface)

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if (input_id == 'quit' and input_data.pressed):
            self.quit()
        else:
            self.state_machine.on_input(input_id, input_data)