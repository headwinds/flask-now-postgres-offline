from flask import Blueprint, redirect, url_for, render_template, request, session, json
from helpers.helpers_user import get_user, credentials_valid, hash_password, username_taken, add_user
from forms.registration_form import RegistrationForm

registration_blueprint = Blueprint("registration", __name__)

# -------- Register --------- #
@registration_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    if not session.get('logged_in'):
        form = RegistrationForm(request.form)
        if form.validate_on_submit():
            if not username_taken(form.username.data):
                print("username: ", form.username.data)
                add_user(form.username.data, form.password.data, form.email.data)
                session['logged_in'] = True
                session['username'] = form.username
                return redirect(url_for('home.home'))
            return json.dumps({'status': 'Username taken'})
        return render_template('landing.html', form=form)
    return redirect(url_for('login.login'))
