import smtplib
from email.mime.text import MIMEText
from string import Template
from datetime import datetime as dt

from Common import util, constants

def send_mail(values):
    # メール設定読み込み
    mail_settings = util.get_mail_settings()

    body = _create_body(values, mail_settings['name'])
    msg = MIMEText(body)

    msg['Subject'] = _create_subject(values['work_day'], mail_settings['name'])
    msg['To'] = mail_settings['mail_to']
    msg['Cc'] = mail_settings['mail_cc']
    msg['From'] = mail_settings['mail_from']

    # サーバを指定
    server = smtplib.SMTP(mail_settings['mail_host'], mail_settings['mail_port'])
    # メール送信
    server.send_message(msg)
    # サーバを閉じる
    server.quit()

def _create_subject(date_str, name):
    date = dt.strptime(date_str, constants.DATE_FORMAT)
    formated_date = dt.strftime(date, '%y%m%d')
    return constants.MAIL_SUBJECT.format(formated_date, name)    

def _create_body(values, name):
    with open(constants.MAIL_TEMPLATE_PATH, encoding='utf-8') as f:
        template = Template(f.read())

    body = template.substitute(
        name=name,
        work_day=values['work_day'],
        work_start_time=values['work_start_time'],
        work_end_time=values['work_end_time'],
        breakout_time=values['breakout_time'],
        detail=values['detail'],
        next_day_plan=values['next_day_plan'],
        problems=values['problems'],
        solution=values['solution'],
        others=values['others'] 
    )

    return body
