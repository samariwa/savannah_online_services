from app import app, csrf, organization
from app.response import respond
from flask import render_template, make_response, json, request, redirect, url_for
from app.forms import AddSessionForm, AddEventForm, AddDepartmentForm,\
     AddEventVenueForm
from app.controllers.read import fetch_active_departments, fetch_active_event_venues,\
     fetch_active_sessions, fetch_active_participants, fetch_active_events,\
     get_event_sessions_count, fetch_department_participants, fetch_department_details,\
     fetch_event_details, fetch_event_venue_sessions, fetch_event_venue_details,\
     fetch_participant_sessions, fetch_participant_details, get_participant_sessions_count,\
     get_participant_events_count, fetch_session_event_uuid, fetch_session_participants,\
     fetch_session_details
from app.general_functions import datetime, datetime_to_time, datetime_to_standard_date
from app.auth_views import roles_required, login_required_redirect
from flask_login import current_user
import segno

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
    events=fetch_active_events()
    events_count = len(events)
    return render_template('admin/events.html',
                           add_event_form = add_event_form,
                           events=events,
                           events_count=events_count)

@app.route('/admin/event/<event_uuid>')
@app.route('/admin/event/<event_uuid>/')
@login_required_redirect(
    login_url="admin_login",
    login_message="Please log in to access this page"
)
@roles_required('SuperUser', 'Admin')
def event(event_uuid):
    add_session_form = AddSessionForm()
    sessions = fetch_active_sessions(event_uuid)
    sessions_count = get_event_sessions_count(event_uuid)
    event_details = fetch_event_details(event_uuid)
    event_venues = fetch_active_event_venues()
    event_venue_options = [(v['id'], v['venue'])
                                  for v in event_venues]
    add_session_form.session_venue.choices.extend(event_venue_options)
    if event_details is None:
        #response = {'error': 'Error: Event # does not exist'}
        return redirect(url_for('events'))
    else:
        return render_template('admin/event.html', 
                            add_session_form=add_session_form,
                            sessions=sessions,
                            sessions_count=sessions_count,
                            event_details=event_details)

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
    event_venues_count = len(event_venues)
    return render_template('admin/event-venues.html', 
                           add_venue_form = add_venue_form,
                           event_venues=event_venues,
                           event_venues_count=event_venues_count)

@app.route('/admin/event-venue/<venue_id>')
@app.route('/admin/event-venue/<venue_id>/')
@login_required_redirect(
    login_url="admin_login",
    login_message="Please log in to access this page"
)
@roles_required('SuperUser', 'Admin')
def event_venue(venue_id):
    venue_sessions = fetch_event_venue_sessions(venue_id)
    venue_details = fetch_event_venue_details(venue_id)
    if venue_details is None:
        return redirect(url_for('event_venues'))
    else:
        return render_template('admin/event-venue.html',
                            venue_details=venue_details,
                            venue_sessions=venue_sessions,
                            venue_sessions_count=len(venue_sessions)
        )

@app.route('/admin/session/<session_uuid>')
@app.route('/admin/session/<session_uuid>/')
@login_required_redirect(
    login_url="admin_login",
    login_message="Please log in to access this page"
)
@roles_required('SuperUser', 'Admin')
def session(session_uuid):
    event_uuid = fetch_session_event_uuid(session_uuid)
    participants = fetch_session_participants(session_uuid)
    session_details = fetch_session_details(session_uuid)
    if session_details is None:
        #response = [{'error': 'Error: Event # does not exist'}]
        return redirect(url_for('events'))
    else:
        qrcode = segno.make('https://a38f-41-90-190-72.ngrok-free.app/session-registration/'+session_uuid)
        return render_template('admin/session.html',
                            event_uuid=event_uuid,
                            participants=participants,
                            participants_count=len(participants),
                            session_details=session_details,
                            qrcode= qrcode)

@app.route('/admin/registered-staff')
@app.route('/admin/registered-staff/')
@login_required_redirect(
    login_url="admin_login",
    login_message="Please log in to access this page"
)
@roles_required('SuperUser', 'Admin')
def registered_staff():
    participants = fetch_active_participants()
    participants_count = len(participants)
    return render_template('admin/registered-staff.html', 
                           participants=participants,
                           participants_count=participants_count)

@app.route('/admin/staff/<participant_id>')
@app.route('/admin/staff/<participant_id>/')
@login_required_redirect(
    login_url="admin_login",
    login_message="Please log in to access this page"
)
@roles_required('SuperUser', 'Admin',)
def staff(participant_id):
    participant_details = fetch_participant_details(participant_id)
    sessions = fetch_participant_sessions(participant_id)
    sessions_count=get_participant_sessions_count(participant_id)
    events_count=get_participant_events_count(participant_id)
    return render_template(
        'admin/staff.html',
        sessions=sessions,
        sessions_count=sessions_count,
        events_count=events_count,
        participant_details=participant_details
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
                           departments=departments,
                           departments_count=len(departments))

@app.route('/admin/department/<department_id>')
@app.route('/admin/department/<department_id>/')
@login_required_redirect(
    login_url="admin_login",
    login_message="Please log in to access this page"
)
@roles_required('SuperUser', 'Admin')
def department(department_id):
    department_details=fetch_department_details(department_id)
    department_participants=fetch_department_participants(department_id)
    if department_details is None:
        return redirect(url_for('departments'))
    else:
        return render_template('admin/department.html',
                            department_details=department_details,
                            department_participants=department_participants,
                            department_participants_count=len(department_participants))

@app.route('/admin/analytics')
@app.route('/admin/analytics/')
@login_required_redirect(
    login_url="admin_login",
    login_message="Please log in to access this page"
)
@roles_required('SuperUser', 'Admin')
def analytics():
    return render_template('admin/analytics.html')