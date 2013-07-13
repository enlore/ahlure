from flask import Flask
import smtplib
from email.mime.text import MIMEText
from .frontend import frontend

ERRLOG = u'/tmp/ahlure.err.log'
ADMINS = [u'oneofy@gmail.com']
CONTACTS = [u'oneofy@gmail.com']
GMAIL_ACCOUNT = None
GMAIL_PASS = None
PORT = 5000
HOST = 'localhost'

__all__ = ['create_app']

def create_app():
    app = Flask(__name__)
    app.config.from_object(__name__)
    app.config.from_envvar('APPCONFIG', silent=True)

    app.register_blueprint(frontend)

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

        return app

