from nicegui import ui

from ui.ui_nice_guy import create_ui
from features.game_factory import Game_factory


def run_game() -> None:
    game = Game_factory.get_game()
    create_ui(game)
    ui.run(title="Code Name",  port=8080, reload=True, show=False)

if __name__ in {"__main__", "__mp_main__"}:
    run_game()
    