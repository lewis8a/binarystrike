import settings
from src.Binarystrike import Binarystrike

if __name__ == '__main__':
    game = Binarystrike(
        "Binarystrike",
        settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT,
        settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT
    )
    game.exec()
