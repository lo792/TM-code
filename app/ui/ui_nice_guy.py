from nicegui import ui

from features.word_type import blue_list, red_list, grey_list, black_word
from features.word_list import liste_25_mot
from features.game import Game

COLOR_HEX = {
    "red": "#e53935",
    "blue": "#1e88e5",
    "grey": "#9e9e9e",
    "black": "#212121",
}


def create_ui(game: Game) -> None:
    @ui.page("/")
    def index():
        state: dict = {"screen": "setup"}
    
        @ui.refreshable
        def score_panel():
            display_score(game)
            
        @ui.refreshable
        def word_panel():
            display_words_grid()

        def refresh_all():
            score_panel.refresh()
            word_panel.refresh()

        def start_game(names):
            for key in names:
                game.get_team(key).set_names(names[key]['player'], names[key]['leader'])
            #game.new_game()
            state["screen"] = "playing"
            start_screen.refresh()
        
        @ui.refreshable
        def start_screen():
            if state["screen"] == "setup":
                display_setup(game, start_game)
                return
            with ui.column().classes(
                "w-full max-w-4xl mx-auto items-stretch gap-3 p-4"
            ):
                score_panel()
                word_panel()

        start_screen()


def display_menu() -> None:
    """Top bar: title, role toggle, New game and Quit buttons."""
    with ui.row().classes("w-full items-center justify-between"):
        ui.label("🕵️  Code Name").classes("text-3xl font-bold")
  

def display_score(game: Game) -> None:
    with ui.card().classes("w-full"):
        with ui.row().classes("w-full items-center justify-between"):
            # whose turn / current team
            team = game.current_team()
            with ui.row().classes("items-center gap-2"):
                ui.badge(team.color).style(
                    f"background-color:{team.color};color:white;"
                    "font-size:1rem;padding:6px 12px;"
                )
                if game.state == "fin du tour":
                    phase_text = f"{team.get_leader().name} is giving a clue"
                elif game.state == "on continue":
                    phase_text = f"{team.get_player().name} is guessing"
                else:
                    phase_text = "game over"
                ui.label(phase_text).classes("text-lg")

            # scoreboard: hidden cards left per team
            with ui.row().classes("items-center gap-4"):
                for t in (game.current_team().color, game.not_current_team().color):
                    ui.label(f"{t}: {game.fois} left").style(
                        f"color:{t};font-weight:700;"
                    )

        # active clue
        if game.state == "on continue" and game.announce:
            ui.label(
                f'Clue: “{game.announce}”  ·  {game.fois} '
                f"guess{'es' if game.fois != 1 else ''} left"
            ).classes("text-xl font-semibold")

        # message / banner
        ui.separator()
        classes = "text-lg"
        if game.state == "fin du jeu":
            classes = "text-2xl font-bold"
        ui.label(game.state).classes(classes)


def player_click_change_color(e):
    if e.sender.text in blue_list:
        e.sender.props(remove='color=brown', add='color=blue')
    elif e.sender.text in red_list:
        e.sender.props(remove='color=brown', add='color=red')
    elif e.sender.text in grey_list:
        e.sender.props(remove='color=brown', add='color=grey')
    else:
        e.sender.props(remove='color=brown', add='color=black')
    e.sender.update()

        
def afficher_current_team():
    ui.label(f"c'est le tour de l'équipe {Game.current_team}")


def display_words_grid():
    for r in liste_25_mot:
        with ui.row().classes('w-full gap-2'):
            for w in r:
                ui.button(f"{w}", on_click=player_click_change_color, color='brown').style('width: 150px; height: 40px')
                    
    
def afficher_end_of_game():
        ui.label(f"Le jeu est terminé, l'équipe {Game.winner} a gagné!")
        Game.print_score()

  
def display_setup(game: Game, on_start) -> None:
    """aider du doc de Nicegui et exemple de git hub"""
    with ui.column().classes("w-full max-w-2xl mx-auto items-stretch gap-4 p-4"):
        ui.label("Code Name").classes("text-4xl font-bold text-center")

    inputs: dict = {}
    with ui.row().classes("grow"):
        for team in (game.current_team(), game.not_current_team()):
            ui.label(f"{team.color} team").classes("text-xl font-bold")
            leader = ui.input(
                "Leader",
                value=team.get_leader().name,
            ).props("outlined dense").classes("w-full")
            player = ui.input(
                "Player quel est ton nom? ",
                value=team.get_player().name,
            ).props("outlined dense").classes("w-full")
            inputs[team.color] = (leader, player)

    def start():
        names = {
            team: {"leader": inputs[team][0].value,
                    "player": inputs[team][1].value}
            for team in (game.current_team().color, game.not_current_team().color)
        }
        on_start(names)

    with ui.row().classes("w-full justify-center gap-3"):
        ui.button("Start game", icon="play_arrow", on_click=start).props("size=lg")
        ui.button("Quit", icon="power_settings_new", color="negative",
                    ).props("outline")
        

