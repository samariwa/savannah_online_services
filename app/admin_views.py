from app import app, csrf, organization
from app.response import respond
from flask import render_template, make_response, json, request, redirect, url_for
from app.forms import AddSessionForm, AddEventForm, AddDepartmentForm,\
     AddEventVenueForm, AddAdminForm, AdminActionForm
from app.controllers.read import fetch_active_orders, fetch_active_customers
from app.general_functions import datetime, datetime_to_time, datetime_to_standard_date
from app.auth_views import login_required_redirect
from flask_login import current_user

@app.route('/admin/dashboard')
@app.route('/admin/dashboard/')
@app.route('/admin/')
@app.route('/admin')
@login_required_redirect(
    login_url="admin_login",
    login_message="Please log in to access this page"
)
def admin_dashboard():
    return render_template('admin/dashboard.html')

@app.route('/admin/customers')
@app.route('/admin/customers/')
@login_required_redirect(
    login_url="admin_login",
    login_message="Please log in to access this page"
)
def customers():
    return render_template('admin/customers.html',
                           customers=fetch_active_customers(),
                           customers_count=len(fetch_active_customers()),
                           add_admin_form=AddAdminForm(),
                           admin_action_form=AdminActionForm())

@app.route('/admin/orders')
@app.route('/admin/orders/')
@login_required_redirect(
    login_url="admin_login",
    login_message="Please log in to access this page"
)
def orders():
    print(fetch_active_orders())
    return render_template('admin/orders.html',
                           orders=fetch_active_orders(),
                           orders_count=len(fetch_active_orders()),
                           add_admin_form=AddAdminForm(),
                           admin_action_form=AdminActionForm())

@app.route('/admin/profile')
@app.route('/admin/profile/')
@login_required_redirect(
    login_url="admin_login",
    login_message="Please log in to access this page"
)
def profile():
    return render_template('admin/profile.html')