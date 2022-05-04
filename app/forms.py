from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtfforms.validators import DataRequired, Length

class SignUpForm(FlaskForm):
    username = StringField("Username", validators= [DataRequired(), Length(min=3)])
    password = PasswordField("Password", validators= [DataRequired(), Length(min=4)])
    submit = SubmitField("Sign up")

class SignInForm(FlaskForm):
    username = StringField("Username", validators= [DataRequired()])
    password = PasswordField("Password", validators= [DataRequired(), Length(min=4)])
    submit = SubmitField("Sign in")