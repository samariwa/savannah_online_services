from app import app, db, organization, csrf
from flask import render_template, request
from app.response import flash_response
import json


@app.route('/')
def index():
    return render_template(
        'public/index.html',
        organization=organization,
    )