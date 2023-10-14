from app.backup_restore.restore import *

def execute_restoration():
    """
    Function that executes data restoration to the database from the json file
    """
    try:
        prepare_data_restoration()
        restore_data()
    except Exception as err:
        app.logger.error(err)