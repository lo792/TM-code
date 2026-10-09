from .word_list import cree_list_de_25_mot
import random


def cree_liste_couleur()->tuple[list]:
    blue_list = []
    red_list = []
    grey_list = []
    black_word = []
    liste_25_mot = cree_list_de_25_mot()
    
    flat_liste_25 = [item for sublist in liste_25_mot for item in sublist]
    for i in range(8):
        mot_blue = random.choice(flat_liste_25)
        blue_list.append(mot_blue)
        flat_liste_25.remove(mot_blue)
        mot_red = random.choice(flat_liste_25)
        red_list.append(mot_red)
        flat_liste_25.remove(mot_red)
        mot_grey = random.choice(flat_liste_25)
        grey_list.append(mot_grey)
        flat_liste_25.remove(mot_grey)
    black = random.choice(flat_liste_25)
    black_word.append(black)
    return liste_25_mot, blue_list, red_list, grey_list, black_word


if __name__ == "__main__":
    blue_list, red_list, grey_list, black_word = cree_liste_couleur()
    print(blue_list, red_list, grey_list, black_word)
