from flask import Blueprint, redirect, url_for, render_template, request, session, json, jsonify
from helpers.helpers_user import get_user, credentials_valid
from forms.login_form import LoginForm
import os

about_blueprint = Blueprint("about", __name__)


# -------- API ABOUT --------- #
@about_blueprint.route('/api/about', methods=['GET'])
def about_route():
    # if not session.get('logged_in'):
    about = """
    Forge is a tool to help me to learn how to produce an API. 
    """
    if session.get('logged_in'):
        about = """
                You are logged in and can see that Forge is an API tool. 
                """
        return jsonify({'data': {"about": about, "status": 200}})
    return jsonify({'data': {"about": about, "status": 200}})


# -------- TEST ABOUT --------- #
@about_blueprint.route('/about', methods=['GET'])
def home():
    if session.get('logged_in'):
        return render_template('about.html', about=about)
    return redirect(url_for('login.login'))
