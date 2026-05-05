from .team import Team
from .word_type import blue_list, red_list, grey_list, black_word


class Game:
    def __init__(self, teamred: Team, teamblue: Team):
        self.tour_nb=0
        self.state="on continue"
        self.teams=[teamred, teamblue]
    
    def current_team(self) -> Team:
        current_team_index = self.tour_nb % 2# à chaque tour, c'est 0 ou 1, alternés
        return self.teams[current_team_index]
    
    def not_current_team(self) -> Team:
        not_current_team_index = 1 if self.tour_nb % 2 == 0 else 0
        return self.teams[not_current_team_index]
    
    def get_current_word_type_list(self) -> list:
        team=self.current_team()
        if team.colour=="blue":
            return blue_list
        else:
            return red_list
    
    def check (self, word_to_check: str, fois: int):
        """_summary_ renvoi 1 etat: player continue, tour à l'autre equipe et fin du jeu

        Args:
            word_to_check (str): _description_

        Returns:
            str: _description_
        """
        if fois == 0:
            self.state="fin du tour"
            return
        elif word_to_check in self.get_current_word_type_list():
            self.state="on continue"
            self.current_team().add_success_word(word_to_check)
            if self.current_team().success_words==len(self.get_current_word_type_list):
                self.state = "fin du jeu"
                self.winner=self.current_team()
            return   
        elif word_to_check in black_word:
            self.state="fin du jeu"
            self.winner=self.not_current_team()
            return
        else:
            self.state = "fin du tour"
        
        