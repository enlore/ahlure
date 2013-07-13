from flask import Blueprint, request, render_template, redirect, flash, url_for, current_app
from .forms import ContactForm

frontend = Blueprint('frontend', __name__)

# helpers
def send_mail(msg, rcpt):
    import smtplib
    from email.mime.text import MIMEText

    login = current_app.config['GMAIL']
    password = current_app.config['GMAIL_PASS']
    mime_msg = MIMEText(msg)
    mime_msg[u'Subject'] = u'[ CONTACT FORM @ ahlure.net ]'
    mime_msg[u'From'] = u'ahlue.app@gmail.com'
    mime_msg[u'Reply-To'] = u'noreply'
    mime_msg[u'To'] = u'oneofy@gmail.com'

    smtp = smtplib.SMTP(u'smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(login, password)
    smtp.sendmail(login, rcpt, mime_msg.as_string())
    smtp.quit()

# routes
@frontend.route('/', methods = [u'GET', u'POST'])
def index():
    form = ContactForm()

    if form.validate_on_submit():
        send_mail(form.message.data, u'oneofy@gmail.com')
        flash('Thank you for your message!  I\'ll get back to you soon.', 'success')
        return redirect(url_for('frontend.index'))

    return render_template('frontend/index.html', form=form)

@frontend.route('/google1f5182fb6bdd5d62.html', methods=['GET'])
def gwmt():
    return render_template('frontend/google1f5182fb6bdd5d62.html')
