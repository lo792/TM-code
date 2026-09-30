from nicegui import ui
from features.word_type import blue_list, red_list, grey_list, black_word
from features.word_list import liste_25_mot
from features.game import Game
from features.game_factory import Game_factory


def create_ui(game: Game) -> None:
    state: dict = {"screen": "setup"}
    
    def get_card_color(word: str) -> str:
        if word in blue_list:
            return "blue"
        elif word in red_list:
            return "red"
        elif word in grey_list:
            return "grey"
        elif word in black_word:
            return "black"
        return "brown"

    def is_word_found(word: str) -> bool:
        all_found = game.teams[0].success_words + game.teams[1].success_words + game.teams[0].fail_words + game.teams[1].fail_words
        return word in all_found

    # fenêtre player (http://localhost:8080/player)

    @ui.page("/player")
    def player_page():
         # Carte non trouvée
        def make_click_handler(word):
            def handle_click():
                if game.state != "on continue":
                    ui.notify("Attendez le tour de jeu !", color="warning")
                    return
                # Vérification avec la fonction check de game.py
                game.check(word, game.fois)

                if game.state == "on continue":
                    game.fois -= 1
                    if game.fois <= 0:
                        game.state = "fin du tour"
                        game.tour_nb += 1
                elif game.state == "fin du tour":
                    game.tour_nb += 1
                render_player.refresh()
            return handle_click

        @ui.refreshable
        def render_player():
            if state["screen"] == "setup":
                def on_start(names):
                    for key in names:
                        game.get_team(key).set_names(names[key]['player'], names[key]['leader'])
                    state["screen"] = "playing"
                    render_player.refresh()

                display_setup(game, on_start)
                return

            with ui.column().classes("w-full max-w-4xl mx-auto items-stretch gap-4 p-4"):
                display_menu()
                display_score_view(game)

                # Écran de fin de partie
                if game.state == "fin du jeu":
                    def on_start(names):
                        for key in names:
                            game.get_team(key).set_names(names[key]['player'], names[key]['leader'])
                        state["screen"] = "playing"
                        render_player.refresh()
                    
                    winner_color = getattr(game, 'winner', 'Inconnu')
                    
                    # AJOUTER - ON RECREE LE JEU nonlocal C'EST LA CLEF POUR REDEFINIR LE GAME: on prend le game pas local donc définit tout en haut
                    def restart_game():
                        nonlocal game
                        # CHANGE LA FACTORY POUR POUVOIR DONNER DES NOMS COMME çA SI LES JOUEURS NE CHANGENT PAS ALORS ILS REAPPARAISSENT
                        game = Game_factory.get_game(
                            game.teams[0].get_leader().name,
                            game.teams[0].get_player().name,
                            game.teams[1].get_leader().name,
                            game.teams[1].get_player().name
                        )
                        state["screen"] = "setup" # ON REMET setup POUR FORCER LE RECOMMENCEMENT
                        render_player.refresh()
    
                    with ui.card().classes("w-full text-center bg-amber-100 p-6"):
                        ui.label(f"🏆 Partie terminée ! Victoire de l'équipe {winner_color.upper()} !").classes("text-3xl font-bold text-amber-900")
                        # LE BOUTON DE RECOMMENCER: CLICK => restart_game()
                        ui.button("Recommencer une partie", icon="replay", on_click=restart_game, color="primary").props("size=lg")
                    # RETURN PERMET DE QUITTER ET DE NE PAS AFFICHER CE QU'IL Y A DESSOUS
                    return

                # Tour en attente de l'indice du leader
                elif game.state == "fin du tour":
                    with ui.card().classes("w-full text-center p-4 bg-gray-100"):
                        ui.label(f"⏳ C'est au Leader {game.current_team().color.upper()} ({game.current_team().get_leader().name}) de donner un indice sur son écran...").classes("text-lg")
                        ui.button("Actualiser l'écran", on_click=render_player.refresh).props("outline")

                # Tour du player qui devine
                else:
                    with ui.row().classes("w-full justify-between items-center bg-blue-50 p-3 rounded"):
                        ui.label(f" Indice : {game.announce} ({game.fois} essai(s) restant(s))").classes("text-xl font-bold")

                        def end_turn():
                            game.state = "fin du tour"
                            game.tour_nb += 1
                            render_player.refresh()

                        ui.button("Passer le tour", on_click=end_turn, color="warning").props("outline")

                # Grille des cartes
                for r in liste_25_mot:
                    with ui.row().classes("w-full gap-2 justify-center"):
                        for mot_de_la_ligne in r:
                            found = is_word_found(mot_de_la_ligne)
                            real_color = get_card_color(mot_de_la_ligne)

                            if found:
                                # Carte déjà trouvée
                                ui.button(text=mot_de_la_ligne, color=real_color).props("unelevated").classes("w-32 h-14 opacity-75")
                            else:
                                ui.button(text=mot_de_la_ligne, color="brown", on_click=make_click_handler(mot_de_la_ligne)).classes("w-32 h-14")

        render_player()

    # fenêtre leader (http://localhost:8080/leader)

    @ui.page("/leader")
    def leader_page():
        @ui.refreshable
        def render_leader():
            if state["screen"] == "setup":
                with ui.column().classes("w-full max-w-xl mx-auto items-center gap-4 p-8"):
                    ui.label("Code Name - Vue Leader").classes("text-3xl font-bold")
                    ui.label("En attente de configuration sur l'écran joueur...").classes("text-lg text-gray-500")
                    ui.button("Rejoindre la partie", on_click=render_leader.refresh).props("size=lg color=primary")
                return

            with ui.column().classes("w-full max-w-4xl mx-auto items-stretch gap-4 p-4"):
                display_menu()
                display_score_view(game)

                # Panneau pour ecrire l'indice pour le leader
                if game.state == "fin du tour":
                    with ui.card().classes("w-full bg-blue-50 p-4"):
                        ui.label(f" Tour du Leader {game.current_team().color.upper()} ({game.current_team().get_leader().name})").classes("text-lg font-bold")
                        with ui.row().classes("w-full items-center gap-3"):
                            input_clue = ui.input("Mot Indice").classes("grow")
                            input_count = ui.number("Nombre de cartes", value=1, min=1, max=8).classes("w-32")

                            def send_clue():
                                if not input_clue.value or not game.verify_annonce(input_clue.value):
                                    ui.notify("Veuillez entrer un mot indice différent!", color="negative")
                                    return
                                game.set_announce(str(input_clue.value), int(input_count.value))
                                game.state = "on continue"
                                render_leader.refresh()

                            ui.button("Envoyer l'indice", on_click=send_clue, color="primary").props("size=md")
                elif game.state == "on continue":
                    with ui.card().classes("w-full text-center p-3 bg-gray-100"):
                        ui.label(f"Indice actif : {game.announce} ({game.fois} restant(s)) - Le joueur devine...").classes("text-lg")
                        ui.button("Actualiser la vue", on_click=render_leader.refresh).props("outline")

                # Écran de fin de partie
                if game.state == "fin du jeu":
                    winner_color = getattr(game, 'winner', 'Inconnu')
                    with ui.card().classes("w-full text-center bg-amber-100 p-6"):
                        ui.label(f"🏆 Partie terminée ! Victoire de l'équipe {winner_color.upper()} !").classes("text-3xl font-bold text-amber-900")
                    
                # Grille visible par le Leader (toutes les vraies couleurs)
                for r in liste_25_mot:
                    with ui.row().classes("w-full gap-2 justify-center"):
                        for w in r:
                            c = get_card_color(w)
                            found = is_word_found(w)

                            # Si trouvé, on ajoute une couleur differente
                            label_text = f"✓ {w}" if found else f"{w}"
                            btn = ui.button(text=label_text, color=c).props("unelevated").classes("w-32 h-14")
                            if found:
                                btn.classes("opacity-40")

        render_leader()


def display_menu() -> None:
    with ui.row().classes("w-full items-center justify-between"):
        ui.label("Code Name").classes("text-3xl font-bold")


def display_score_view(game: Game) -> None:
    with ui.card().classes("w-full"):
        with ui.row().classes("w-full items-center justify-between"):
            current = game.current_team()
            with ui.row().classes("items-center gap-2"):
                ui.badge(current.color.upper()).style(
                    f"background-color:{current.color};color:white;"
                    "font-size:1rem;padding:6px 12px;"
                )
                phase_text = f"Tour de l'équipe {current.color.upper()}"
                ui.label(phase_text).classes("text-lg font-medium")

            # Mots trouvés par équipe
            with ui.row().classes("items-center gap-6"):
                for team in game.teams:
                    ui.label(f"{team.color.upper()} : {len(team.success_words)} trouvés").style(f"color:{team.color};font-weight:700;")


def display_setup(game: Game, on_start) -> None:
    with ui.column().classes("w-full max-w-2xl mx-auto items-stretch gap-4 p-4"):
        ui.label("Configuration de la partie").classes("text-4xl font-bold text-center")

        inputs: dict = {}
        for team in game.teams:
            with ui.card().classes("w-full p-4"):
                ui.label(f"Équipe {team.color.upper()}").classes("text-xl font-bold")
                leader = ui.input("Nom du Leader", value=team.get_leader().name).props("outlined dense").classes("w-full mb-2")
                player = ui.input("Nom du Joueur", value=team.get_player().name).props("outlined dense").classes("w-full")
                inputs[team.color] = (leader, player)

        def start():
            names = {
                team.color: {
                    "leader": inputs[team.color][0].value,
                    "player": inputs[team.color][1].value
                }
                for team in game.teams
            }
            on_start(names)

        with ui.row().classes("w-full justify-center gap-3"):
            # UTILISER link POUR OUVRI PAGE LEADER ET NEW TAB TRUE POUR OUVRIR NOUVEL ONGLET
            ui.link("Ouvrir ce lien pour la page des leaders:", "http://localhost:8080/leader", new_tab=True)
                    
        with ui.row().classes("w-full justify-center gap-3"):
            ui.button("Commencer la partie", icon="play_arrow", on_click=start).props("size=lg color=primary")
