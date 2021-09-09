import PySimpleGUI as sg
import json
from string import Template
from datetime import datetime as dt

from Common import constants
from Services import dailyreport_service
from Controllers import complete, error

now = dt.now()

def create_display():
    layout = [
        [
            sg.MenuBar([
                ['Option', ['settings']]
            ])
        ],
        [
            sg.Text('日付'), 
            sg.Input(key='work_day', default_text=now.strftime(constants.DATE_FORMAT), size=(20,)), 
            sg.CalendarButton('Date', target='work_day', format=constants.DATE_FORMAT)],
        [
            sg.Text('勤務時間'), 
            sg.Input(key='work_start_time', default_text='9:30', size=(7,)), 
            sg.Text('勤務終了'), 
            sg.Input(key='work_end_time', default_text=now.strftime(constants.TIME_FORMAT), size=(7,)), 
            sg.Text('休憩時間'), 
            sg.Input(key='breakout_time', default_text='1:00', size=(5,))],
        [
            sg.Text('業務内容')
        ],
        [
            sg.Multiline(key='detail', size=(50, 6))
        ],
        [
            sg.Text('翌営業日の予定')
        ],
        [
            sg.Multiline(key='next_day_plan', size=(50, 6))
        ],
        [
            sg.Text('問題点')
        ],
        [
            sg.Multiline(key='problems', size=(50, 4))
        ],
        [
            sg.Text('解決策')
        ],
        [
            sg.Multiline(key='solution', size=(50, 4))
        ],
        [
            sg.Text('その他')
        ],
        [
            sg.Multiline(key='others', size=(50, 6))
        ],
        [
            sg.Button('Submit', key='submit'),
            sg.Button('Clear', key='clear'),
            sg.Button('Restore', key='restore')
        ]
    ]

    return layout

def submit(window, value):
    # 入力の履歴を保存
    _save_history(value)

    # 日報送信処理
    error_code = dailyreport_service.report(value)

    if error_code:
        error.create_display(constants.ERROR_MESSAGES[error_code])
    else:
        complete.create_display('日報を送信しました。')

def clear(window, value):
    now = dt.now()
    window['work_day'].update(now.strftime(constants.DATE_FORMAT))
    window['work_end_time'].update(now.strftime(constants.TIME_FORMAT))
    window['detail'].update('')
    window['next_day_plan'].update('')
    window['problems'].update('')
    window['solution'].update('')
    window['others'].update('')

def restore(window, value):
    with open(constants.HISTORY_PATH, encoding='utf-8') as f:
        history = json.load(f)
    
    window['detail'].update(history['detail'])
    window['next_day_plan'].update(history['next_day_plan'])
    window['problems'].update(history['problems'])
    window['solution'].update(history['solution'])
    window['others'].update(history['others'])

def _save_history(values):
    with open(constants.HISTORY_PATH, encoding='utf-8') as f:
        history = json.load(f)

    history['detail'] = values['detail']
    history['next_day_plan'] = values['next_day_plan']
    history['problems'] = values['problems']
    history['solution'] = values['solution']
    history['others'] = values['others']

    with open(constants.HISTORY_PATH, 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=4)