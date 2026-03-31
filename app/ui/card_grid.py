from features.word_list import liste_25_mot


def print_word_grid():
    for i in range(len(liste_25_mot)):
        ligne =liste_25_mot[i]
        for j in range(len(ligne)):
            print(ligne[j]+" ", end="")
        print()