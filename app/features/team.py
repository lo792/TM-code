class Team:
    
    def __init__(self, color: str, player: Player, leader: Leader):
        self.player = player
        self.leader = leader
        self.color = color
        self.success_words = []
    
    def add_success_word(self, success_word: str):
        self.success_words.append(success_word)
    
    def get_leader(self) -> Leader:
        return self.leader
    
    def get_player(self) -> Player:
        return self.player


class Leader():
    
    def __init__(self, name: str):
        self.name = name


class Player():
    
    def __init__(self, name: str):
        self.name = name
        