from app import app, db, csrf, organization, mail, Message
import json
from flask import make_response, json, request, jsonify, abort, render_template, Response
from app.controllers.create import create_customer, create_order
from app.controllers.update import update_customer, update_order
from app.controllers.delete import delete_customer, delete_order
from app.general_functions import empty_input_fields, get_uuid
from datetime import datetime
from app.response import respond

## Customers ##########################################################################
@app.route('/crud/customers-create', methods=['POST'])
def customers_create():
    """
    This function gets the client request and passes its values to the
    create customer controller which creates a customer object and queries
    the database to insert.
    Any errors caught in any of the processes are returned back to the
    client for standardization to a user friendly output
    """
    response = ''
    # Check if there are any blank input fields
    empty_fields = empty_input_fields(request.form)
    if len(empty_fields) > 0:
        response = make_response(json.dumps(empty_fields), 422)
    else:
        # call the create customer controller
        query_result = create_customer(
            first_name=request.form['firstname'],
            last_name=request.form['lastname'],
            phone_no=request.form['phoneno'],
        )
        # If customer has successfully been created
        if query_result == respond('201'):
            response = make_response(respond('201'), 201)
        # If the customer already exists
        elif query_result == respond('SF020')[0] or respond('SF011'):
            response = make_response(respond('SF020')[1], 200)
        # Any other uncaught error
        else:
            response = make_response(query_result, 200)
    # request response returned
    return response

@app.route('/crud/customers-update', methods=['POST'])
@csrf.exempt
def customers_update():
    """
    This function gets the client update request and passes the values to the
    update customer controller which queries the database for the update.
    Currently it is passing all attributes and their values regardless of
    whether they are all being updated or not to the controller.
    In future only values of attributes being updated should be passed for
    efficiency.
    Any errors caught in any of the processes are returned back to the client
    for standardization to a user friendly output
    """
    response = ''
    # call the update customer controller
    update_result = update_customer(**request.get_json())
    # If update is successful
    if update_result == respond('200'):
        response = make_response(respond('200'), 200)
    # If update causes a duplicate
    elif update_result == respond('SF020')[0]:
        response = make_response(respond('SF020')[1], 200)
    # Any other uncaught error
    else:
        response = make_response(update_result, 200)
    # request response returned
    return response

@app.route('/crud/customers-delete', methods=['POST'])
@csrf.exempt
def customers_delete():
    """
    This function gets the client delete request and passes the id of the
    resource to be deleted to the delete customer controller which queries
    the database for the deletion.
    Any errors caught in any of the processes are returned back to the client
    for standardization to a user friendly output
    """
    response = ''
    # call the delete customer controller
    delete_result = delete_customer(request.get_json()['id'])
    # if deletion is successful
    if delete_result == respond('200'):
        response = make_response(respond('200'), 200)
    # Any error
    else:
        response = make_response(delete_result, 200)
    # request response returned
    return response
#############################################################################
## Orders ###################################################################
