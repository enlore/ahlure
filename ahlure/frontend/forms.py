from flask.ext.wtf import Form
from flask.ext.wtf import (TextField, TextAreaField, SubmitField, HiddenField)
from flask.ext.wtf.html5 import EmailField
from flask.ext.wtf import Required, Email

class ContactForm(Form):
    hidden_field    = HiddenField()
    name    = TextField(u'Name:', [Required()])
    email   = EmailField(u'Email:', [Required(), Email()])
    phone   = TextField(u'Phone:', [Required()])
    message = TextAreaField(u'Message:', [Required()])
    submit  = SubmitField()
