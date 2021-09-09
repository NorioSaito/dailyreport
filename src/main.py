import PySimpleGUI as sg
import json
from logging import getLogger, config

from Controllers import dailyreport, error
import handler

with open('log_config.json', encoding='utf-8') as f:
        log_config = json.load(f)

config.dictConfig(log_config)
logger = getLogger(__name__)
logger.info('message')

if __name__ == '__main__':
    # メイン画面描画
    layout = dailyreport.create_display()
    window = sg.Window('日報さん Desktop', layout=layout)
    
    while True:
        event, value = window.read()
        if event is None:
            break
        
        try:
            function = handler.handler[event]
            function(window, value)
        except Exception as e:
            logger.error(e)
            error.create_display('予期せぬエラーが発生しました')
    window.close()