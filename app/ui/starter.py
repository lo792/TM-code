from features.team import Player, Leader, Team

class Starter:
    @staticmethod
    def get_teams() -> dict:
        l = Leader(input("Quel est ton nom?"))
        p = Player(input("Quel est ton nom?"))
        team_blue = Team('blue', p, l)
        l = Leader(input("Quel est ton nom?"))
        p = Player(input("Quel est ton nom?"))
        team_red = Team('red', p, l)
        return {
            'team_blue': team_blue,
            'team_red': team_red
        }
        