from app import app, db, organization, csrf
from flask import render_template, request
from app.response import flash_response
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
    return render_template(
        'public/session-registration.html', random_number=random_number)

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