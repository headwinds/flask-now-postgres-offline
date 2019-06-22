from flask import Blueprint, redirect, url_for, render_template, request, session, json
from helpers.helpers_user import get_user, credentials_valid
from forms.login_form import LoginForm
from forms.registration_form import RegistrationForm

landing_blueprint = Blueprint("landing", __name__)

# -------- Landing --------- #
@landing_blueprint.route('/', methods=['GET', 'POST'])
def landing():
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
                    return json.dumps({'status': 'Login successful'})
                return json.dumps({'status': 'Invalid user/pass'})
            return json.dumps({'status': 'Both fields required'})
        return render_template('landing.html', form=registrationForm)
    user = get_user()
    data = {"title": "blacksmith gear", "username": user.username}
    return render_template('home.html', data=data)
