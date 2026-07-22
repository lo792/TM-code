from .team import Team, Leader, Player
from .game import Game


class Game_factory:
    @staticmethod
    def get_game(data: dict) -> Game:
        l = Leader(data["leader_blue"])
        p = Player(data["player_blue"])
        team_blue = Team('blue', p, l)
        l = Leader(data["leader_red"])
        p = Player(data["player_red"])
        team_red = Team('red', p, l)
        return Game(team_red, team_blue)
