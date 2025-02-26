from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, DateField, PasswordField, SubmitField, BooleanField

from wtforms.validators import  Length, Email, Optional, EqualTo, DataRequired


class SignupForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired(), Length(2, 30)]
    )
    email = StringField(
        "Email",
        validators=[DataRequired(), Email()]
    )
    gender = SelectField(
        "Gender",
        choices=["Male", "Female", "other"],
        validators=[Optional()]
    )
    dob = DateField(
        "Date of Birth",
        validators=[DataRequired()]
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(6,30)]
    )
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[DataRequired(), Length(6, 30), EqualTo("password")]
    )

    submit = SubmitField(
        "Sign up"
    )


class Loginform(FlaskForm):
        email = StringField(
            "Email",
            validators=[DataRequired(), Email()]
        )
        password = PasswordField(
            "Password",
            validators=[DataRequired(), Length(6, 30)],
        )
        remember_me = BooleanField("Remember Me")

        submit = SubmitField("Login")
