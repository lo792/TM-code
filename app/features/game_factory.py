from .team import Team, Leader, Player
from .game import Game


class Game_factory:
    @staticmethod
    def get_game(
        leader_blue: str = "leader_blue",
        player_blue: str = "player_blue",
        leader_red: str = "leader_red",
        player_red: str = "player_red"
        ) -> Game:
        l = Leader(leader_blue)
        p = Player(player_blue)
        team_blue = Team('blue', p, l)
        l = Leader(leader_red)
        p = Player(player_red)
        team_red = Team('red', p, l)
        return Game(team_red, team_blue)
