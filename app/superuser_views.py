from app import app
from flask import render_template
from app.forms import AdminActionForm
from app.controllers.read import fetch_all_users
from app.auth_views import login_required_redirect
from flask_login import current_user

@app.route('/superuser/dashboard')
@app.route('/superuser/dashboard/')
@app.route('/superuser/')
@app.route('/superuser')
@login_required_redirect(
    login_url="admin_login",
    login_message="Please log in to access this page"
)
def superuser_dashboard():
    return render_template('superuser/dashboard.html')

@app.route('/superuser/users')
@app.route('/superuser/users/')
@login_required_redirect(
    login_url="admin_login",
    login_message="Please log in to access this page"
)
def users():
    return render_template('superuser/users.html',
                           admin_action_form=AdminActionForm())