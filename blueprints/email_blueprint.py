from flask import Blueprint, redirect, url_for, render_template, request, session, json, jsonify
from helpers.helpers_user import get_user, credentials_valid
from forms.login_form import LoginForm
import os
from email import message
from helpers.helpers_email import send_email

email_blueprint = Blueprint("email", __name__)


# -------- API email --------- #
@email_blueprint.route('/api/email', methods=['GET', 'POST'])
def email_route():
    response = send_email()
    if response is not None:
        print("Email response with status_code is: ", response)
        if response.status_code == 202:
            return jsonify({"body": "brilliant you brought a mac", "status": response.status_code, "message": "success"})

    print("Email response without status_code is: ", response)
    return jsonify({"body": {}, "status": 400, "message": "fail"})


# -------- TEST email --------- #
@email_blueprint.route('/email', methods=['GET'])
def home():
    if session.get('logged_in'):
        return render_template('email.html', email=email)
    return redirect(url_for('login.login'))
