from flask import Blueprint, request, render_template

frontend = Blueprint('frontend', __name__)

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
@frontend.route('/', methods = [u'GET', u'POST'])
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
        return render_template('frontend/index.html', msg=msg)
    return render_template('frontend/index.html')

@frontend.route('/google1f5182fb6bdd5d62.html', methods=['GET'])
def gwmt():
    return render_template('frontend/google1f5182fb6bdd5d62.html')
