from flask import Flask, render_template

ERRLOG = '/tmp/ahlure.err.log'
ADMINS = ['oneofy@gmail.com']

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('AHLURE_SETTINGS', silent=True)

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


