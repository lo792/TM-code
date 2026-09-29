from features.word_list import cree_list_de_25_mot
import random


def cree_liste_couleur()->tuple[list]:
    blue_list = []
    red_list = []
    grey_list = []
    black_word = []
    liste_25_mot = cree_list_de_25_mot()
    for j in range(8):
        mot_blue = random.choice(liste_25_mot)
        blue_list.append(mot_blue)
        liste_25_mot.remove(mot_blue)
        mot_red = random.choice(liste_25_mot)
        red_list.append(mot_red)
        liste_25_mot.remove(mot_red)
        mot_grey = random.choice(liste_25_mot)
        grey_list.append(mot_grey)
        liste_25_mot.remove(mot_grey)
    black = random.choice(liste_25_mot)
    black_word.append(black)
    return blue_list, red_list, grey_list, black_word
