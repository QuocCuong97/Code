import os
import subprocess
import telegram
import smtplib


class Telegram_Bot(object):
    def __init__(self, para_token, para_chat_id):
        self.token = para_token
        self.chat_id = para_chat_id
    def send_message(self, msg):
        try:
            telegram_notify = telegram.Bot(self.token)       # token
            telegram_notify.send_message(chat_id=self.chat_id, text=msg, parse_mode='HTML')   # chat_id
        except:
            print('Failed')


class Email_Bot(object):
    
    def __init__(self, para_sender_email, para_sender_password):
        self.sender = para_sender_email
        self.sender_password = para_sender_password

    def get_target(self, target_file):
        count = subprocess.getoutput("cat %s | wc -l" %target_file)
        op = open(target_file, 'r')
        i = 1
        self.list_target = []
        while i <= int(count):
            x = op.readline().strip()
            self.list_target.append(x)
            i+=1
        return self.list_target

    def send_email(self, para_subject, para_body):
        for x in self.list_target:
            email_text = "From: %s\nTo: %s\nSubject: %s\n\n%s\n" % (self.sender, x, para_subject, para_body)
            try:
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.ehlo()
                server.login(self.sender, self.sender_password)
                server.sendmail(self.sender, x, email_text)
                server.close()
            except:
                print('Something went wrong...')




