from flask import Blueprint, redirect, url_for, render_template, request, session, json, jsonify
from helpers.helpers_user import get_user, credentials_valid, username_taken, add_user, hash_password
from forms.registration_form import RegistrationForm

registration_blueprint = Blueprint("registration", __name__)


def register(request):
    print("signup register")
    username = request.form['username'].lower()
    password = hash_password(request.form['password'])
    email = request.form['email']
    if not username_taken(username):
        print("signup username: ", username)
        print("signup password: ", password)
        result = add_user(username, password, email)
        session['logged_in'] = True
        session['username'] = username
        if result is True:
            print("registered success")
            return redirect(url_for('home.home'))
        else:
            print("registered fail")
            return redirect(url_for('landing.landing'))
    return json.dumps({'status': 'Username taken'})


# ensure that we are registrating with formData
# form.username.data is FlaskForm
# -------- Register --------- #
@registration_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    if not session.get('logged_in'):
        form = RegistrationForm(request.form)
        # skip validation if offline since reCaptcha won't be available....
        # only works against localhost testing

        print("signup not logged in!")

        if form.validate_on_submit():
            print("validate!")
            return register(request)

        print("signup not valid errors: ", form.errors)

        return render_template('landing.html', form=form)
    return redirect(url_for('home.home'))
