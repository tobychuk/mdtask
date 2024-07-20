import math
import tkinter as tk
from tkinter import ttk


def area_heron(a, b, c):
    # sorted list of numbers
    ln = [a, b, c]
    for n in ln:
        if isinstance(n, int) or isinstance(n, float):
            pass
        else:
            return "Error. Value is not integer or float"
            exit()
    sln = sorted(ln)
    if sln[0]+sln[1]<sln[2]:
        return "Error. This Triangle doesnt exist"
    # checking if triangle is right
    if sln[0]*sln[0]+sln[1]*sln[1] == sln[2]*sln[2]:
        status = "right"
    elif sln[0]*sln[0]+sln[1]*sln[1] > sln[2]*sln[2]:
        status = "acute"
    else:
        status = "obtuse"
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - c) * (s - b) * (s - a))

    return f"Area of triangle with those values is {area}. Triangle is {status}"


def area_circle(r):
    pi = 3.1415

    return f"Area of circle with those value is {pi * (r*r)}"


import PySimpleGUI as sg
def callback_function1():

# All the stuff inside your window.
    layout = [ [sg.Text('Enter triangle sides')],
            [sg.Text('First side'), sg.InputText()],
                [sg.Text('Second side'), sg.InputText()],
                [sg.Text('Third side'), sg.InputText()],

                [sg.Button('Ok'), sg.Button('Cancel')] ]
    window = sg.Window('Area Calculator', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        else:
            try:
                sg.popup(area_heron(float(values[0]),float(values[1]),float(values[2])))
            except ValueError:
                sg.popup('You entered wrong value!')
    window.close()


def callback_function2():
    layout = [ [sg.Text('Enter circle radius')],
            [sg.Text('Radius'), sg.InputText()],

                [sg.Button('Ok'), sg.Button('Cancel')] ]
    window = sg.Window('Area Calculator', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        else:
            try:
                sg.popup(area_circle(float(values[0])))
            except ValueError:
                sg.popup('You entered wrong value!')
    window.close()


layout = [[sg.Text('Pick your action')],
          [sg.Button('Area of Triangle'), sg.Button('Area of Circle')]]

window = sg.Window('Area Calculator', layout)

while True:             # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Area of Triangle':
        callback_function1()        # call the "Callback" function
    elif event == 'Area of Circle':
        callback_function2()        # call the "Callback" function

window.close()

# # All the stuff inside your window.
# layout = [  [sg.Text('Enter triangle sides')],
#             [sg.Text('First side'), sg.InputText()],
#             [sg.Text('Second side'), sg.InputText()],
#             [sg.Text('Third side'), sg.InputText()],
#
#             [sg.Button('Ok'), sg.Button('Cancel')] ]
#
# # Create the Window
# window = sg.Window('Area Calculator', layout)
#
# # Event Loop to process "events" and get the "values" of the inputs
# while True:
#     event, values = window.read()
#     if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
#         break
#
#
#
#
# window.close()