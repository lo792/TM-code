class Team:
    
    def __init__(self, colour: str, player: Player, leader: Leader):
        self.player = player
        self.leader = leader
        self.colour = colour
        self.success_words = []
    
    def add_success_word(self, success_word: str):
        self.success_words.append(success_word)
    
    def get_leader(self) -> Leader:
        return self.leader
    
    def get_player(self) -> Player:
        return self.player
    
    def describe(self):
        self.leader.description()
        self.player.description()
        print(self.colour)

class Leader:
    
    def __init__(self, name):
        self.name = name
        
    def announce(self) -> dict:
        mot=input("un mot")
        fois=int(input("cb de fois?"))
        return {
            'mot': mot,
            'fois': fois
        }
    
    def description(self):
        print(f"{self.name} tu es leader")

class Player:
    
    def __init__(self, name):
        self.name = name
       
    def guess_word(self):
        return input("un mot a selectionné ")
    
    def description(self):
        print(f"{self.name} tu es player")
    