from app import app, organization
from flask import render_template, request
from app.response import respond
import json


@app.errorhandler(400)
def bad_request(e):
    error_code = '400'
    return render_template("/public/error_templates/error.html",
                           organization=organization,
                           error_code=error_code,
                           error_def=respond(error_code),
                           error_message=e,
                           json=json,
                           sum=sum,
                           )


@app.errorhandler(403)
def not_found(e):
    error_code = '403'
    return render_template("/public/error_templates/error.html",
                           organization=organization,
                           error_code=error_code,
                           error_def=respond(error_code),
                           error_message=e,
                           json=json,
                           sum=sum,
                           )


@app.errorhandler(404)
def not_found(e):
    error_code = '404'
    return render_template("/public/error_templates/error.html",
                           organization=organization,
                           error_code=error_code,
                           error_def=respond(error_code),
                           error_message=e,
                           json=json,
                           sum=sum,
                           )


@app.errorhandler(408)
def request_timeout(e):
    error_code = '408'
    return render_template("/public/error_templates/error.html",
                           organization=organization,
                           error_code=error_code,
                           error_def=respond(error_code),
                           error_message=e,
                           json=json,
                           sum=sum,
                           )


@app.errorhandler(413)
def request_timeout(e):
    error_code = '413'
    return render_template("/public/error_templates/error.html",
                           organization=organization,
                           error_code=error_code,
                           error_def=respond(error_code),
                           error_message=e,
                           json=json,
                           sum=sum,
                           )


@app.errorhandler(429)
def too_many_request(e):
    error_code = '429'
    return render_template("/public/error_templates/error.html",
                           organization=organization,
                           error_code=error_code,
                           error_def=respond(error_code),
                           error_message=e,
                           json=json,
                           sum=sum,
                           )


@app.errorhandler(500)
def server_error(e):
    error_code = '500'
    return render_template("/public/error_templates/error.html",
                           organization=organization,
                           error_code=error_code,
                           error_def=respond(error_code),
                           error_message=e,
                           json=json,
                           sum=sum,
                           )


@app.errorhandler(503)
def service_unavailable(e):
    error_code = '503'
    return render_template("/public/error_templates/error.html",
                           organization=organization,
                           error_code=error_code,
                           error_def=respond(error_code),
                           error_message=e,
                           json=json,
                           sum=sum,
                           )
