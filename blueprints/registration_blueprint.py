from flask import Blueprint, redirect, url_for, render_template, request, session, json, jsonify
from helpers.helpers_user import get_user, credentials_valid, username_taken, add_user, hash_password
from forms.registration_form import RegistrationForm
from helpers.helpers_email import confirm_token
from helpers.helpers_user import get_user_email, update_confirm_user_email
import datetime

registration_blueprint = Blueprint("registration", __name__)


def register(request):
    print("signup register")
    username = request.form['username'].lower()
    password = hash_password(request.form['password'])
    email = request.form['email']
    if not username_taken(username):
        result = add_user(username, password, email)
        session['logged_in'] = True
        session['username'] = username
        if result is True:
            print("registered success")
            return redirect(url_for('home.verify'))
        else:
            print("registered fail")
            return redirect(url_for('landing.landing'))
    return json.dumps({'status': 'Username taken'})

# ensure that we are registrating with formData
# form.username.data is FlaskForm
# -------- Register API --------- #
@registration_blueprint.route('/api/signup', methods=['POST'])
def api_signup():
    if not session.get('logged_in'):
        form = RegistrationForm(request.form)
        # skip validation if offline since reCaptcha won't be available....
        # only works against localhost testing

        if form.validate_on_submit():
            print("validate!")
            return register(request)

        print("form failed validation: ", form.errors)

        return jsonify({
                "message": "success - registered",
                "status": 200,
                "source": "api",
                })

    return jsonify({
                "message": "success - already logged in",
                "status": 200,
                "source": "api",
                })

# ensure that we are registrating with formData
# form.username.data is FlaskForm
# -------- Register --------- #
@registration_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    if not session.get('logged_in'):
        form = RegistrationForm(request.form)
        # skip validation if offline since reCaptcha won't be available....
        # only works against localhost testing

        if form.validate_on_submit():
            print("validate!")
            return register(request)

        print("form failed validation: ", form.errors)

        return render_template('landing.html', form=form)
    return redirect(url_for('home.home'))


@registration_blueprint.route('/email/confirm/<token>')
def confirm_email():
    if session.get('logged_in'):
        try:
            email = confirm_token(token)
        except:
            # flash('The confirmation link is invalid or has expired.', 'danger')
            print("confirmation link is invalid")

        user = get_user_email()

        if user.confirmed is True:
            # flash('Account already confirmed. Please login.', 'success')
            print("user email already confirmed")
        else:
            result = update_confirm_user_email()
            if result is True:
                print("user email updated to be confirmed")
            else:
                print("user email update fail")

    return redirect(url_for('home.home'))
