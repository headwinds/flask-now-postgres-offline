from flask import Blueprint, redirect, url_for, render_template, request, session, json, jsonify
from helpers.helpers_user import get_user, credentials_valid
from forms.login_form import LoginForm
import os
from helpers.helpers_cbc_schedules import get_schedule

cbc_blueprint = Blueprint("cbc", __name__)


# -------- API ABOUT --------- #
@cbc_blueprint.route('/api/cbc/schedules', methods=['GET'])
def cbc_route():
    # if not session.get('logged_in'):
    """
    if session.get('logged_in'):
        schedule = get_schedule()
        return jsonify({
            "schedule": schedule,
            "status": 200,
            "message": "success"
        })
    return jsonify({"schedule": [], "status": 200, "message": "fail"})
    """
    station = request.args.get("station")
    print("station", station)
    schedule = get_schedule(station)
    return jsonify({"schedule": schedule, "status": 200, "message": "success"})


# -------- TEST ABOUT --------- #
"""
@cbc_blueprint.route('/cbc/schedules', methods=['GET'])
def cbc():
    if session.get('logged_in'):
        return render_template('about.html', about=about)
    return redirect(url_for('login.login'))
"""
