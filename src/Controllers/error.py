import PySimpleGUI as sg

def create_display(message):
    layout = [
        [sg.Text(message)],
        [sg.Button('Close')]
    ]

    complete = sg.Window('Error!', layout, size=(300, 150))

    while True:
        event, value = complete.read()

        if (event is None) or (event == 'Close'):
            break
    
    complete.close()
