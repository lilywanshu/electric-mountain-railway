#=================================
# GUI for emr
# author: Lily
# created: 2022.2.3
#=================================

import PySimpleGUI as sg      
from emr import SCHEDULE
import emr.main
import emr

sg.theme('DarkAmber')    # Keep things interesting for your users
font_title = ('Arial', 40)
font_body = ('Arial', 20)

def build_task1():
    rows = [
        [sg.Text('START OF THE DAY', font=font_title)],
    ]
    up = SCHEDULE['up']
    down = SCHEDULE['down']
    for i in range(len(down)):
        available = emr.data[i]['ticket']
        sold = emr.AVAILABLE_INNITIAL - available
        rows.append([
            sg.Text(f'UP {up[i]}    DOWN {down[i]}', font=font_body),
            sg.Text(f'Available {available}    Sold {sold}', font=font_body),
            sg.Button('Purchase', font=font_body, key=f'-purchase{i}-')
        ])
    rows.append([sg.Button('END', font=font_body)])
    return rows

def build_task2():
    rows = [
        [sg.Text('PURCHASING TIME', font=font_title)],
        [sg.Text('', key='-available-', font=font_body)],
        [sg.Text('', key='-price-', font=font_body)],
        [sg.Button('-', font=font_body, key='-subtract-'), sg.Input(1, font=font_body, key='-tickets-'), sg.Button('+', font=font_body, key='add')],
        [sg.Text('', key='-caution-', font=font_body, text_color='red')],
        [sg.Button('Buy', key='-buy-', font=font_body)],
        [sg.Button('Back', key='-back-', font=font_body)]
    ]
    return rows

def build_task3():
    rows = [
        [sg.Text('END OF THE DAY', font=font_title)],
    ]
    up = SCHEDULE['up']
    down = SCHEDULE['down']
    for i in range(len(down)):
        available = emr.data[i]['ticket']
        sold = emr.AVAILABLE_INNITIAL - available
        rows.append([
            sg.Text(f'UP {up[i]}    DOWN {down[i]}', font=font_body),
            sg.Text(f'Sold {sold}   ', font=font_body), sg.Text('price ', key='-everyprice-', font=font_body),
            sg.Text('CLOSED', font=font_body, text_color='grey')
        ])
    rows.append([sg.Text('Total price ', font=font_body, key='-totalprice-'), sg.Text('Total tickets ', font=font_body, key='-totaltickets-')])
    rows.append([sg.Button('START', font=font_body, key='-start-')])
    return rows

def change_task(task_index):
    for i in (1, 2, 3):
        window[f'-task{i}-'].update(visible=False)
    window[f'-task{task_index}-'].update(visible=True)


layout = [
    [
        sg.Column(build_task1(), key='-task1-', visible=True),
        sg.Column(build_task2(), key='-task2-', visible=False),
        sg.Column(build_task3(), key='-task3-', visible=False),
    ]
]

window = sg.Window('Electric mountain railway(by Lily)', layout, size=(800, 600))


def main_loop():
    while True:                             # The Event Loop
        event, values = window.read() 
        print(event, values)       
        if event == sg.WIN_CLOSED:
            break      
        if event == 'END':
            change_task(3)
        elif event == '-start-':
            change_task(1)
        elif event.startswith('-purchase'):
            change_task(2)
        elif event == '-back-':
            change_task(1)
    window.close()