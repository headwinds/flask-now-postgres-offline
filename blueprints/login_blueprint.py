from flask import Blueprint, redirect, url_for, render_template, request, session, json, jsonify
from helpers.helpers_user import get_user, credentials_valid
from forms.login_form import LoginForm
from forms.registration_form import RegistrationForm
from flask_wtf import FlaskForm

login_blueprint = Blueprint("login", __name__)


# -------- API Login --------- #
@login_blueprint.route('/api/login', methods=['POST'])
def api_login():
    if not session.get('logged_in'):
        loginForm = LoginForm(request.form)

        if request.method == 'POST':
            print("LOGIN request.data", request.data)
            print("LOGIN is_json", request.is_json)
            if "username" in request.form:

                username = request.form['username'].lower()
                password = request.form['password']

                if loginForm.validate():
                    if credentials_valid(username, password):
                        session['logged_in'] = True
                        session['username'] = username
                        return jsonify({
                            "message": "success",
                            "status": 200,
                            "username": username,
                            "source": "api"
                        })
                    return json.dumps({'status': 'Invalid user/pass'})

            elif request.is_json is True:
                json_data = request.get_json()
                username = json_data["username"]
                password = json_data["password"]
                ff = FlaskForm()
                if credentials_valid(username, password):
                    session['logged_in'] = True
                    session['username'] = username
                    # return json.dumps({'status': 'success', "username": username, "source": "api"})
                    return jsonify({
                        "message": "success",
                        "status": 200,
                        "csrfToken": ff.csrf_token  # a hidden html field 
                    })
                return jsonify({
                    "message": "invalid username or password",
                    "status": 200,
                })
            return jsonify({
                "message": "both field required",
                "status": 200,
            })
    user = get_user()
    return json.dumps({
        'status': 'success',
        "user": {
            "username": user.username
        }
    })


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
                    return jsonify({
                        "message": "success",
                        "status": 200,
                        "username": username,
                    })
                    return jsonify({
                        "message": "success",
                        "status": 200,
                    })
                return jsonify({
                    "message": "invalid username or password",
                    "status": 200,
                })
            return jsonify({
                "message": "both fields required",
                "status": 200,
            })
        return render_template('landing.html', form=registrationForm)
    return redirect(url_for('home.home'))
