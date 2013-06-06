from flask import Flask, render_template, request

ERRLOG = u'/tmp/ahlure.err.log'
ADMINS = [u'oneofy@gmail.com']
CONTACTS = [u'oneofy@gmail.com']

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

    smtp = smtplib.SMTP(u'localhost', 143)
    smtp.sendmail(u'ahlure@chilidog.rokitpowered.net', rcpt, mime_msg.as_string())
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
        """ % (form[u'contact-name'], form[u'contact-phone'], form[u'contact-blurb'])

        send_mail(msg,CONTACTS)
        return render_template(u'index.html', msg=msg)

    return render_template(u'index.html')

if __name__ == u'__main__':
    app.debug = True
    app.run()
