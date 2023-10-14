from app import app
from app.general_functions import stringify_datetime_object
from app.controllers.read import fetch_all_departments, fetch_all_users,\
fetch_all_roles, fetch_all_staff, fetch_all_customers

def backup_departments():
    try:
        with open('app/backup_restore/backup_data.py', 'a') as fp:
            fp.write('from app.controllers.create import create_department\n')
            department_data = fetch_all_departments()
            for data in department_data:
                updated_at = data.updated_at
                if data.updated_at is not None:
                    updated_at = stringify_datetime_object(data.updated_at)
                values = {'id': data.id, 
                          'department': data.department,
                          'db_status': data.db_status, 
                          'created_at': stringify_datetime_object(data.created_at),
                          'updated_at': updated_at}
                fp.write('create_department(**'+str(values)+')\n')
            fp.close()
        app.logger.info("Department data backup complete")
    except Exception as err:
        app.logger.error(type(err).__name__+':'+str(err))

def backup_staff_roles():
    try:
        with open('app/backup_restore/backup_data.py', 'a') as fp:
            fp.write('from app.controllers.create import create_staff_role\n')
            roles_data = fetch_all_roles()
            for data in roles_data:
                updated_at = data.updated_at
                if data.updated_at is not None:
                    updated_at = stringify_datetime_object(data.updated_at)
                values = {'id': data.id, 
                          'department_id': data.department_id,
                          'role': data.role,
                          'db_status': data.db_status, 
                          'created_at': stringify_datetime_object(data.created_at),
                          'updated_at': updated_at}
                fp.write('create_staff_role(**'+str(values)+')\n')
            fp.close()
        app.logger.info("Staff Roles data backup complete")
    except Exception as err:
        app.logger.error(type(err).__name__+':'+str(err))

def backup_staff():
    try:
        with open('app/backup_restore/backup_data.py', 'a') as fp:
            fp.write('from app.controllers.create import create_staff\n')
            staff_data = fetch_all_staff()
            for data in staff_data:
                updated_at = data.updated_at
                if data.updated_at is not None:
                    updated_at = stringify_datetime_object(data.updated_at)
                values = {'id': data.id, 
                          'role_id': data.role_id,
                          'first_name': data.first_name,
                          'last_name': data.last_name,
                          'id_number': data.id_number,
                          'yob': data.yob,
                          'gender': data.gender,
                          'nssf_number': data.nssf_number,
                          'nhif_number': data.nhif_number,
                          'db_status': data.db_status, 
                          'created_at': stringify_datetime_object(data.created_at),
                          'updated_at': updated_at}
                fp.write('create_staff(**'+str(values)+')\n')
            fp.close()
        app.logger.info("Staff data backup complete")
    except Exception as err:
        app.logger.error(type(err).__name__+':'+str(err))

def backup_customers():
    try:
        with open('app/backup_restore/backup_data.py', 'a') as fp:
            fp.write('from app.controllers.create import create_customer\n')
            customer_data = fetch_all_customers()
            for data in customer_data:
                updated_at = data.updated_at
                if data.updated_at is not None:
                    updated_at = stringify_datetime_object(data.updated_at)
                values = {'id': data.id, 
                          'first_name': data.first_name,
                          'last_name': data.last_name,
                          'location': data.location,
                          'phone_no': data.phone_no,
                          'customer_type': data.customer_type,
                          'note': data.note,
                          'customer_status': data.customer_status,
                          'credit_customer': data.credit_customer,
                          'db_status': data.db_status, 
                          'created_at': stringify_datetime_object(data.created_at),
                          'updated_at': updated_at}
                fp.write('create_customer(**'+str(values)+')\n')
            fp.close()
        app.logger.info("Customers data backup complete")
    except Exception as err:
        app.logger.error(type(err).__name__+':'+str(err))

def backup_users():
    try:
        with open('app/backup_restore/backup_data.py', 'a') as fp:
            fp.write('from app.controllers.create import create_user\n')
            user_data = fetch_all_users()
            for data in user_data:
                last_activity = data.last_activity
                updated_at = data.updated_at
                if data.last_activity is not None:
                    last_activity = stringify_datetime_object(data.last_activity)
                if data.updated_at is not None:
                    updated_at = stringify_datetime_object(data.updated_at)
                values = {'id': data.id, 
                          'customer_id': data.customer_id,
                          'staff_id': data.staff_id, 
                          'user_status': data.user_status,
                          'email_address': data.email_address, 
                          'login_status': data.login_status,
                          'last_activity': last_activity, 
                          'login_attempts': data.login_attempts,
                          'db_status': data.db_status, 
                          'created_at': stringify_datetime_object(data.created_at),
                          'updated_at': updated_at}
                fp.write('create_user(**'+str(values)+')\n')
            fp.close()
        app.logger.info("User data backup complete")
    except Exception as err:
        app.logger.error(type(err).__name__+':'+str(err))
