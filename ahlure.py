from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText

ERRLOG = u'/tmp/ahlure.err.log'
ADMINS = [u'oneofy@gmail.com']
CONTACTS = [u'oneofy@gmail.com']
GMAIL_ACCOUNT = None
GMAIL_PASS = None
PORT = 9002

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar(u'AHLURE_SETTINGS', silent=True)

# let's log stuff!
if not app.debug:
    import logging
    from logging.handlers import SMTPHandler
    from logging import Formatter, FileHandler

    # for files!
    fh = FileHandler(app.config[u'ERRLOG'])
    fh.setFormatter(Formatter(u'''
    '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'
        '''))
    app.logger.addHandler(fh)

    # for emails yes!
    serv = u'127.0.0.1'
    who = u'ahlure@chilidog.rokitpowered.net'
    whom = ADMINS
    subj = u'[AHLURE TOTALLY BARFED]'
    mh = SMTPHandler(serv, who, whom, subj)
    mh.setLevel(logging.ERROR)
    mh.setFormatter(Formatter(u'''
    OH JESUS
    Message type: %(levelname)s
    Location: %(pathname)s:%(lineno)d
    Module: %(module)s
    Function: %(funcName)s
    Time: %(asctime)s

    Message:

    %(message)s
    '''))

# helpers
def send_mail(msg, rcpt):
    import smtplib
    from email.mime.text import MIMEText

    login = None
    password = None
    mime_msg = MIMEText(msg)
    mime_msg[u'Subject'] = u'[ CONTACT FORM @ ahlure.net ]'
    mime_msg[u'From'] = u'contact.ahlure@gmail.com'
    mime_msg[u'Reply-To'] = u'noreply'
    mime_msg[u'To'] = CONTACTS

    smtp = smtplib.SMTP(u'smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(app.config['GMAIL_ACCOUNT'], app.config['GMAIL_PASS'])
    smtp.sendmail(app.config['GMAIL_ACCOUNT'], rcpt, mime_msg.as_string())
    smtp.quit()

# routes
@app.route('/', methods = [u'GET', u'POST'])
def index():
    if request.method == u'POST':
        form = request.form

        rcpt = form[u'contact-email']
        subj = u'[ahlure.net CONTACT FORM]'
        msg = u"""
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
    app.run(port=app.config['PORT'])
