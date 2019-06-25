from flask import Blueprint, redirect, url_for, render_template, request, session, json, jsonify
from helpers.helpers_user import get_user, credentials_valid
from forms.login_form import LoginForm
from forms.registration_form import RegistrationForm

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
                print("LOGIN request.form", request.form['username'])
                username = request.form['username'].lower()
                password = request.form['password']

                if loginForm.validate():
                    if credentials_valid(username, password):
                        session['logged_in'] = True
                        session['username'] = username
                        return json.dumps({'status': 'success', "username": username, "source": "api"})
                    return json.dumps({'status': 'Invalid user/pass'})

            elif request.is_json == True:
                print("LOGIN no request.form so payload is json")
                json_data = request.get_json()
                username = json_data["username"]
                password = json_data["password"]
                print("LOGIN username: ", username)
                if credentials_valid(username, password):
                    session['logged_in'] = True
                    session['username'] = username
                    # return json.dumps({'status': 'success', "username": username, "source": "api"})
                    return jsonify({'data':{"message": "success", "status": 200}})
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
                    return json.dumps({'status': 'success', "username": username})
                return json.dumps({'status': 'Invalid user/pass'})
            return json.dumps({'status': 'Both fields required'})
        return render_template('landing.html', form=registrationForm)
    return redirect(url_for('home.home'))
