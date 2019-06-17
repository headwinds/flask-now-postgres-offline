from flask import Blueprint, redirect, url_for, render_template, request, session, json
from helpers.helpers import get_user, credentials_valid
from forms.login_form import LoginForm

settings_blueprint = Blueprint("settings", __name__)

# -------- Settings --------- #
@settings_blueprint.route('/settings', methods=['GET', 'POST'])
def settings():
    if session.get('logged_in'):
        if request.method == 'POST':
            password = request.form['password']
            if password != "":
                password = hash_password(password)
            email = request.form['email']
            change_user(password=password, email=email)
            return json.dumps({'status': 'Saved'})
        user = get_user()
        print("settings user: ", user)
        return render_template('settings.html', user=user)
    return redirect(url_for('login'))