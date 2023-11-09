from app import app, db, organization, csrf
from flask import render_template, request
from app.response import flash_response
from app.forms import SessionRegistrationForm
from app.controllers.read import fetch_active_departments
import json
import random

@app.route('/')
def index():
    random_number = random.randint(0, 11)
    return render_template(
        'public/index.html',
        random_number=random_number,
    )

@app.route('/session-registration/<session_id>')
@app.route('/session-registration/<session_id>/')
def session_registration(session_id):
    random_number = random.randint(0, 11)
    session_registration_form = SessionRegistrationForm()
    departments=fetch_active_departments()
    department_options = [(d['id'], d['department'])
                                  for d in departments]
    session_registration_form.department.choices.extend(department_options)
    return render_template(
        'public/session-registration.html', 
        random_number=random_number,
        session_registration_form=session_registration_form)

@app.route('/session-registration-success/<session_id>')
@app.route('/session-registration-success/<session_id>/')
def session_registration_success(session_id):
    random_number = random.randint(0, 11)
    return render_template(
        'public/session-registration-success.html', random_number=random_number)

@app.route('/session-registration-error/<session_id>')
@app.route('/session-registration-error/<session_id>/')
def session_registration_error(session_id):
    random_number = random.randint(0, 11)
    return render_template(
        'public/session-registration-error.html', random_number=random_number)

@app.route('/status-page')
@app.route('/status-page/')
def status_page():
    random_number = random.randint(0, 11)
    return render_template(
        'public/status-page.html', random_number=random_number)