#!/bin/bash
# a script to set environment variables for symphafresh
# web system requirements

echo "setting env dependencies..."
CONFIG_ARGS=($(python config.py))

if [[ ! -z CONN_STR ]]; then
    export CONN_STR=${CONFIG_ARGS[0]}
    echo "CONN_STR set successfully"
else
    CONN_STR=${CONFIG_ARGS[0]}
    echo "CONN_STR updated successfully"
fi

if [[ ! -z MAIL_USERNAME ]]; then
    export MAIL_USERNAME=${CONFIG_ARGS[1]}
    echo "MAIL_USERNAME set successfully"
else
    MAIL_USERNAME=${CONFIG_ARGS[1]}
    echo "MAIL_USERNAME updated successfully"
fi

if [[ ! -z MAIL_PASSWORD ]]; then
    export MAIL_PASSWORD=${CONFIG_ARGS[2]}
    echo "MAIL_PASSWORD set successfully"
else
    MAIL_PASSWORD=${CONFIG_ARGS[2]}
    echo "MAIL_PASSWORD updated successfully"
fi

if [[ ! -z LOCAL_APP_SCRT ]]; then
    export LOCAL_APP_SCRT=${CONFIG_ARGS[4]}
else
    LOCAL_APP_SCRT=${CONFIG_ARGS[4]}
fi

if [[ ! -z L_RECAPTCHA_PUBLIC_KEY ]]; then
    export L_RECAPTCHA_PUBLIC_KEY=${CONFIG_ARGS[7]}
else
    L_RECAPTCHA_PUBLIC_KEY=${CONFIG_ARGS[7]}
fi

if [[ ! -z L_RECAPTCHA_PRIVATE_KEY ]]; then
    export L_RECAPTCHA_PRIVATE_KEY=${CONFIG_ARGS[8]}
else
    L_RECAPTCHA_PRIVATE_KEY=${CONFIG_ARGS[8]}
fi

if [[ ! -z AWS_ACCESS_KEY ]]; then
    export AWS_ACCESS_KEY=${CONFIG_ARGS[9]}
else
    AWS_ACCESS_KEY=${CONFIG_ARGS[9]}
fi

if [[ ! -z AWS_SECRET_KEY ]]; then
    export AWS_SECRET_KEY=${CONFIG_ARGS[10]}
else
    AWS_SECRET_KEY=${CONFIG_ARGS[10]}
fi

if [[ ! -z MOBILE ]]; then
    export MOBILE=${CONFIG_ARGS[11]}
else
    MOBILE=${CONFIG_ARGS[11]}
fi

if [[ ! -z EMAIL ]]; then
    export EMAIL=${CONFIG_ARGS[12]}
else
    EMAIL=${CONFIG_ARGS[12]}
fi

if [[ ! -z LOCATION ]]; then
    export LOCATION=${CONFIG_ARGS[13]}
else
    LOCATION=${CONFIG_ARGS[13]}
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
python run.py