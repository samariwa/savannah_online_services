from app import app, admin_views, auth_views, views, crud_functions, error_views

if __name__ == "__main__":
    debugger = False

    app.run(port=8000, debug=debugger)
