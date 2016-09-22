# -*- coding: utf-8 -*-
from flask import Flask, flash, g, abort, render_template, session, request, redirect, url_for
from flask_mail import Message
from flask_mail import Mail
from threading import Thread
from flask import jsonify
from flask import json
import os

app = Flask(__name__)

app.config.update(
    MAIL_SERVER = 'smtp.qq.com',
    MAIL_PORT = 465,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = '1145833162',
    MAIL_PASSWORD = 'prfhpkoxsjkzhheh',
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]',
    FLASKY_MAIL_SENDER = '1145833162@qq.com',
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN'),
    MAIL_DEBUG = True
)

#IMAP/SMTP授权码：exzrqfabsgggifii
#POP3/SMTP：prfhpkoxsjkzhheh

# app.config['MAIL_SERVER']='smtp.qq.com'
# app.config['MAIL_PORT']=25
# app.config['MAIL_PASSWORD']='**********'


# --- Common utility functions ------------------------------------------------

mail = Mail(app)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        data = json.loads(request.form.get('data'))
        msg = Message(data["name"],sender='1145833162@qq.com',recipients=['211028041@qq.com'])
        msg.body = ""
        msg.html = u"姓名：" + data["name"] + "<br>"+ u"学号："+ data["studentnumber"]+ "<br>"  + u"电话号码："+ data["phone"]+ "<br>" + data["goods"]
        mail.send(msg)
    return render_template('form.html')
@app.route('/form')
def form():
    return render_template('sign_up.html')
# --- Entry point -------------------------------------------------------------
	
if __name__ == '__main__':
	app.secret_key = os.urandom(24)
	app.run(debug = False)
