from app import app, organization
from flask import render_template, request
from app.response import respond
import json,random

@app.errorhandler(400)
def bad_request(e):
    error_code = '400'
    random_number = random.randint(0, 11)
    return render_template("/public/error_templates/error.html",
                           organization=organization,
                           error_code=error_code,
                           error_def=respond(error_code),
                           error_message=e,
                           json=json,
                           sum=sum,
                           random_number=random_number
                           )


@app.errorhandler(403)
def not_found(e):
    error_code = '403'
    random_number = random.randint(0, 11)
    return render_template("/public/error_templates/error.html",
                           organization=organization,
                           error_code=error_code,
                           error_def=respond(error_code),
                           error_message=e,
                           json=json,
                           sum=sum,
                           random_number=random_number
                           )


@app.errorhandler(404)
def not_found(e):
    error_code = '404'
    random_number = random.randint(0, 11)
    return render_template("/public/error_templates/error.html",
                           organization=organization,
                           error_code=error_code,
                           error_def=respond(error_code),
                           error_message=e,
                           json=json,
                           sum=sum,
                           random_number=random_number
                           )


@app.errorhandler(408)
def request_timeout(e):
    error_code = '408'
    random_number = random.randint(0, 11)
    return render_template("/public/error_templates/error.html",
                           organization=organization,
                           error_code=error_code,
                           error_def=respond(error_code),
                           error_message=e,
                           json=json,
                           sum=sum,
                           random_number=random_number
                           )


@app.errorhandler(413)
def request_timeout(e):
    error_code = '413'
    random_number = random.randint(0, 11)
    return render_template("/public/error_templates/error.html",
                           organization=organization,
                           error_code=error_code,
                           error_def=respond(error_code),
                           error_message=e,
                           json=json,
                           sum=sum,
                           random_number=random_number
                           )


@app.errorhandler(429)
def too_many_request(e):
    error_code = '429'
    random_number = random.randint(0, 11)
    return render_template("/public/error_templates/error.html",
                           organization=organization,
                           error_code=error_code,
                           error_def=respond(error_code),
                           error_message=e,
                           json=json,
                           sum=sum,
                           random_number=random_number
                           )


@app.errorhandler(500)
def server_error(e):
    error_code = '500'
    random_number = random.randint(0, 11)
    return render_template("/public/error_templates/error.html",
                           organization=organization,
                           error_code=error_code,
                           error_def=respond(error_code),
                           error_message=e,
                           json=json,
                           sum=sum,
                           random_number=random_number
                           )


@app.errorhandler(503)
def service_unavailable(e):
    error_code = '503'
    random_number = random.randint(0, 11)
    return render_template("/public/error_templates/error.html",
                           organization=organization,
                           error_code=error_code,
                           error_def=respond(error_code),
                           error_message=e,
                           json=json,
                           sum=sum,
                           random_number=random_number
                           )
