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
        [
            sg.Button('-', font=font_body, key='-subtract-'),
            sg.Input(1, font=font_body, key='-tickets-', enable_events=True),
            sg.Button('+', font=font_body, key='-add-'),
            # sg.Button('Check', font=font_body, key='-check-')
        ],
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

def update_task2(train_index, ticket):
    window['-caution-'].update(value='')
    try:
        tickets_value = int(window['-tickets-'].get()) + int(ticket)
        if tickets_value < 1:
            tickets_value = 1
        window['-tickets-'].update(value=tickets_value)
        price = emr.main.check_ticket(train_index, tickets_value)
        train = emr.data[train_index]
        available = train['ticket'] - tickets_value
        window['-price-'].update(value=f'The price of train{train_index + 1} is {price}.')
        window['-available-'].update(value=f'The available tickets of train{train_index + 1} is {available}.')
        return tickets_value
    except ValueError as e:
        window['-caution-'].update(value=str(e))
    return 0

layout = [
    [
        sg.Column(build_task1(), key='-task1-', visible=True),
        sg.Column(build_task2(), key='-task2-', visible=False),
        sg.Column(build_task3(), key='-task3-', visible=False),
    ]
]

window = sg.Window('Electric mountain railway(by Lily)', layout, size=(800, 600))


def main_loop():
    train_index = 0 
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
            train_index = int(event[-2])
            update_task2(train_index, 0)
        elif event == '-back-':
            change_task(1)
        elif event == '-subtract-':
            update_task2(train_index, -1)
        elif event == '-add-':
            update_task2(train_index, 1)
        elif event == '-tickets-':
            update_task2(train_index, 0) 
        elif event == '-buy-':
            ticket = update_task2(train_index, 0)
            if ticket > 0:
                emr.main.buy_ticket(train_index, ticket)
                change_task(1)
    window.close()