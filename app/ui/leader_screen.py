from features.word_type import blue_list, red_list, grey_list, black_word
from features.word_list import liste_25_mot


def print_leader_screen (title: str, ):
    print(title)
    for sequence in liste_25_mot:
        for mot in sequence:
            if mot in blue_list:
                print(f"[blue]{mot} ", end='')
            elif mot in red_list:
                print(f"[red]{mot} ", end='')
            elif mot in grey_list:
                print(f"[grey]{mot} ", end='')
            else:
                print(f"[black]{mot} ", end='')
        print()