from app import app, db, csrf, organization
from flask import make_response, json, request, jsonify, abort
from app.general_functions import empty_input_fields
from app.controllers.create import create_admin, create_department, create_event_venue
from app.controllers.update import update_user
from app.controllers.delete import delete_admin, delete_staff
from datetime import datetime
from app.response import respond

##########################################################################
## Staff #################################################################
@app.route('/crud/admin-create', methods=['POST'])
@csrf.exempt
def admin_create():
    """
    This function gets the client request and passes its values to the
    create admin controller which creates an admin object and queries the
    database to insert.
    Any errors caught in any of the processes are returned back to
    the client for standardization to a user friendly output
    """
    response = ''
    # Check if there are any blank input fields
    empty_fields = empty_input_fields(request.form)
    if len(empty_fields) > 0:
        response = make_response(json.dumps(empty_fields), 422)
    else:
        # call the create admin controller
        query_result = create_admin(
            firstname=request.form['firstname'],
            lastname=request.form['lastname'],
            email_address=request.form['email_address'],
            role=request.form['role']
        )
        # If admin has successfully been created
        if query_result == respond('201'):
            response = make_response(respond('201'), 201)
        # If the admin already exists
        elif query_result == respond('SF020')[0]:
            response = make_response(respond('SF020')[1], 200)
        # Any other uncaught error
        else:
            response = make_response(query_result, 200)
    # request response returned
    return response

@app.route('/crud/admin-update', methods=['POST'])
@csrf.exempt
def admin_update():
    """
    This function gets the client update request and passes the values to the
    update user controller which queries the database for the update.
    Currently it is passing all attributes and their values regardless
    of whether they are all being updated or not to the controller.
    In future only values of attributes being updated should be passed
    Any errors caught in any of the processes are returned back to the
    client for standardization to a user friendly output
    """
    response = ''
    # call the update user controller
    update_result = update_user(**request.get_json())
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

@app.route('/crud/admin-delete', methods=['POST'])
@csrf.exempt
def admin_delete():
    """
    This function gets the client delete request and passes the id of the
    resource to be deleted to the delete admin controller
    which queries the database for the deletion.
    Any errors caught in any of the processes are returned back to
    the client for standardization to a user friendly output
    """
    response = ''
    # call the delete admin controller
    delete_result = delete_admin(request.get_json()['id'])
    # if deletion is successful
    if delete_result == respond('200'):
        response = make_response(respond('200'), 200)
    # Any error
    else:
        response = make_response(delete_result, 200)
    # request response returned
    return response

@app.route('/crud/staff-delete', methods=['POST'])
@csrf.exempt
def staff_delete():
    """
    This function gets the client delete request and passes the id of the
    resource to be deleted to the delete staff controller
    which queries the database for the deletion.
    Any errors caught in any of the processes are returned back to
    the client for standardization to a user friendly output
    """
    response = ''
    # call the delete staff controller
    delete_result = delete_staff(request.get_json()['id'])
    # if deletion is successful
    if delete_result == respond('200'):
        response = make_response(respond('200'), 200)
    # Any error
    else:
        response = make_response(delete_result, 200)
    # request response returned
    return response

##########################################################################
## Department ############################################################
@app.route('/crud/department-create', methods=['POST'])
@csrf.exempt
def department_create():
    """
    This function gets the client request and passes its values to the
    create department controller which creates a department object and 
    queries the database to insert.
    Any errors caught in any of the processes are returned back to
    the client for standardization to a user friendly output
    """
    response = ''
    # Check if there are any blank input fields
    empty_fields = empty_input_fields(request.form)
    if len(empty_fields) > 0:
        response = make_response(json.dumps(empty_fields), 422)
    else:
        # call the create department controller
        query_result = create_department(
            department=request.form['department_name']
        )
        # If department has successfully been created
        if query_result == respond('201'):
            response = make_response(respond('201'), 201)
        # If the department already exists
        elif query_result == respond('SF020')[0]:
            response = make_response(respond('SF020')[1], 200)
        # Any other uncaught error
        else:
            response = make_response(query_result, 200)
    # request response returned
    return response

##########################################################################
## Event Venue ###########################################################
@app.route('/crud/event-venue-create', methods=['POST'])
@csrf.exempt
def event_venue_create():
    """
    This function gets the client request and passes its values to the
    create event venue controller which creates an event venue object and 
    queries the database to insert.
    Any errors caught in any of the processes are returned back to
    the client for standardization to a user friendly output
    """
    response = ''
    # Check if there are any blank input fields
    empty_fields = empty_input_fields(request.form)
    if len(empty_fields) > 0:
        response = make_response(json.dumps(empty_fields), 422)
    else:
        # call the create event venue controller
        query_result = create_event_venue(
            venue=request.form['event_venue_name']
        )
        # If event venue has successfully been created
        if query_result == respond('201'):
            response = make_response(respond('201'), 201)
        # If the event venue already exists
        elif query_result == respond('SF020')[0]:
            response = make_response(respond('SF020')[1], 200)
        # Any other uncaught error
        else:
            response = make_response(query_result, 200)
    # request response returned
    return response