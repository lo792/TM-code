from nicegui import ui

from ui.ui_nice_guy import create_ui
from features.game_factory import Game_factory


"""def run_game():
    data = Ui_game.input_teams()
    factory = Game_factory()
    game = factory.get_game(data)
    ui_game = Ui_game(game)    
    ui_game.print_title()
    ui_game.print_current_team()
    ui_game.print_not_current_team()
    ui_game.print_player_screen()
    ui_game.print_leader_screen()
    while game.state!="fin du jeu":
        ui_game.print_next_playing_team()
        announce = ui_game.print_current_team_leader_announce()
        game.state="on continue"
        while game.state=="on continue" and announce['fois']>0:
            word_to_check=ui_game.input_player_guess_word()
            game.check(word_to_check, announce['fois'])
            announce["fois"] -= 1
        game.tour_nb += 1
    #jeu fini
    ui_game.print_end_of_game()
    #verifier le cas ou le leader mais zero plutot a mettre dans verify_announce"""
    
def run_game() -> None:
    game = Game_factory.get_game()
    create_ui(game)
    ui.run(title="Code Name",  port=8080, reload=True, show=False)

if __name__ in {"__main__", "__mp_main__"}:
    run_game()
    