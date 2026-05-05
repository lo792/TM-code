from ui.leader_screen import print_leader_screen
from features.team import Team
from features.team import Player
from features.team import Leader
from features.game import Game
from ui.player_screen import print_player_screen
from ui.starter import Starter


def built_game() -> Game:
    teams = Starter.get_teams()
    print("Bienvenue dans Code Game:")
    teams['team_blue'].describe()
    teams['team_red'].describe()
    print_player_screen()
    print_leader_screen()
    return Game(teamblue=teams['team_blue'], teamred=teams['team_red'])

def run_game():
    game=built_game()
    while game.state!="fin du jeu":
        current_team=game.current_team()
        leader=current_team.get_leader()
        announce = leader.announce()
        print(f"{announce['mot']}, {announce['fois']}")
        player=current_team.get_player()
        game.state="on continue"
        while game.state=="on continue" and announce['fois']>0:
            word_to_check=player.guess_word()
            game.check(word_to_check, announce['fois'])
            announce["fois"] -= 1
        game.tour_nb += 1
    #jeu fini
    print(f"Le jeu est terminé, l'équipe {game.winner} a gagné!")
    
    
    
if __name__== "__main__":
    run_game()