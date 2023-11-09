from app import app
from flask import render_template
from app.forms import AddAdminForm, AdminActionForm
from app.controllers.read import fetch_active_admins, fetch_active_roles
from app.auth_views import roles_required, login_required_redirect
from flask_login import current_user
from app.aws.s3.fetch_backups import fetch_backups_list

@app.route('/superuser/dashboard')
@app.route('/superuser/dashboard/')
@app.route('/superuser/')
@app.route('/superuser')
@login_required_redirect(
    login_url="admin_login",
    login_message="Please log in to access this page"
)
@roles_required('SuperUser')
def superuser_dashboard():
    return render_template('superuser/dashboard.html')

@app.route('/superuser/users')
@app.route('/superuser/users/')
@login_required_redirect(
    login_url="admin_login",
    login_message="Please log in to access this page"
)
@roles_required('SuperUser')
def users():
    add_admin_form=AddAdminForm()
    staff_roles = fetch_active_roles().all()
    staff_role_options = [(role.id, role.role)
                                  for role in staff_roles]
    add_admin_form.role.choices.extend(staff_role_options)
    admins = fetch_active_admins().all()
    admins_count = len(admins)
    return render_template('superuser/users.html',
                           add_admin_form=add_admin_form,
                           admin_action_form=AdminActionForm(),
                           admins=admins,
                           admins_count=admins_count)

@app.route('/superuser/backup_restore')
@app.route('/superuser/backup_restore/')
@login_required_redirect(
    login_url="admin_login",
    login_message="Please log in to access this page"
)
@roles_required('SuperUser')
def backup_restore():
    return render_template('superuser/backup_restore.html',
                           backups=reversed(fetch_backups_list()),
                           backup_count = len(fetch_backups_list()))