from app import app, csrf, organization
from app.response import respond
from flask import render_template, make_response, json, request, redirect, url_for
from app.forms import AddOrderForm, AddCustomerForm, AdminActionForm
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
                           add_customer_form=AddCustomerForm())

@app.route('/admin/orders')
@app.route('/admin/orders/')
@login_required_redirect(
    login_url="admin_login",
    login_message="Please log in to access this page"
)
def orders():
    add_order_form = AddOrderForm()
    customers = fetch_active_customers()
    customer_options = [(customer.id, customer.first_name+' '+customer.last_name) for customer in customers]
    add_order_form.customer.choices.extend(customer_options)
    return render_template('admin/orders.html',
                           orders=fetch_active_orders(),
                           orders_count=len(fetch_active_orders()),
                           add_order_form=add_order_form)

@app.route('/admin/profile')
@app.route('/admin/profile/')
@login_required_redirect(
    login_url="admin_login",
    login_message="Please log in to access this page"
)
def profile():
    return render_template('admin/profile.html')