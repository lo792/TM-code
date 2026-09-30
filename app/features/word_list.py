import random

liste_de_mot_à_prendre = [
    "soleil", "lune", "étoile", "nuage", "pluie", "neige", "feu", "glace",
    "vent", "foudre", "océan", "rivière", "lac", "montagne", "désert",
    "forêt", "île", "plage", "volcan", "grotte", "château", "palais",
    "prison", "école", "hôpital", "banque", "musée", "cinéma", "théâtre",
    "restaurant", "hôtel", "gare", "aéroport", "métro", "pont", "tunnel",
    "tour", "phare", "église", "bibliothèque", "pirate", "roi", "reine",
    "prince", "princesse", "soldat", "espion", "détective", "médecin",
    "professeur", "astronaute", "pilote", "magicien", "robot", "fantôme",
    "vampire", "sorcière", "géant", "héros", "ninja", "chat", "chien",
    "cheval", "lion", "tigre", "éléphant", "singe", "serpent", "aigle",
    "requin", "dauphin", "baleine", "poulpe", "araignée", "papillon",
    "abeille", "fourmi", "loup", "renard", "ours", "pomme", "banane",
    "orange", "citron", "fraise", "cerise", "raisin", "pastèque",
    "chocolat", "fromage", "pizza", "burger", "sushi", "gâteau", "glace",
    "pain", "café", "thé", "sel", "poivre", "épée", "bouclier", "pistolet",
    "bombe", "couteau", "marteau", "clé", "corde", "boussole", "carte",
    "lampe", "miroir", "lunettes", "montre", "téléphone", "ordinateur",
    "caméra", "parapluie", "valise", "parachute", "voiture", "moto", "vélo",
    "train", "avion", "bateau", "fusée", "hélicoptère", "bus", "taxi",
    "ambulance", "tracteur", "skateboard", "trottinette", "sous-marin",
    "tram", "camion", "yacht", "canoë", "montgolfière", "amour", "guerre",
    "paix", "mort", "vie", "temps", "chance", "secret", "peur", "joie",
    "colère", "liberté", "pouvoir", "argent", "mystère", "rêve", "mensonge",
    "vérité", "danger", "aventure", "musique", "danse", "film", "livre",
    "peinture", "photo", "chanson", "guitare", "piano", "batterie", "micro",
    "concert", "spectacle", "masque", "costume", "couronne", "statue",
    "tableau", "scène", "diamant", "or", "perle", "trésor", "anneau",
    "coffre", "pièce", "billet", "laser", "dragon", "monstre", "licorne",
    "alien", "zombie", "sorcier"
]


def cree_list_de_25_mot()->list[str]:
    liste_25 = []
    liste_à_prendre = [item for item in liste_de_mot_à_prendre]
    for i in range(5):
        ligne = []
        for j in range(5):
            mot = random.choice(liste_à_prendre)
            ligne.append(mot)
            liste_à_prendre.remove(mot)
        liste_25.append(ligne)
    return liste_25


liste_25_mot = cree_list_de_25_mot()
