from ui.ui_game import Ui_game
from features.game_factory import Game_factory

  

def run_game():
    data = Ui_game.input_teams()
    factory = Game_factory()
    game = factory.get_game(data)
    ui = Ui_game(game)    
    ui.print_title()
    ui.print_current_team()
    ui.print_not_current_team()
    ui.print_player_screen()
    ui.print_leader_screen()
    while game.state!="fin du jeu":
        ui.print_next_playing_team()
        announce = ui.print_current_team_leader_announce()
        game.state="on continue"
        while game.state=="on continue" and announce['fois']>0:
            word_to_check=ui.input_player_guess_word()
            game.check(word_to_check, announce['fois'])
            announce["fois"] -= 1
        game.tour_nb += 1
    #jeu fini
    ui.print_end_of_game()
    #verifier le cas ou le leader mais zero plutot a mettre dans verify_announce
    
    
if __name__== "__main__":
    run_game()
    