from flask import Blueprint, redirect, url_for, render_template, request, session, json, jsonify
from helpers.helpers_transactions import transaction_valid, add_transaction
from forms.transaction_form import TransactionForm

transaction_blueprint = Blueprint("transaction", __name__)


def post_transaction(form):
    if request.is_json is True:
        json_data = request.get_json()
        title = json_data["title"]
        type = json_data["type"]
        cost = json_data["cost"]
        transaction_json = json_data["transaction_json"]

        if transaction_valid(title, type, cost, transaction_json):
            result = add_transaction(title, type, cost, transaction_json)

            if result is True:
                return jsonify({"data": {"message": "success", "status": 200}})
            else:
                return jsonify({
                    "data": {
                        "message": "invalid transaction database error",
                        "status": 200
                    }
                })

        return jsonify(
            {"data": {
                "message": "invalid transaction failed validation",
                "status": 200
            }})

    elif form.validate():
        title = request.form["title"]
        type = request.form["type"]
        cost = request.form["cost"]
        transaction_json = request.form["transaction_json"]

        if transaction_valid(title, type, cost, transaction_json):

            result = add_transaction(title, type, cost, transaction_json)

            if result is True:
                return jsonify({"data": {"message": "success", "status": 200}})
            else:
                return jsonify({
                    "data": {
                        "message": "invalid transaction failed validation",
                        "status": 200
                    }
                })

    return jsonify({"data": {"message": "invalid transaction failed both form and json", "status": 200}})


# -------- API Settings --------- #
@transaction_blueprint.route(
    '/api/transactions', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def api_transactions():
    if session.get('logged_in'):

        form = TransactionForm(request.form)

        if request.method == 'POST':
            return post_transaction(form)

    return jsonify({"data": {"message": "invalid transaction not logged in", "status": 200}})


# -------- Test Settings --------- #
@transaction_blueprint.route(
    '/transactions', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def transactions():
    if session.get('logged_in'):
        if request.method == 'POST':
            password = request.form['password']
            if password != "":
                password = hash_password(password)
            email = request.form['email']
            change_user(password=password, email=email)
            return json.dumps({'status': 'Saved'})
        user = get_user()
        print("settings user: ", user)
        return render_template('settings.html', user=user)
    return redirect(url_for('login.login'))
