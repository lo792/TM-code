'''from nicegui import ui
from features.word_type import black_word, blue_list, red_list, grey_list
    
def changer_de_couleur(e):
    if e.sender.text in blue_list:
        e.sender.props(remove='color=blue', add='color=purple')
        e.sender.update()
    elif e.sender.text in red_list:
        e.sender.props(remove='color=blue', add='color=red')
        e.sender.update()
    else:
        e.sender.props(remove='color=blue', add='color=black')
        e.sender.update()

with ui.row().classes('w-screen h-screen justify-center items-center'):
    with ui.grid(columns=5).classes('gap-10'):
    
        ui.button('maison', on_click=changer_de_couleur)
        ui.button('voiture', on_click=changer_de_couleur)
        ui.button('chien', on_click=changer_de_couleur)
        ui.button('porte', on_click=changer_de_couleur)
        ui.button('rue', on_click=changer_de_couleur)
    
        ui.button('fenêtre', on_click=changer_de_couleur)
        ui.button('pomme', on_click=changer_de_couleur)
        ui.button('londre', on_click=changer_de_couleur)
        ui.button('Height:', on_click=changer_de_couleur)
        ui.button('1.80m', on_click=changer_de_couleur)
    
        ui.button('salut', on_click=changer_de_couleur)
        ui.button('pomme', on_click=changer_de_couleur)
        ui.button('londre', on_click=changer_de_couleur)
        ui.button('Height:', on_click=changer_de_couleur)
        ui.button('1.80m', on_click=changer_de_couleur)
    
        ui.button('salut')
        ui.button('pomme')
        ui.button('londre')
        ui.button('Height:')
        ui.button('1.80m')
    
        ui.button('salut')
        ui.button('pomme')
        ui.button('londre')
        ui.button('Height:')
        ui.button('1.80m')

ui.label("bienvenu")
with ui.row():
    ui.button("quitter", color="red")
    ui.button("entrer", color="blue")
    ui.button("jouer", color="green")
    
name = ui.input("Quel est ton nom?")
message = ui.label("")
def dire_bonjour(prenom):
    message.set_text(f"Bonjour {prenom.value}")
name.on('keydown.enter', lambda: dire_bonjour(name))

ui.run()'''
from features.word_type import blue_list, red_list, grey_list, black_word
from nicegui import ui

import  ui.ui_nice_guy

def player_click_change_color(e):
    if e.sender.text in blue_list:
        e.sender.props(remove='color=blue', add='color=purple')
        e.sender.update()
    elif e.sender.text in red_list:
        e.sender.props(remove='color=blue', add='color=red')
        e.sender.update()
    else:
        e.sender.props(remove='color=blue', add='color=black')
        e.sender.update()
        
def afficher_title():
    ui.label("Bienvenu dans codename!")

def boutton_jouer():
    jouer = ui.button()
    jouer("jouer", on_click=input_name() and jouer.visible == False)
    
def input_name():
    name = ui.input("Quel est ton nom?")
    message = ui.label("")
    def dire_bonjour(prenom):
        message.set_text(f"Bonjour {prenom.value}")
    name.on('keydown.enter', lambda: dire_bonjour(name))
    name.visible = False

if __name__== "__main__":
    pass
