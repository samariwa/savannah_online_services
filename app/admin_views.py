from app import app, csrf, organization
from app.response import respond
from flask import render_template, make_response, json, request
from app.forms import AddCategoryForm, AddCustomerForm, AddSupplierForm,\
     ProductUnitSettingForm, ForceAttributionForm, AddProductUnitForm,\
     AddExpenseCategoryForm, AddReclassCategoryForm, AddReclassItemForm
from app.general_functions import datetime, datetime_to_time, datetime_to_standard_date
from app.auth_views import roles_required, login_required_redirect
from flask_login import current_user

@app.route('/admin/dashboard')
@app.route('/admin/dashboard/')
@app.route('/admin/')
@app.route('/admin')
@login_required_redirect(
    login_url="admin_login",
    login_message="Please log in to access this page"
)
@roles_required('SuperUser', 'Admin')
def admin_dashboard():
    return render_template('admin/dashboard.html')

@app.route('/admin/profile')
@app.route('/admin/profile/')
@login_required_redirect(
    login_url="admin_login",
    login_message="Please log in to access this page"
)
@roles_required('SuperUser', 'Admin')
def profile():
    return render_template('admin/profile.html')

@app.route('/admin/events')
@app.route('/admin/events/')
@login_required_redirect(
    login_url="admin_login",
    login_message="Please log in to access this page"
)
@roles_required('SuperUser', 'Admin')
def events():
    return render_template('admin/events.html')

@app.route('/admin/registered_staff')
@app.route('/admin/registered_staff/')
@login_required_redirect(
    login_url="admin_login",
    login_message="Please log in to access this page"
)
@roles_required('SuperUser', 'Admin')
def registered_staff():
    return render_template('admin/registered_staff.html')

@app.route('/admin/analytics')
@app.route('/admin/analytics/')
@login_required_redirect(
    login_url="admin_login",
    login_message="Please log in to access this page"
)
@roles_required('SuperUser', 'Admin')
def analytics():
    return render_template('admin/analytics.html')