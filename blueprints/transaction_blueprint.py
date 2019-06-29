from flask import Blueprint, redirect, url_for, render_template, request, session, json, jsonify
from helpers.helpers_transactions import transaction_valid, add_transaction
from forms.transaction_form import TransactionForm
from blueprints.transaction.post_transaction import post_transaction

transaction_blueprint = Blueprint("transaction", __name__)

# -------- API Settings --------- #
@transaction_blueprint.route('/api/transactions',
                             methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def api_transactions():
    if session.get('logged_in'):

        form = TransactionForm(request.form)

        if request.method == 'POST':
            return post_transaction(form)
        elif request.method == 'PUT':
            return put_transaction(form)
        elif request.method == 'PATCH':
            return patch_transaction(form)
        elif request.method == 'DELETE':
            return delete_transaction(form)

    return jsonify({
        "data": {
            "message": "invalid transaction not logged in",
            "status": 200
        }
    })


# -------- Test Settings --------- #
@transaction_blueprint.route('/transactions',
                             methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
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
