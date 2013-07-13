from flask.ext.wtf import Form, TextField, TextAreaField, SubmitField 
from flask.ext.wtf import Required, Email

class ContactForm(Form):
    name    = TextField(u'Name:', [Required()])
    email   = EmailField(u'Email:', [Required(), Email()])
    phone   = TextField(u'Phone:', [Required()])
    message = TextAreadField(u'Message:', [Required()])
