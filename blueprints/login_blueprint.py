from flask import Blueprint, redirect, url_for, render_template, request, session, json
from helpers.helpers import get_user, credentials_valid
from forms.registration_form import RegistrationForm

login_blueprint = Blueprint("login", __name__)

# -------- Login --------- #
@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if not session.get('logged_in'):
        form = RegistrationForm(request.form)
        if request.method == 'POST':
            username = request.form['username'].lower()
            password = request.form['password']
            if form.validate():
                if credentials_valid(username, password):
                    session['logged_in'] = True
                    session['username'] = username
                    return redirect(url_for('login.home'))
                return json.dumps({'status': 'Invalid user/pass'})
            return json.dumps({'status': 'Both fields required'})
        return render_template('landing.html', form=form)
    user = get_user()
    return render_template('home.html', user=user)
