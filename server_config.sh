#!/bin/bash
# a script to set environment variables for the app
# web system requirements

echo "setting env dependencies..."
CONFIG_ARGS=($(python config.py))

if [[ ! -z CONN_STR ]]; then
    export CONN_STR=${CONFIG_ARGS[0]}
    echo "CONN STR set successfully"
else
    CONN_STR=${CONFIG_ARGS[0]}
    echo "CONN STR updated successfully"
fi

if [[ ! -z MAIL_USERNAME ]]; then
    export MAIL_USERNAME=${CONFIG_ARGS[1]}
    echo "MAIL USERNAME set successfully"
else
    MAIL_USERNAME=${CONFIG_ARGS[1]}
    echo "MAIL USERNAME updated successfully"
fi

if [[ ! -z MAIL_PASSWORD ]]; then
    export MAIL_PASSWORD=${CONFIG_ARGS[2]}
    echo "MAIL PASSWORD set successfully"
else
    MAIL_PASSWORD=${CONFIG_ARGS[2]}
    echo "MAIL PASSWORD updated successfully"
fi

if [[ ! -z LOCAL_APP_SCRT ]]; then
    export LOCAL_APP_SCRT=${CONFIG_ARGS[3]}
    echo "LOCAL APP SECRET set successfully"
else
    LOCAL_APP_SCRT=${CONFIG_ARGS[3]}
    echo "LOCAL APP SECRET updated successfully"
fi

if [[ ! -z AFRICASTALKING_USERNAME ]]; then
    export AFRICASTALKING_USERNAME=${CONFIG_ARGS[4]}
    echo "AFRICASTALKING USERNAME set successfully"
else
    AFRICASTALKING_USERNAME=${CONFIG_ARGS[4]}
    echo "AFRICASTALKING USERNAME updated successfully"
fi

if [[ ! -z AFRICASTALKING_API_KEY ]]; then
    export AFRICASTALKING_API_KEY=${CONFIG_ARGS[5]}
    echo "AFRICASTALKING API KEY set successfully"
else
    AFRICASTALKING_API_KEY=${CONFIG_ARGS[5]}
    echo "AFRICASTALKING API KEY updated successfully"
fi

if [[ ! -z L_RECAPTCHA_PUBLIC_KEY ]]; then
    export L_RECAPTCHA_PUBLIC_KEY=${CONFIG_ARGS[6]}
    echo "GRECAPTCHA PUBLIC KEY set successfully"
else
    L_RECAPTCHA_PUBLIC_KEY=${CONFIG_ARGS[6]}
    echo "GRECAPTCHA PUBLIC KEY updated successfully"
fi

if [[ ! -z L_RECAPTCHA_PRIVATE_KEY ]]; then
    export L_RECAPTCHA_PRIVATE_KEY=${CONFIG_ARGS[7]}
    echo "GRECAPTCHA PRIVATE_KEY set successfully"
else
    L_RECAPTCHA_PRIVATE_KEY=${CONFIG_ARGS[7]}
    echo "GRECAPTCHA PRIVATE_KEY updated successfully"
fi

if [[ ! -z GOOGLE_OAUTH_CLIENT_ID ]]; then
    export GOOGLE_OAUTH_CLIENT_ID=${CONFIG_ARGS[8]}
    echo "GOOGLE OAUTH CLIENT ID set successfully"
else
    GOOGLE_OAUTH_CLIENT_ID=${CONFIG_ARGS[8]}
    echo "GOOGLE OAUTH CLIENT ID updated successfully"
fi

if [[ ! -z GOOGLE_OAUTH_CLIENT_SECRET ]]; then
    export GOOGLE_OAUTH_CLIENT_SECRET=${CONFIG_ARGS[9]}
    echo "GOOGLE OAUTH CLIENT SECRET set successfully"
else
    GOOGLE_OAUTH_CLIENT_SECRET=${CONFIG_ARGS[9]}
    echo "GOOGLE OAUTH CLIENT SECRET updated successfully"
fi

if [[ ! -z IP_ADDRESS ]]; then
    export IP_ADDRESS=${CONFIG_ARGS[10]}
    echo "IP ADDRESS set successfully"
else
    IP_ADDRESS=${CONFIG_ARGS[10]}
    echo "IP ADDRESS updated successfully"
fi

if [[ ! -z MOBILE ]]; then
    export MOBILE=${CONFIG_ARGS[11]}
    echo "MOBILE set successfully"
else
    MOBILE=${CONFIG_ARGS[11]}
    echo "MOBILE updated successfully"
fi

if [[ ! -z EMAIL ]]; then
    export EMAIL=${CONFIG_ARGS[12]}
    echo "EMAIL set successfully"
else
    EMAIL=${CONFIG_ARGS[12]}
    echo "EMAIL updated successfully"
fi

if [[ ! -z LOCATION ]]; then
    export LOCATION=${CONFIG_ARGS[13]}
    echo "LOCATION set successfully"
else
    LOCATION=${CONFIG_ARGS[13]}
    echo "LOCATION updated successfully"
fi    

echo "starting server..."
echo "initializing database..."
python reset_db.py
echo "database initialization complete..."
echo "build successful..."
# to run app using gunicorn
# gunicorn run:app

# to run app using the default flask server
#flask --app=run.py --debug run

#to run app using the default flask server
#python run.py
gunicorn --bind 0.0.0.0:8000 --workers=3 wsgi:app
