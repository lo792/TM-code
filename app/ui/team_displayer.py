from ui.leader_screen import print_leader_screen
from ui.player_screen import print_player_screen


def display_teams(liste_roles: list):
    print("Ecrans pour chaque joueurs:")
    for role in liste_roles:
        if 'leader' in role:
            print_leader_screen(role)
        elif 'player' in role:
            print_player_screen(role)
            