from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired

class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    signup_submit = SubmitField("Sign me up")

class SignInForm(FlaskForm):
    TicketNumber = IntegerField("Ticket Number", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    TYPE = StringField("Type", validators=[DataRequired()])
    StoryPoints = IntegerField("Story Points", validators=[DataRequired()])
    signin_submit = SubmitField("Sign me in")
