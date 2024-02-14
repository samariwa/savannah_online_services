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