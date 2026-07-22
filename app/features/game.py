from .team import Team
from .word_type import blue_list, red_list, grey_list, black_word
from .team import Player
from ui.score_displayer import Score


class Game:
    def __init__(self, teamred: Team, teamblue: Team):
        self.tour_nb=0
        self.state="on continue"
        self.teams=[teamred, teamblue]
        self.score = Score(self)
    
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
        
    def get_not_current_word_type_list(self) -> list:
        team=self.not_current_team()
        if team.colour=="blue":
            return blue_list
        else:
            return red_list
    
    def verify_word_to_guess(self, word_to_check) -> str:
        while True:
            tous_les_mots_de_la_grille = (
                self.get_current_word_type_list() +
                self.get_not_current_word_type_list() +
                black_word +
                grey_list
            )
            deja_devine = (
                self.current_team().success_words +
                self.not_current_team().success_words
            )
            if (word_to_check in tous_les_mots_de_la_grille) and not (deja_devine):
                return word_to_check
            else:
                print("Le mot a déjà été deviné ou n'est pas dans la grille")
                word_to_check = self.current_team().get_player().guess_word()

        return word_to_check
    
    #def verify_annonce(self, announce) -> str:
    #    while True:
    #        tous_les_mots_de_la_grille = (
    #            self.get_current_word_type_list() +
    #            self.get_not_current_word_type_list() +
    #            black_word +
    #            grey_list
    #        )
    #        if announce in tous_les_mots_de_la_grille:
    #            print("Ce mot n'est pas dans la grille")
    #            announce = self.current_team().get_leader().announce()
    #        else:
    #            return True
    #            
    #    return announce
    
    def check (self, word_to_check: str, fois: int):
        if fois == 0:
            self.state="fin du tour"
            self.score.score_displayer()
            return
        elif word_to_check in self.get_current_word_type_list():
            self.state="on continue"
            self.current_team().add_success_word(word_to_check)
            if len(self.current_team().success_words)==len(self.get_current_word_type_list()):
                self.state = "fin du jeu"
                self.winner=self.current_team().colour
            return   
        elif word_to_check in black_word:
            self.state="fin du jeu"
            self.winner=self.not_current_team().colour
            return
        elif word_to_check in self.get_not_current_word_type_list():
            self.state = "fin du tour"
            self.score.score_displayer()
            self.not_current_team().add_success_word(word_to_check)
            if  len(self.not_current_team().success_words)==len(self.get_not_current_word_type_list()):
                self.state = "fin du jeu"
                self.winner = self.not_current_team().colour
        else:
            self.state = "fin du tour"
            self.score.score_displayer()
        
        