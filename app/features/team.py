def choisir_prenoms() -> list:
    type = ['bleu', 'rouge']
    equipe = ['player', 'leader']
    resultat = []
    print("Merci d'entrer les joueurs")
    for e in equipe:
        for t in type:
            d = input(f"{e} {t}: ")
            resultat.append(f"{e} {t}: {d}")
    return resultat   