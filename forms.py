from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
    first_name = StringField('First name',validators=[DataRequired("please enter your first name.")])
    last_name = StringField('Last name',validators=[DataRequired("please enter your last name.")])
    email = StringField('Email',validators=[DataRequired("please enter your email address."),Email("please enter your email address.")])
    password = PasswordField('Password',validators=[DataRequired("please enter your password."),Length(min=6,message="Password must be 6 character om more.")])
    submit = SubmitField('Sign up')

class LoginForm(Form):
    email = StringField('Email',validators=[DataRequired("please enter your email address."),Email("please enter your email address.")])
    password = PasswordField('Password',validators=[DataRequired("please enter your password")])
    submit = SubmitField('Sign in')

class AdderssForm(Form):
    address = StringField('Address',validators=[DataRequired("please enter your address.")])
    submit = SubmitField('Search')