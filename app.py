# -*- coding: utf-8 -*-
from dotenv import load_dotenv
load_dotenv()
import database.database_connection 
from forms.login_form import LoginForm
from helpers.helpers_user import get_user, hash_password, credentials_valid, username_taken, add_user, change_user
from flask import Flask, redirect, url_for, render_template, request, session
from flask_cors import CORS
from blueprints.landing_blueprint import landing_blueprint
from blueprints.home_blueprint import home_blueprint
from blueprints.login_blueprint import login_blueprint
from blueprints.logout_blueprint import logout_blueprint
from blueprints.registration_blueprint import registration_blueprint
from blueprints.settings_blueprint import settings_blueprint
import json
import sys
import os

# ======== App Config =================================================#

app = Flask(__name__)
CORS(app)

secret_key = None
if 'SECRET_KEY' in os.environ:
    secret_key = os.environ['SECRET_KEY']
else:
    secret_key = 'local-demo'

app.secret_key = secret_key

app.config['RECAPTCHA_USE_SSL']= False
app.config['RECAPTCHA_PUBLIC_KEY']= os.getenv("RECAPTCHA_PUBLIC_KEY")
app.config['RECAPTCHA_PRIVATE_KEY']= os.getenv("RECAPTCHA_PRIVATE_KEY")
app.config['RECAPTCHA_OPTIONS'] = {'theme':'white'}


# ======== Blueprint Routing =================================================#
# Landing 
app.register_blueprint(landing_blueprint)
# Login 
app.register_blueprint(login_blueprint)
# Logout 
app.register_blueprint(logout_blueprint)
# Registration 
app.register_blueprint(registration_blueprint)
# Home 
app.register_blueprint(home_blueprint)
# Settings 
app.register_blueprint(settings_blueprint)


# ======== Bind the Database =================================================#
# bind_engine()

# ======== Main ============================================================== #
if __name__ == "__main__":
    app.secret_key = os.urandom(12)  # Generic key for dev purposes only
    app.run(debug=True, use_reloader=True)
