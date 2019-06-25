# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm, RecaptchaField
from wtforms import Form, StringField, validators


class RegistrationForm(FlaskForm):
    username = StringField('Username:', validators=[validators.required(), validators.Length(min=1, max=30)])
    password = StringField('Password:', validators=[validators.required(), validators.Length(min=1, max=30)])
    email = StringField('Email:', validators=[validators.optional(), validators.Length(min=0, max=50)])
    recaptcha = RecaptchaField()
