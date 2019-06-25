from flask import Blueprint, redirect, url_for, render_template, request, session, json
from helpers.helpers_user import get_user, credentials_valid, username_taken, add_user, hash_password
from forms.registration_form import RegistrationForm

registration_blueprint = Blueprint("registration", __name__)

def register(request):
    username = request.form['username'].lower()
    password = hash_password(request.form['password'])
    email = request.form['email']
    if not username_taken(username):
        print("signup username: ", username)
        print("signup password: ", password)
        add_user(username, password, email)
        session['logged_in'] = True
        session['username'] = username
        print("registered success!")
        # because this form post not ajax we need to do a redirect
        # return json.dumps({'status': 'success', "username": username, "source": "test"})
        user = get_user()
        print("user is: ", user.username)
        data = {"title": "blacksmith gear", "username": user.username}
        return render_template('home.html', data=data)
    return json.dumps({'status': 'Username taken'})

# ensure that we are registrating with formData 
# form.username.data is json!
# -------- Register --------- #
@registration_blueprint.route('/signupa', methods=['GET','POST'])
def signupa():
    if not session.get('logged_in'):
        form = RegistrationForm(request.form)
        # skip validation if offline since reCaptcha won't be available....
        # only works against localhost testing

        print("signup not logged in!")
  
        if form.validate_on_submit():
            return register(request)

        print("signup not valid")

        return render_template('landing.html', form=form)
    return redirect(url_for('home.home'))


# -------- Signup ---------------------------------------------------------- #
@registration_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    if not session.get('logged_in'):
        form = RegistrationForm(request.form)
        if request.method == 'POST':
            username = request.form['username'].lower()
            password = hash_password(request.form['password'])
            email = request.form['email']
            print("signup username A: ", username)
            print("signup password A: ", password)
            print("signup email A: ", email)
            if form.validate():
                if not username_taken(username):
                    add_user(username, password, email)
                    session['logged_in'] = True
                    session['username'] = username
                    return json.dumps({'status': 'success'})
                return json.dumps({'status': 'Username taken'})
            return json.dumps({'status': 'Invalid form User/Pass required'})
        return render_template('login.html', form=form)
    return redirect(url_for('login'))
