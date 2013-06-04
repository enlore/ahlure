from flask import Flask, render_template, request

ERRLOG = '/tmp/ahlure.err.log'
ADMINS = ['oneofy@gmail.com']

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
    if requset.method == 'POST':
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

    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
