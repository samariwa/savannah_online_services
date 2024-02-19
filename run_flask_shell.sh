#!/bin/bash
# a script to set environment variables for the app
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
    export LOCAL_APP_SCRT=${CONFIG_ARGS[3]}
    echo "LOCAL_APP_SECRET set successfully"
else
    LOCAL_APP_SCRT=${CONFIG_ARGS[3]}
    echo "LOCAL_APP_SECRET updated successfully"
fi

if [[ ! -z AFRICASTALKING_USERNAME ]]; then
    export AFRICASTALKING_USERNAME=${CONFIG_ARGS[4]}
    echo "AFRICASTALKING_USERNAME set successfully"
else
    AFRICASTALKING_USERNAME=${CONFIG_ARGS[4]}
    echo "AFRICASTALKING_USERNAME updated successfully"
fi

if [[ ! -z AFRICASTALKING_API_KEY ]]; then
    export AFRICASTALKING_API_KEY=${CONFIG_ARGS[5]}
    echo "AFRICASTALKING_API_KEY set successfully"
else
    AFRICASTALKING_API_KEY=${CONFIG_ARGS[5]}
    echo "AFRICASTALKING_API_KEY updated successfully"
fi

if [[ ! -z L_RECAPTCHA_PUBLIC_KEY ]]; then
    export L_RECAPTCHA_PUBLIC_KEY=${CONFIG_ARGS[6]}
    echo "GRECAPTCHA_PUBLIC_KEY set successfully"
else
    L_RECAPTCHA_PUBLIC_KEY=${CONFIG_ARGS[6]}
    echo "GRECAPTCHA_PUBLIC_KEY updated successfully"
fi

if [[ ! -z L_RECAPTCHA_PRIVATE_KEY ]]; then
    export L_RECAPTCHA_PRIVATE_KEY=${CONFIG_ARGS[7]}
    echo "GRECAPTCHA_PRIVATE_KEY set successfully"
else
    L_RECAPTCHA_PRIVATE_KEY=${CONFIG_ARGS[7]}
    echo "GRECAPTCHA_PRIVATE_KEY updated successfully"
fi

if [[ ! -z GOOGLE_OAUTH_CLIENT_ID ]]; then
    export GOOGLE_OAUTH_CLIENT_ID=${CONFIG_ARGS[8]}
    echo "GOOGLE_OAUTH_CLIENT_ID set successfully"
else
    GOOGLE_OAUTH_CLIENT_ID=${CONFIG_ARGS[8]}
    echo "GOOGLE_OAUTH_CLIENT_ID updated successfully"
fi

if [[ ! -z GOOGLE_OAUTH_CLIENT_SECRET ]]; then
    export GOOGLE_OAUTH_CLIENT_SECRET=${CONFIG_ARGS[9]}
    echo "GOOGLE_OAUTH_CLIENT_SECRET set successfully"
else
    GOOGLE_OAUTH_CLIENT_SECRET=${CONFIG_ARGS[9]}
    echo "GOOGLE_OAUTH_CLIENT_SECRET updated successfully"
fi

if [[ ! -z MOBILE ]]; then
    export MOBILE=${CONFIG_ARGS[10]}
    echo "MOBILE set successfully"
else
    MOBILE=${CONFIG_ARGS[10]}
    echo "MOBILE updated successfully"
fi

if [[ ! -z EMAIL ]]; then
    export EMAIL=${CONFIG_ARGS[11]}
    echo "EMAIL set successfully"
else
    EMAIL=${CONFIG_ARGS[11]}
    echo "EMAIL updated successfully"
fi

if [[ ! -z LOCATION ]]; then
    export LOCATION=${CONFIG_ARGS[12]}
    echo "LOCATION set successfully"
else
    LOCATION=${CONFIG_ARGS[12]}
    echo "LOCATION updated successfully"
fi   

#RUN SHELL
flask --app=run.py --debug shell