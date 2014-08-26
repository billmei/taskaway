from flask.ext.wtf import Form
from flask.ext.wtf.html5 import EmailField
from wtforms import PasswordField
from wtforms.validators import Required

class LoginForm(Form):
    email = EmailField('Email', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
