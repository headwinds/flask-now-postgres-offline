from flask import Blueprint, redirect, url_for, render_template, request, session, json
from helpers.helpers import get_user, credentials_valid, hash_password, username_taken, add_user
from forms.registration_form import RegistrationForm

registration_blueprint = Blueprint("probe", __name__)

# -------- Register --------- #
@registration_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    if not session.get('logged_in'):
        form = RegistrationForm(request.form)
        if request.method == 'POST':
            username = request.form['username'].lower()
            password = hash_password(request.form['password'])
            email = request.form['email']
            if form.validate():
                if not username_taken(username):
                    add_user(username, password, email)
                    session['logged_in'] = True
                    session['username'] = username
                    return json.dumps({'status': 'Signup successful'})
                return json.dumps({'status': 'Username taken'})
            return json.dumps({'status': 'User/Pass required'})
        return render_template('login.html', form=form)
    return redirect(url_for('login.login'))
