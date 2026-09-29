import random

liste_de_mot_à_prendre = [
    "Soleil", "Lune", "Étoile", "Nuage", "Pluie", "Neige", "Feu", "Glace",
    "Vent", "Foudre", "Océan", "Rivière", "Lac", "Montagne", "Désert",
    "Forêt", "Île", "Plage", "Volcan", "Grotte", "Château", "Palais",
    "Prison", "École", "Hôpital", "Banque", "Musée", "Cinéma", "Théâtre",
    "Restaurant", "Hôtel", "Gare", "Aéroport", "Métro", "Pont", "Tunnel",
    "Tour", "Phare", "Église", "Bibliothèque", "Pirate", "Roi", "Reine",
    "Prince", "Princesse", "Soldat", "Espion", "Détective", "Médecin",
    "Professeur", "Astronaute", "Pilote", "Magicien", "Robot", "Fantôme",
    "Vampire", "Sorcière", "Géant", "Héros", "Ninja", "Chat", "Chien",
    "Cheval", "Lion", "Tigre", "Éléphant", "Singe", "Serpent", "Aigle",
    "Requin", "Dauphin", "Baleine", "Poulpe", "Araignée", "Papillon",
    "Abeille", "Fourmi", "Loup", "Renard", "Ours", "Pomme", "Banane",
    "Orange", "Citron", "Fraise", "Cerise", "Raisin", "Pastèque",
    "Chocolat", "Fromage", "Pizza", "Burger", "Sushi", "Gâteau", "Glace",
    "Pain", "Café", "Thé", "Sel", "Poivre", "Épée", "Bouclier", "Pistolet",
    "Bombe", "Couteau", "Marteau", "Clé", "Corde", "Boussole", "Carte",
    "Lampe", "Miroir", "Lunettes", "Montre", "Téléphone", "Ordinateur",
    "Caméra", "Parapluie", "Valise", "Parachute", "Voiture", "Moto", "Vélo",
    "Train", "Avion", "Bateau", "Fusée", "Hélicoptère", "Bus", "Taxi",
    "Ambulance", "Tracteur", "Skateboard", "Trottinette", "Sous-marin",
    "Tram", "Camion", "Yacht", "Canoë", "Montgolfière", "Amour", "Guerre",
    "Paix", "Mort", "Vie", "Temps", "Chance", "Secret", "Peur", "Joie",
    "Colère", "Liberté", "Pouvoir", "Argent", "Mystère", "Rêve", "Mensonge",
    "Vérité", "Danger", "Aventure", "Musique", "Danse", "Film", "Livre",
    "Peinture", "Photo", "Chanson", "Guitare", "Piano", "Batterie", "Micro",
    "Concert", "Spectacle", "Masque", "Costume", "Couronne", "Statue",
    "Tableau", "Scène", "Diamant", "Or", "Perle", "Trésor", "Anneau",
    "Coffre", "Pièce", "Billet", "Laser", "Dragon", "Monstre", "Licorne",
    "Alien", "Zombie", "Sorcier"]


def cree_list_de_25_mot()->list[str]:
    liste_25_mot = []
    for i in range(5):
        ligne = []
        for j in range(5):
            mot = random.choice(liste_de_mot_à_prendre)
            ligne.append(mot)
        liste_25_mot.append(ligne)
    return liste_25_mot


