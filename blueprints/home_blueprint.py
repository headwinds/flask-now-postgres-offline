from flask import Blueprint, redirect, url_for, render_template, request, session, json
from helpers.helpers import get_user, credentials_valid
from forms.login_form import LoginForm

home_blueprint = Blueprint("home", __name__)

# -------- Settings --------- #
@home_blueprint.route('/home', methods=['GET'])
def home():
    if session.get('logged_in'):
        user = get_user()
        return render_template('home.html', user=user)
    return redirect(url_for('login.login'))