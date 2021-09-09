import os

# 履歴ファイルパス
HISTORY_PATH = '.history.json'
# 設定ファイルパス
SETTINGS_PATH = '.settings.json'
# メール本文テンプレートパス
MAIL_TEMPLATE_PATH = os.path.join('template', 'dailyreport.txt')

# 日付フォーマット
DATE_FORMAT = '%Y/%m/%d'
TIME_FORMAT = '%H:%M'

# メール件名
MAIL_SUBJECT = '日報_{0}_{1}'
# エラーコード
EXCEL_ERROR = '100'

ERROR_MESSAGES = {
    '100': 'Excel 書き込み処理に失敗しました',
    '900': '予期せぬエラーが発生しました。',
}