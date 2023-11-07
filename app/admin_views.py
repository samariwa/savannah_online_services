from app import app, csrf, organization
from app.response import respond
from flask import render_template, make_response, json, request
from app.forms import AddSessionForm, AddEventForm, AddDepartmentForm,\
     AddEventVenueForm
from app.controllers.read import fetch_active_departments, fetch_active_event_venues,\
     fetch_active_sessions
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
    add_event_form = AddEventForm()
    return render_template('admin/events.html', add_event_form = add_event_form)

@app.route('/admin/event/<event_id>')
@app.route('/admin/event/<event_id>/')
@login_required_redirect(
    login_url="admin_login",
    login_message="Please log in to access this page"
)
@roles_required('SuperUser', 'Admin')
def event(event_id):
    add_session_form = AddSessionForm()
    sessions = fetch_active_sessions()
    return render_template('admin/event.html', add_session_form=add_session_form)

@app.route('/admin/event-venues')
@app.route('/admin/event-venues/')
@login_required_redirect(
    login_url="admin_login",
    login_message="Please log in to access this page"
)
@roles_required('SuperUser', 'Admin')
def event_venues():
    add_venue_form = AddEventVenueForm()
    event_venues = fetch_active_event_venues()
    return render_template('admin/event-venues.html', 
                           add_venue_form = add_venue_form,
                           event_venues=event_venues)

@app.route('/admin/event-venue/<venue_id>')
@app.route('/admin/event-venue/<venue_id>/')
@login_required_redirect(
    login_url="admin_login",
    login_message="Please log in to access this page"
)
@roles_required('SuperUser', 'Admin')
def event_venue(venue_id):
    return render_template('admin/event-venue.html')

@app.route('/admin/session/<session_id>')
@app.route('/admin/session/<session_id>/')
@login_required_redirect(
    login_url="admin_login",
    login_message="Please log in to access this page"
)
@roles_required('SuperUser', 'Admin')
def session(session_id):
    return render_template('admin/session.html')

@app.route('/admin/registered_staff')
@app.route('/admin/registered_staff/')
@login_required_redirect(
    login_url="admin_login",
    login_message="Please log in to access this page"
)
@roles_required('SuperUser', 'Admin')
def registered_staff():
    return render_template('admin/registered_staff.html')

@app.route('/admin/staff/<staff_id>')
@app.route('/admin/staff/<staff_id>/')
@login_required_redirect(
    login_url="admin_login",
    login_message="Please log in to access this page"
)
@roles_required('SuperUser', 'Admin',)
def staff(staff_id):
    return render_template(
        'admin/staff.html',
    )

@app.route('/admin/departments')
@app.route('/admin/departments/')
@login_required_redirect(
    login_url="admin_login",
    login_message="Please log in to access this page"
)
@roles_required('SuperUser', 'Admin')
def departments():
    add_department_form = AddDepartmentForm()
    departments = fetch_active_departments()
    return render_template('admin/departments.html',
                           add_department_form = add_department_form,
                           departments=departments)

@app.route('/admin/department/<department_id>')
@app.route('/admin/department/<department_id>/')
@login_required_redirect(
    login_url="admin_login",
    login_message="Please log in to access this page"
)
@roles_required('SuperUser', 'Admin')
def department(department_id):
    return render_template('admin/department.html')

@app.route('/admin/analytics')
@app.route('/admin/analytics/')
@login_required_redirect(
    login_url="admin_login",
    login_message="Please log in to access this page"
)
@roles_required('SuperUser', 'Admin')
def analytics():
    return render_template('admin/analytics.html')