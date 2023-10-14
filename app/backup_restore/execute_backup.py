#from app.backup_restore.backup_v1 import *
#from app.backup_restore.backup_v2 import *
from app.backup_restore.backup_v3 import *
from app.response import respond

def execute_backup():
    """
    Function that executes all data backup from the database and stores 
    them in a json file
    """
    try:
        prepare_backup_file()
        backup_url = run_backup()
        return respond('200')
    except Exception as err:
        app.logger.error(err)


"""
def execute_backup_old():

    Function that executes all data backup from the database and stores creation objects

    try:
        backup_departments()
        backup_staff_roles()
        backup_staff()
        backup_customers()
        backup_users()
        app.logger.info("Data backup completed successfully")
    except Exception as err:
        app.logger.error(err)
"""