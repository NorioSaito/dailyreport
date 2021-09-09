from tkinter.constants import S
import PySimpleGUI as sg
import json

import handler
from Common import util
from Controllers import complete

def create_display(window, value):
    mail_settings = util.get_mail_settings()
    excel_settings = util.get_excel_settings()

    layout = [
        [
            sg.TabGroup([[
                sg.Tab('日報', [
                    [sg.Text('From', size=(10, 1)), sg.Input(key='mail_from', default_text=mail_settings['mail_from'], size=(100,))], 
                    [sg.Text('To', size=(10, 1)), sg.Input(key='mail_to', default_text=mail_settings['mail_to'], size=(100,))],
                    [sg.Text('Cc', size=(10, 1)), sg.Input(key='mail_cc', default_text=mail_settings['mail_cc'], size=(100,))],
                    [sg.Text('Name', size=(10, 1)), sg.Input(key='name', default_text=mail_settings['name'], size=(100,))],
                    # [sg.Text('Template', size=(10, 1)), sg.Multiline(key='template', default_text=util.read_report_template(), size=(100, 1000))]
                ]),
            sg.Tab('認証', [
                    [sg.Text('ホスト', size=(10, 1)), sg.Input(key='mail_host', default_text=mail_settings['mail_host'])], 
                    [sg.Text('ポート', size=(10, 1)), sg.Input(key='mail_port', default_text=mail_settings['mail_port'])], 
                    [sg.Text('ユーザ名', size=(10, 1)), sg.Input(key='mail_user', default_text=mail_settings['mail_user'])], 
                    [sg.Text('パスワード', size=(10, 1)), sg.Input(key='mail_password', default_text=mail_settings['mail_password'], password_char='●')]
                ]   ),
            sg.Tab('勤務表', [
                    [sg.Text('ファイル'), sg.Input(key='file_path', default_text=excel_settings['file_path']), sg.FileBrowse(target='file_path')]
                ])
            ]])
        ],
        [
            sg.Button('Save', key='save')
        ]
    ]

    window2 = sg.Window('Settings', layout, size=(500, 300))

    while True:
        event, value = window2.read()

        if event is None:
            break

        function = handler.handler[event]
        # 設定保存に成功したら終了
        if function(window2, value):
            break
    
    window2.close()

def save(window, values=None):
    print("here")
    if values:
        try:
            settings = util.read_settings()
            mail_settings = util.get_mail_settings()
            excel_settings = util.get_excel_settings()

            mail_settings['mail_from'] = values['mail_from']
            mail_settings['mail_to'] = values['mail_to']
            mail_settings['mail_cc'] = values['mail_cc']
            mail_settings['mail_user'] = values['mail_user']
            mail_settings['mail_password'] = values['mail_password']
            mail_settings['mail_host'] = values['mail_host']
            mail_settings['mail_port'] = values['mail_port']
            mail_settings['name'] = values['name']

            excel_settings['file_path'] = values['file_path']

            settings['mail_settings'] = mail_settings
            settings['excel_settings'] = excel_settings

            util.save_settings(settings)

            complete.create_display('設定を保存しました')
            return True
        except Exception:
            pass


