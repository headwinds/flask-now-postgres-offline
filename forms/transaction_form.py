# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm, RecaptchaField
from wtforms import Form, StringField, IntegerField, validators


class TransactionForm(FlaskForm):
    title = StringField(
        'Title:',
        validators=[validators.required(),
                    validators.Length(min=1, max=30)])
    type = StringField(
        'Type:',
        validators=[validators.required(),
                    validators.Length(min=1, max=30)])
    cost = IntegerField('Country Code', [validators.required()])           
    transaction_json = StringField(
        'Transaction:',
        validators=[validators.optional(),
                    validators.Length(min=0, max=50)])
