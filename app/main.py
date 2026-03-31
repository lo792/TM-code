from ui.leader_screen import print_leader_screen
from features.team import choisir_prenoms
from ui.team_displayer import display_teams


if __name__== "__main__":
    print("Bienvenue dans Code Game:")
    prenoms_joueurs_et_leaders = choisir_prenoms()
    display_teams(prenoms_joueurs_et_leaders)
    
    keep_on = True
    
    while keep_on:
        # ...
        if jeu_fini:
            kee_on = False
    
    print(f"Le jeu est terminé, l'équipe {gagnant} a gagné!")
    
