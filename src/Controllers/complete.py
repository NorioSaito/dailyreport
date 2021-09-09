import PySimpleGUI as sg

def create_display(text):
    layout = [
        [sg.Text(text)],
        [sg.Button('OK')]
    ]

    complete = sg.Window('Complete!', layout, size=(300, 150))

    while True:
        event, value = complete.read()

        if (event is None) or (event == 'OK'):
            break
    
    complete.close()
