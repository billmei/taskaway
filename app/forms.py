from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required

# class LoginForm(Form):
#     openid = TextField('openid', validators = [Required()])
#     remember_me = BooleanField('remember_me', default = False)

class LoginForm(Form):
    email = TextField('Email', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
