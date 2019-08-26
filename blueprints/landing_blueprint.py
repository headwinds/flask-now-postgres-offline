from flask import Blueprint, redirect, url_for, render_template, request, session, json, jsonify
from helpers.helpers_user import get_user, credentials_valid
from forms.registration_form import RegistrationForm
from flask_wtf import FlaskForm
from bs4 import BeautifulSoup

landing_blueprint = Blueprint("landing", __name__)


# -------- Landing --------- #
@landing_blueprint.route('/api/page', methods=['GET'])
def api_page():
    if request.method == 'GET':
        ff = FlaskForm()
        # value = soup
        return jsonify({
            "csrf": ff.csrf_token  # a hidden html field 
        })


@landing_blueprint.route('/', methods=['GET', 'POST'])
def landing():
    if not session.get('logged_in'):
        registrationForm = RegistrationForm(request.form)
        """
        if request.method == 'POST':
            username = request.form['username'].lower()
            password = request.form['password']
            if loginForm.validate():
                if credentials_valid(username, password):
                    session['logged_in'] = True
                    session['username'] = username
                    return json.dumps({'status': 'Login successful'})
                return json.dumps({'status': 'Invalid user/pass'})
            return json.dumps({'status': 'Both fields required'})
        """
        return render_template('landing.html', form=registrationForm)
    user = get_user()
    data = {"title": "blacksmith gear", "username": user.username}
    return render_template('home.html', data=data)

