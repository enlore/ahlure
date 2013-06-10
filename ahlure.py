from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText

ERRLOG = '/tmp/ahlure.err.log'
ADMINS = ['oneofy@gmail.com']
CONTACTS = ['oneofy@gmail.com', 'alexander@waerealty.com']

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('AHLURE_SETTINGS', silent=True)

# let's log stuff!
if not app.debug:
    import logging
    from logging.handlers import SMTPHandler
    from logging import Formatter, FileHandler

    serv = '127.0.0.1'
    who = 'ahlure@chilidog.rokitpowered.net'
    whom = ADMINS
    subj = '[AHLURE TOTALLY BARFED]'
    mh = SMTPHandler(serv, who, whom, subj)
    mh.setLevel(logging.ERROR)
    mh.setFormatter(Formatter('''
    OH JESUS
    Message type: %(levelname)s
    Location: %(pathname)s:%(lineno)d
    Module: %(module)s
    Function: %(funcName)s
    Time: %(asctime)s

    Message:

    %(message)s
    '''))

# routes
@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        form = request.form

        rcpt = form['contact-email']
        msg = """
        Submission to ahlure.net:
        Name:  %s
        Phone: %s
        Message: 
        %s
        """ % (form['contact-name'], form['contact-phone'], form['contact-blurb'])
        mime_msg = MIMEText(msg)
        mime_msg['Subject'] = '[ahlure.net CONTACT FORM]'
        smtp = smtplib.SMTP('127.0.0.1', 143)
        smtp.sendmail('contact@ahlure.net', rcpt, mime_msg.as_string())
        return render_template('index.html', msg=msg)
    return render_template('index.html')

@app.route('/google1f5182fb6bdd5d62.html', methods=['GET'])
def gwmt():
    return render_template('google1f5182fb6bdd5d62.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
