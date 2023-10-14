from app import app, admin_views, auth_views, views, superuser_views, crud_functions, error_views
import os

if __name__ == "__main__":
    debugger = True

    app.run(port=8000, debug=debugger)
