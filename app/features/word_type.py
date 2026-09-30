from .word_list import liste_25_mot
import random


def cree_liste_couleur()->tuple[list]:
    blue_list = []
    red_list = []
    grey_list = []
    black_word = []
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
    return blue_list, red_list, grey_list, black_word


blue_list, red_list, grey_list, black_word = cree_liste_couleur()


if __name__ == "__main__":
    blue_list, red_list, grey_list, black_word = cree_liste_couleur()
    print(blue_list, red_list, grey_list, black_word)
