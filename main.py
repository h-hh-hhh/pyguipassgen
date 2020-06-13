import tkinter, random
import PySimpleGUI as sg

layout = [[sg.Text('Enter characters to be included in the password'),sg.Input('abcdefhijklmnopqrstuvwxyzABCDEFHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&')],
         [sg.Text('Enter length of password'),sg.Input('8')],
         [sg.Text('Generated password:'),sg.Input(key='_GENERATED_')],
         [sg.Button('Generate')]]

window = sg.Window('Password Generator', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    if event == 'Generate':
        values[1] = ''.join(random.choice(values[0]) for i in range(int(values[1])))
        window.Refresh()
        window['_GENERATED_'].Update(values[1])