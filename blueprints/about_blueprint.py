from flask import Blueprint, redirect, url_for, render_template, request, session, json
from helpers.helpers_user import get_user, credentials_valid
from forms.login_form import LoginForm
import os

home_blueprint = Blueprint("about", __name__)

about = {
    version: os.environ['VERSION']
}

# -------- Settings --------- #
@home_blueprint.route('/about', methods=['GET'])
def home():
    if session.get('logged_in'):
        return render_template('about.html', about=about)
    return redirect(url_for('login.login'))