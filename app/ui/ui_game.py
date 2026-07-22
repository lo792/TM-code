from features.word_type import blue_list, red_list, grey_list, black_word
from features.word_list import liste_25_mot
from features.team import Leader, Team, Player
from features.game import Game
        

class Ui_game():
     
    def __init__(self, game: Game):
        self.game: Game = game
    
    def print_title(self):
        print("Bienvenue dans Code Game:")
    
    def print_next_playing_team(self):
        print(f"c'est le tour de l'équipe: {self.game.current_team().color}")
    
    @staticmethod     
    def input_teams() -> dict:
        return {
            "leader_blue": input("Quel est ton nom leader bleu? "),
            "player_blue": input("Quel est ton nom joueur bleu? "),
            "leader_red": input("Quel est ton nom leader rouge? "),
            "player_red": input("Quel est ton nom joueur rouge? ")
        }
    
    def print_current_team(self):
        print(self.game.current_team().leader.name)
        print(self.game.current_team().player.name)
        print(self.game.current_team().color)
    
    def print_not_current_team(self):
        print(self.game.not_current_team().leader.name)
        print(self.game.not_current_team().player.name)
        print(self.game.not_current_team().color)
    
    def print_current_team_words_list(self):
        pass
    
        
    def print_leader_screen(self):
        for sequence in liste_25_mot:
            for mot in sequence:
                if mot in blue_list:
                    print(f"[blue]{mot} ", end='')
                elif mot in red_list:
                    print(f"[red]{mot} ", end='')
                elif mot in grey_list:
                    print(f"[grey]{mot} ", end='')
                else:
                    print(f"[black]{mot} ", end='')
            print()
    
    def print_current_team_leader_announce(self) -> dict:
        mot=input("un mot: ")
        #announce = game.verify_annonce(announce)
        fois=int(input("cb de fois? "))
        print(f"{mot}, {fois}")
        return {
            "mot": mot,
            "fois": fois
        }
    
    def print_player_screen(self):
        for i in range(len(liste_25_mot)):
            ligne =liste_25_mot[i]
            for j in range(len(ligne)):
                print(ligne[j]+" ", end="")
            print()
          
    def print_end_of_game(self):
        print(f"Le jeu est terminé, l'équipe {self.game.winner} a gagné!")
        self.print_score()
          
    def input_player_guess_word(self) -> str:
        word_to_check = input("un mot a selectionné ")
        while not self.game.verify_word_to_guess(word_to_check):
            print("Le mot a déjà été deviné ou n'est pas dans la grille")
            word_to_check = input("un mot a selectionné ")
        return word_to_check
            
    def print_score(self):
        red_score = len(self.game.teams[0].success_words)
        blue_score = len(self.game.teams[1].success_words)
        print(f"le score de l'equipe red est de: {red_score} mots et celui de l'equipe bleu est: {blue_score}")
    
    


class Ui_team():
    
    def __init__(self, team: Team):
        self.team: Team = team
    
    def discribe(self):
        self.leader.description()
        self.player.description()
        print(self.colour)
        

class Ui_leader:
    
    def __init__(self, leader: Leader):
        self.leader: Leader = leader

    def announce(self) -> dict:
        mot=input("un mot")
        fois=int(input("cb de fois?"))
        return {
            'mot': mot,
            'fois': fois
        }
    
    def describe(self):
        print(f"{self.leader.name} tu es leader")
        
    def print_leader_screen ():
        for sequence in liste_25_mot:
            for mot in sequence:
                if mot in blue_list:
                    print(f"[blue]{mot} ", end='')
                elif mot in red_list:
                    print(f"[red]{mot} ", end='')
                elif mot in grey_list:
                    print(f"[grey]{mot} ", end='')
                else:
                    print(f"[black]{mot} ", end='')
            print()



class Ui_player:
    
    def __init__(self, player: Player):
        self.player: Player = player
       
    def guess_word(self):
        return input("un mot a selectionné ")
    
    def describe(self):
        print(f"{self.player.name} tu es player")
        
    def print_player_screen():
        print_word_grid()
    