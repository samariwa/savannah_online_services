"""read.py
A module to perform all READ operations in CRUD

order:
-User Crud : User, Account_Verification, Logged_Devices, Newsletter_Subscribers
-Staff Crud: Staff, Staff_Role
"""
from app.models import User , Account_Verification , Logged_Devices 
from app.models import Staff, Staff_Role, Department, Participant
from app.models import Event, Event_Venues, Session, Session_Registration

from sqlalchemy import or_, func
from app import app, db

"""
========================================================
Things to impelement in read controller:
Have a way of:
i) All objects details
ii) Count objects
iii) Reading LIKE filter
========================================================
"""
def read_user(**kwargs):
    """"
    read_user(**kwargs)

    Gets details of one user given any unique attribute

    If found, the function returns the user as an object, otherwise None
    """
    try:
        user_to_get = User.query.filter_by(**kwargs).first()
        if user_to_get is None:
            return None
        else:
            return user_to_get
    except Exception as err:
        app.logger.error(f"Unexpected {err=}")
        return None
    
def fetch_all_users():
    """
    fetch_all_users()

    function that fetches all users in the database regardless of the db status
    """
    return db.session.execute(
        db.select(User.id, User.staff_id, User.user_status,
                  User.email_address, User.login_status, User.last_activity,
                  User.login_attempts, User.db_status, User.password_hash,
                  User.created_at, User.updated_at)
                  .order_by(User.id.asc())
                ).all()

def fetch_all_account_verifications():
    """
    fetch_all_account_verifications()

    function that fetches all user account verification data in the database 
    regardless of the db status
    """
    return db.session.execute(
        db.select(Account_Verification.id, Account_Verification.user_id, 
                  Account_Verification.token, Account_Verification.token_expiry,
                  Account_Verification.db_status, Account_Verification.created_at, 
                  Account_Verification.updated_at)
                  .order_by(Account_Verification.id.asc())
                ).all()

def fetch_all_logged_devices():
    """
    fetch_all_logged_devices()

    function that fetches all logged devices data in the database 
    regardless of the db status
    """
    return db.session.execute(
        db.select(Logged_Devices.id, Logged_Devices.user_id, 
                  Logged_Devices.device_type, Logged_Devices.browser,
                  Logged_Devices.ip_address, Logged_Devices.db_status, 
                  Logged_Devices.created_at, Logged_Devices.updated_at)
                  .order_by(Logged_Devices.id.asc())
                ).all()

########################################################################
#                     STAFF RELATED READ FUNCTIONS                     #
########################################################################
def fetch_all_roles():
    """
    fetch_all_roles()

    function that fetches all staff roles in the database regardless of the db status
    """
    return db.session.execute(
        db.select(Staff_Role.id, Staff_Role.department_id, Staff_Role.role, 
                  Staff_Role.db_status, Staff_Role.created_at, Staff_Role.updated_at)
                  .order_by(Staff_Role.id.asc())
                ).all()

def fetch_active_roles():
    """
    fetch_active_roles()

    Fetches all staff roles that have not been soft deleted
    """
    return Staff_Role.query.filter(Staff_Role.role != 'SuperUser', Staff_Role.db_status != 'deleted').order_by(Staff_Role.id.asc())

def fetch_all_departments():
    """
    fetch_all_departments()

    function that fetches all departments in the database regardless of the db status
    """
    return db.session.execute(
        db.select(Department.id, Department.department, Department.db_status,
                  Department.created_at, Department.updated_at)
                  .order_by(Department.id.asc())
                ).all()

def fetch_active_departments():
    """
    fetch_active_departments()

    function that fetches all departments that have not been soft deleted
    """
    results = db.session.execute(
        db.select(Department.id, Department.department, Department.created_at)
        .filter(Department.db_status != 'deleted')
        .order_by(Department.id.asc())
    )

    departments = []
    for department in results:
        department_details = {}
        department_details['id'] = department.id
        department_details['department'] = department.department
        department_details['participants_count'] = get_departments_participants_count(department.id)
        department_details['created_at'] = department.created_at
        departments.append(department_details)

    return departments

def get_departments_participants_count(department_id):
    """
    get_departments_participants_count(participants_count)

    function that fetches the number of all participants in a department that
    have not been soft deleted
    """
    participants_count =  db.session.execute(
        db.select(Participant)
        .filter(Participant.db_status != 'deleted', Participant.department_id == department_id)
    ).scalars().all()

    return len(participants_count)

def fetch_active_admins():
    """
    fetch_active_admins()

    Fetches all admins that have not been soft deleted
    """
    admins = db.session.execute(
        db.select(User.id, User.email_address, User.user_status, Staff.first_name, Staff.last_name,
                   Staff_Role.role, Department.department
        ).join(Staff, Staff.id == User.staff_id)
        .join(Staff_Role, Staff.role_id == Staff_Role.id)
        .join(Department, Staff_Role.department_id == Department.id)
        .filter(Staff_Role.role != 'SuperUser', User.db_status != 'deleted')
        .order_by(User.id.asc())
    )
    return admins

def fetch_all_staff():
    """
    fetch_all_staff()

    function that fetches all staff in the database regardless of the db status
    """
    return db.session.execute(
        db.select(Staff.id, Staff.role_id, Staff.first_name, Staff.last_name,
                  Staff.db_status, Staff.created_at, Staff.updated_at)
                  .order_by(Staff.id.asc())
                ).all()

def read_staff(id):
    """"
    read_staff(id)

    A method to get details of one staff given a specific staff id
    If found, the function returns the customer as an object, otherwise None

    * note the .one() and [0]
    """
    try:
        staff_to_get = db.session.execute(
            db.select(Staff).filter_by(id=id)).one()
        if staff_to_get is None:
            return None
        else:
            return staff_to_get[0]
    except Exception as err:
        app.logger.error(f"Unexpected {err=}")
        return None
    
def fetch_active_participants():
    """
    fetch_active_participants()

    Fetches all participants that have not been soft deleted
    """
    results = db.session.execute(
        db.select(Participant.id, Participant.first_name, Participant.last_name, 
                  Participant.email_address, Department.department)
                  .join(Department, Participant.department_id == Department.id)
                  .filter(Participant.db_status != 'deleted')
                  .order_by(Participant.id.asc())
                ).all()

    participants = []
    for participant in results:
        participant_details = {}
        participant_details['id'] = participant.id
        participant_details['first_name'] = participant.first_name
        participant_details['last_name'] = participant.last_name
        participant_details['email_address'] = participant.email_address
        participant_details['department'] = participant.department
        participant_details['sessions_count'] = get_participant_sessions_count(participant.id)
        participants.append(participant_details)

    return participants

def fetch_participant_details(participant_id):
    """
    fetch_participant_details(participant_id)

    Fetches the details of a participant whose ID is passed in an ID
    """
    return db.session.execute(
        db.select(Participant.first_name, Participant.last_name, 
                  Participant.email_address, Department.department)
                  .join(Department, Participant.department_id == Department.id)
                  .filter(Participant.id == participant_id)
                ).one()

def get_participant_sessions_count(participant_id):
    """
    get_participant_sessions_count(participant_id)

    function that fetches the number of all sessions a participant has registered
    for that have not been soft deleted
    """
    sessions_count =  db.session.execute(
        db.select(Session_Registration)
        .filter(Session_Registration.db_status != 'deleted', 
                Session_Registration.participant_id == participant_id)
    ).scalars().all()

    return len(sessions_count)

def get_participant_events_count(participant_id):
    """
    get_participant_sessions_count(participant_id)

    function that fetches the number of all sessions a participant has registered
    for that have not been soft deleted
    """
    sessions_count =  db.session.execute(
        db.select(Session_Registration)
        .join(Session, Session_Registration.session_id == Session.id)
        .join(Event, Session.event_id == Event.id)
        .filter(Event.db_status != 'deleted',
                Session.db_status != 'deleted',
                Session_Registration.db_status != 'deleted',
                Session_Registration.participant_id == participant_id)
    ).scalars().all()

    return len(sessions_count)


def fetch_active_events():
    """
    fetch_active_events()

    Fetches all events that have not been soft deleted
    """
    results = db.session.execute(
        db.select(Event.id, Event.event_uuid, Event.event,\
                  Event.start_date, Event.end_date)
                  .filter(Event.db_status != 'deleted')
                  .order_by(Event.id.asc())
                ).all()

    events = []
    for event in results:
        event_details = {}
        event_details['id'] = event.id
        event_details['event_uuid'] = event.event_uuid
        event_details['event'] = event.event
        event_details['start_date'] = event.start_date
        event_details['end_date'] = event.end_date
        event_details['sessions_count'] = get_event_sessions_count(event.event_uuid)
        events.append(event_details)

    return events

def get_event_sessions_count(event_uuid):
    """
    get_event_sessions_count(event_uuid)

    function that fetches the number of all sessions an event has
    and that have not been soft deleted
    """
    sessions_count =  db.session.execute(
        db.select(Session)
        .join(Event, Session.event_id == Event.id)
        .filter(Session.db_status != 'deleted', 
                Event.event_uuid == event_uuid)
    ).scalars().all()

    return len(sessions_count)

def fetch_active_event_venues():
    """
    fetch_active_event_venues()

    function that fetches all event venues that have not been soft deleted
    """
    event_venues = db.session.execute(
        db.select(Event_Venues.id, Event_Venues.venue, Event_Venues.created_at)
        .filter(Event_Venues.db_status != 'deleted')
        .order_by(Event_Venues.id.asc())
    )

    venues = []
    for venue in event_venues:
        venue_details = {}
        venue_details['id'] = venue.id
        venue_details['venue'] = venue.venue
        venue_details['session_count'] = get_event_venue_session_count(venue.id)
        venue_details['created_at'] = venue.created_at
        venues.append(venue_details)

    return venues
    
def get_event_venue_session_count(venue_id):
    """
    get_event_venue_session_count(venue_id)

    function that fetches the number of all sessions in an event venue 
    that have not been soft deleted
    """
    venue_sessions =  db.session.execute(
        db.select(Session)
        .filter(Session.db_status != 'deleted', Session.event_venue_id == venue_id)
    ).scalars().all()

    return len(venue_sessions)

def fetch_all_sessions():
    """
    fetch_all_sessions()

    Fetches all sessions that are in the database regardless of the status
    """
    return Session.query.filter(Session.db_status != 'deleted').order_by(Session.id.asc())

def fetch_active_sessions(event_uuid):
    """
    fetch_active_sessions(event_id)

    Fetches all sessions that have not been soft deleted
    """
    return db.session.execute(
        db.select(Session.id, Session.session_uuid, Session.session,\
                  Session.session_description, Event_Venues.venue,
                  Session.start_timestamp, Session.end_timestamp, Session.db_status)
        .join(Event_Venues, Session.event_venue_id == Event_Venues.id)
        .join(Event, Session.event_id == Event.id)
        .filter(Session.db_status != 'deleted', Event.event_uuid == event_uuid)
        .order_by(Session.id.asc())
    )

def get_event_sessions_count(event_uuid):
    """
    get_event_sessions_count(event_uuid)

    function that fetches the number of all sessions in an event 
    that have not been soft deleted
    """
    sessions =  db.session.execute(
        db.select(Session)
        .join(Event, Session.event_id == Event.id)
        .filter(Session.db_status != 'deleted', Event.event_uuid == event_uuid)
    ).scalars().all()

    return len(sessions)

def fetch_active_session_registrations():
    """
    fetch_active_session_registrations()

    Fetches all session registrations that have not been soft deleted
    """
    return Session_Registration.query.filter(Session_Registration.db_status != 'deleted').order_by(Session_Registration.id.asc())

def fetch_department_participants(department_id):
    """
    fetch_active_sessions(event_id)

    Fetches all participants under a certain department whose department id is passed
     as a parameter and that have not been soft deleted
    """
    results = db.session.execute(
        db.select(Participant.id, Participant.first_name, Participant.last_name, Participant.email_address)
        .filter(Participant.db_status != 'deleted', Participant.department_id == department_id)
        .order_by(Participant.id.asc())
    )

    participants = []
    for participant in results:
        participant_details = {}
        participant_details['first_name'] = participant.first_name
        participant_details['last_name'] = participant.last_name
        participant_details['email_address'] = participant.email_address
        participant_details['sessions_count'] = get_participant_sessions_count(participant.id)
        participants.append(participant_details)

    return participants

def fetch_department_details(department_id):
    """
    fetch_department_details(department_id)

    Fetches the details of the department whose id is passed
    as a parameter
    """
    try:
        return db.session.execute(
            db.select(Department.id, Department.department, Department.created_at)
            .filter(Department.id == department_id)
        ).one()
    except Exception as err:
        return None

def fetch_event_details(event_uuid):
    """
    fetch_event_details(event_id)

    Fetches the details of the event whose id is passed
    as a parameter
    """
    try:
        return db.session.execute(
            db.select(Event.event_uuid, Event.event, Event.start_date, Event.end_date)
            .filter(Event.event_uuid == event_uuid)
        ).one()
    except Exception as err:
        return None

def fetch_event_venue_sessions(event_venue_id):
    """
    fetch_event_venue_sessions(event_venue_id)

    Fetches all sessions under an event venue whose id is passed
    as a parameter and that have not been soft deleted
    """
    results = db.session.execute(
        db.select(Session.id, Event.event, Session.session)
        .join(Event, Session.event_id == Event.id)
        .join(Event_Venues, Session.event_venue_id == Event_Venues.id)
        .filter(Session.db_status != 'deleted', Event_Venues.id == event_venue_id)
        .order_by(Session.id.asc())
    )

    sessions = []
    for session in results:
        session_details = {}
        session_details['event'] = session.event
        session_details['session'] = session.session
        session_details['participants_count'] = get_session_participants_count(session.id)
        sessions.append(session_details)

    return sessions

def get_session_participants_count(session_id):
    """
    get_session_participants_count(session_id)

    function that fetches the number of all participants who registered for a
    session and have not been soft deleted
    """
    participants_count =  db.session.execute(
        db.select(Session_Registration)
        .filter(Session_Registration.db_status != 'deleted', 
                Session_Registration.session_id == session_id)
    ).scalars().all()

    return len(participants_count)

def fetch_session_participants(session_uuid):
    """
    fetch_session_participants(session_uuid)

    Fetches all participants of a session whose uuid is passed
    as a parameter and that have not been soft deleted
    """
    results = db.session.execute(
        db.select(Session.id, Participant.first_name, Participant.last_name, Participant.email_address, 
                  Session_Registration.created_at, Department.department)
        .join(Session_Registration, Session.id == Session_Registration.session_id)
        .join(Participant, Session_Registration.participant_id == Participant.id)
        .join(Department, Participant.department_id == Department.id)
        .filter(Participant.db_status != 'deleted', Session.session_uuid == session_uuid)
        .order_by(Session.id.asc())
    )

    participants = []
    for participant in results:
        participant_details = {}
        participant_details['first_name'] = participant.first_name
        participant_details['last_name'] = participant.last_name
        participant_details['email_address'] = participant.email_address
        participant_details['created_at'] = participant.created_at
        participant_details['department'] = participant.department
        participants.append(participant_details)

    return participants

def fetch_event_venue_details(venue_id):
    """
    fetch_event_venue_details(venue_id)

    Fetches the details of the event venue whose id is passed
    as a parameter
    """
    try:
        return db.session.execute(
            db.select(Event_Venues.id, Event_Venues.venue, Event_Venues.created_at)
            .filter(Event_Venues.id == venue_id)
        ).one()
    except Exception as err:
        return None

def fetch_participant_sessions(participant_id):
    """
    fetch_participant_sessions(participant_id)

    Fetches all sessions and events of a participant whose id is passed
    as a parameter and that have not been soft deleted
    """
    results = db.session.execute(
        db.select(Event.event_uuid, Event.event, Event.start_date, Event.end_date, Session.session)
        .join(Session_Registration, Session.id == Session_Registration.session_id)
        .join(Event, Session.event_id == Event.id)
        .filter(Session.db_status != 'deleted', Session_Registration.participant_id == participant_id)
        .order_by(Session.id.asc())
    )
    """
    Dict Format
    {
     3bh43-34bui3-43nb34-23b34iu3: {
                                    'Event': 'Science Week',
                                    'Start Date': '2021-09-13',
                                    'End Date': '2021-09-17',
                                    'Sessions Count': 2,
                                    'Sessions': ['Session 1', 'Session 2']
                                },
     weu273-b3483483-28434-23bb3: {
                                    'Event': 'Maths Week',
                                    'Start Date': '2021-09-13',
                                    'End Date': '2021-09-17',
                                    'Sessions Count': 2,
                                    'Sessions': ['Session 1', 'Session 2']
                                }
    }
    UUID is used as a unique ID and not event name because and event name can
    occur more than once for different instances
    """
    registered_events = {}

    for session in results:
        if not registered_events.get(session.event_uuid):
            registered_events[session.event_uuid] = {}
            registered_events[session.event_uuid]['event'] = session.event
            registered_events[session.event_uuid]['start_date'] = session.start_date
            registered_events[session.event_uuid]['end_date'] = session.end_date
            registered_events[session.event_uuid]['sessions_count'] = 1
            registered_events[session.event_uuid]['sessions'] = [session.session]
        else:
            registered_events[session.event_uuid]['sessions_count'] += 1
            registered_events[session.event_uuid]['sessions'].append(session.session)

    return registered_events

def fetch_session_event_uuid(session_uuid):
    """
    fetch_session_event_uuid(session_uuid)

    Fetches the uuid of the event whose session uuid is passed
    as a parameter
    """
    try:
        return db.session.execute(
            db.select(Event.event_uuid)
            .join(Session, Session.event_id == Event.id)
            .filter(Session.session_uuid == session_uuid)
        ).one()
    except Exception as err:
        return None

def fetch_session_details(session_uuid):
    """
    fetch_session_details(session_uuid)

    Fetches the details of the session whose uuid is passed
    as a parameter
    """
    try:
        return db.session.execute(
        db.select(Session.id, Session.session_uuid, Session.session, 
                  Session.session_description, Session.start_timestamp, 
                  Session.end_timestamp, Event_Venues.venue, Session.db_status,
                  Event.event)
        .join(Event_Venues, Session.event_venue_id == Event_Venues.id)
        .join(Event, Session.event_id == Event.id)
        .filter(Session.session_uuid == session_uuid)
        ).one()
    except Exception as err:
        return None
    
def participant_id_given_email(participant_email):
    """
    participant_id_given_email(participant_email)

    Fetches the id of a participant whose email is passed
    as a parameter
    """
    try:
        return db.session.execute(
            db.select(Participant.id)
            .filter(Participant.email_address == participant_email)
        ).one()
    except Exception as err:
        return None
    
def fetch_session_registration(session_id, participant_id):
    """
    fetch_session_registration(session_id, participant_id)

    Fetches the id of a session_registration whose id is passed
    together with the session id as parameters
    """
    try:
        return db.session.execute(
            db.select(Session_Registration.id)
            .filter(Session_Registration.session_id == int(session_id), Session_Registration.participant_id == int(participant_id))
        ).one()
    except Exception as err:
        return None
    

    