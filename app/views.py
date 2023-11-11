from app import app, db, organization, csrf
from flask import render_template, request
from app.response import flash_response
from app.forms import SessionRegistrationForm
from app.controllers.read import fetch_active_departments, fetch_session_details
import json
import random

@app.route('/')
def index():
    random_number = random.randint(0, 11)
    return render_template(
        'public/index.html',
        random_number=random_number,
    )

@app.route('/session-registration/<session_uuid>')
@app.route('/session-registration/<session_uuid>/')
def session_registration(session_uuid):
    random_number = random.randint(0, 11)
    session_registration_form = SessionRegistrationForm()
    departments=fetch_active_departments()
    session_details = fetch_session_details(session_uuid)
    department_options = [(d['id'], d['department'])
                                  for d in departments]
    session_registration_form.department.choices.extend(department_options)
    if session_details is None:
        return render_template(
            'public/session-registration-error.html', 
            random_number=random_number)
    else:
        if session_details.db_status == 'active':
            return render_template(
                'public/session-registration.html', 
                random_number=random_number,
                session_details=session_details,
                session_registration_form=session_registration_form)
        else:
            return render_template(
                'public/session-registration-error.html', 
                random_number=random_number)

@app.route('/session-registration-success/<session_uuid>')
@app.route('/session-registration-success/<session_uuid>/')
def session_registration_success(session_uuid):
    random_number = random.randint(0, 11)
    session_details = fetch_session_details(session_uuid)
    return render_template(
        'public/session-registration-success.html', 
        random_number=random_number,
        session_details=session_details)

@app.route('/session-registration-error/<session_uuid>')
@app.route('/session-registration-error/<session_uuid>/')
def session_registration_error(session_uuid):
    random_number = random.randint(0, 11)
    return render_template(
        'public/session-registration-error.html', random_number=random_number)

@app.route('/status-page')
@app.route('/status-page/')
def status_page():
    random_number = random.randint(0, 11)
    return render_template(
        'public/status-page.html', random_number=random_number)