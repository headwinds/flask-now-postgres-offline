from flask import Blueprint, redirect, url_for, render_template, request, session, json, jsonify
from helpers.helpers_user import get_user, credentials_valid
from forms.login_form import LoginForm
import os
from helpers.helpers_shoutcast import get_shoutcast

shoutcast_blueprint = Blueprint("shoutcast", __name__)


# -------- API ABOUT --------- #
@shoutcast_blueprint.route('/api/shoutcast', methods=['GET'])
def shoutcast_route():
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
    shoutcast = get_shoutcast(station)
    return jsonify({"songtitle": str(shoutcast["songtitle"]), "status": 200, "message": "success"})


# -------- TEST ABOUT --------- #
"""
@shoutcast_blueprint.route('/shoutcast/schedules', methods=['GET'])
def shoutcast():
    if session.get('logged_in'):
        return render_template('about.html', about=about)
    return redirect(url_for('login.login'))
"""