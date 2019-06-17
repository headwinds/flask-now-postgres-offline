from flask import Blueprint, redirect, url_for, render_template, request, session, json
from helpers.helpers import get_user, credentials_valid
from forms.login_form import LoginForm

logout_blueprint = Blueprint("login", __name__)

# -------- Logout --------- #
@logout_blueprint.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))