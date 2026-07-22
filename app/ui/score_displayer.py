
class Score:
    def __init__ (self, game):
        self.game = game
        
    def score_displayer(self):
        red_score = len(self.game.teams[0].success_words)
        blue_score = len(self.game.teams[1].success_words)
        print(f"le score actuel de l'equipe red est de: {red_score} mots et celui de l'equipe bleu est: {blue_score}")