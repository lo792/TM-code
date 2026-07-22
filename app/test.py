from nicegui import ui


def main():
    ui.label("Hello Loïse")
    ui.button('Click me!', on_click=lambda: ui.notify('You clicked me!'))

    ui.run()
    

main()
    