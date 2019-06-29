from flask import Blueprint, redirect, url_for, render_template, request, session, json, jsonify
from helpers.helpers_transactions import transaction_valid, add_transaction


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

        return jsonify({
            "data": {
                "message": "invalid transaction failed validation",
                "status": 200
            }
        })

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

    return jsonify({
        "data": {
            "message": "invalid transaction failed both form and json",
            "status": 200
        }
    })
