from flask import Blueprint, redirect, url_for, render_template, request, session, json
from helpers.helpers_user import get_user, credentials_valid
from forms.login_form import LoginForm

home_blueprint = Blueprint("home", __name__)

# -------- Settings --------- #
@home_blueprint.route('/home', methods=['GET'])
def home():
    if session.get('logged_in'):
        user = get_user()
        data = {"title": "blacksmith gear", "username": user.username}
        return render_template('home.html', data=data)
    return redirect(url_for('login.login'))