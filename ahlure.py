from flask import Flask, render_template, request

ERRLOG = '/tmp/ahlure.err.log'
ADMINS = ['oneofy@gmail.com']
CONTACTS = ['oneofy@gmail.com']

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('AHLURE_SETTINGS', silent=True)

# let's log stuff!
if not app.debug:
    import logging
    from logging.handlers import SMTPHandler
    from logging import Formatter, FileHandler

    # for files!
    fh = FileHandler(app.config['ERRLOG'])
    fh.setFormatter(Formatter('''
    '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'
        '''))
    app.logger.addHandler(fh)

    # for emails yes!
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

# helpers
def send_mail(msg, rcpt):
    import smtplib
    from email.mime.text import MIMEText

    login = None
    password = None
    mime_msg = msg
    mime_msg['Subject'] = '[ CONTACT FORM @ ahlure.net ]'

    smtp = smtplib.SMTP('localhost', 143)
    smtp.sendmail('ahlure@chilidog.rokitpowered.net', rcpt, mime_msg.as_string())
    smtp.quit()

# routes
@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        form = request.form

        rcpt = form['contact-email']
        subj = '[ahlure.net CONTACT FORM]'
        msg = """
        Submission to ahlure.net:
        Name:  %s
        Phone: %s
        Message: 
        %s
        """ % (form['contact-name'], form['contact-phone'], form['contact-blurb'])

        send_mail(msg,CONTACTS)
        return render_template('index.html', msg=msg)

    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
