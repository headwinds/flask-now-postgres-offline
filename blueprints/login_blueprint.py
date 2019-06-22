from flask import Blueprint, redirect, url_for, render_template, request, session, json
from helpers.helpers_user import get_user, credentials_valid
from forms.login_form import LoginForm
from forms.registration_form import RegistrationForm

login_blueprint = Blueprint("login", __name__)

# -------- API Login --------- #
@login_blueprint.route('/api/login', methods=['GET', 'POST'])
def api_login():
    if not session.get('logged_in'):
        loginForm = LoginForm(request.form)

        if request.method == 'POST':
            username = request.form['username'].lower()
            password = request.form['password']
            if loginForm.validate():
                if credentials_valid(username, password):
                    session['logged_in'] = True
                    session['username'] = username
                    user = get_user()
                    return json.dumps({'status': 'success', "username": user.username})
                return json.dumps({'status': 'Invalid user/pass'})
            return json.dumps({'status': 'Both fields required'})

    user = get_user()
    return json.dumps({'status': 'success', user: user})

# -------- Test Login --------- #
@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if not session.get('logged_in'):
        loginForm = LoginForm(request.form)
        registrationForm = RegistrationForm(request.form)

        if request.method == 'POST':
            username = request.form['username'].lower()
            password = request.form['password']
            if loginForm.validate():
                if credentials_valid(username, password):
                    session['logged_in'] = True
                    session['username'] = username
                    user = get_user()
                    return json.dumps({'status': 'success', "username": user.username})
                return json.dumps({'status': 'Invalid user/pass'})
            return json.dumps({'status': 'Both fields required'})
        return render_template('landing.html', form=registrationForm)
    return redirect(url_for('home.home'))
