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
    
    def set_names(self, player_name: str, leader_name: str):
        self.player.set_name(player_name)
        self.leader.set_name(leader_name)


class Person():
    def __init__(self, name: str):
        self.name = name
    
    def set_name(self, name: str):
        self.name = name


class Leader(Person):
    def __init__(self, name: str):
        super().__init__(name)


class Player(Person):
    def __init__(self, name: str):
        super().__init__(name)
