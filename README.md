# Savannah Online Services
## _A simple order placement system for Savannah Limited._

![Alt](https://github.com/samariwa/savannah_online_services/blob/main/app/static/img/savannah_logo.png?raw=true)

![Build Status](https://img.shields.io/github/directory-file-count/samariwa/savannah_online_services?style=flat-square) ![Build Status](https://img.shields.io/github/languages/count/samariwa/savannah_online_services?color=red&style=flat-square) ![Build Status](https://img.shields.io/github/languages/top/samariwa/savannah_online_services?color=green&style=flat-square)
![Build Status](https://img.shields.io/github/contributors/samariwa/savannah_online_services?color=green&style=flat-square)

## General Description
>This system is a web application that is used by Savannah Limited's staff to place customer orders. It is built using Python's Flask framework which leverages on HTML, CSS, JavaScript and Python as the major programming languages. PostgreSQL was used as the database and it was manipulated by SQLAlchemy ORM (Object Relational Mapper) on the application side. The software has been built to run on a Linux environment that has a number of dependencies installed. These prerequisites shall be discussed at a later part of this documentation.

## Features
- User authentication with both locally created credentials and OpenID Connect + OAuth2.0 data authorization
- Customer management (CRUD [create, read, update, delete]) using REST APIs
- Order placement with CRUD operations using REST APIs
- Customer SMS alerts once their order has been placed

## Application Structure
The web application uses the general MVC (Model, View, Controller) convention provided by modern frameworks such as Flask and Django. The app structure is illustrated in the diagram below.
![Alt](https://github.com/samariwa/savannah_online_services/blob/main/app_structure.png?raw=true)
### Models
Like in most frameworks, the models contain the database structure in the form of classes. These classes are used to create data objects which are mapped to database queries by our ORM SQLAlchemy. Examples of classes in our scenario include, User, Customer and Order.
### Views
These contain the frontend interfaces on which users interact with data in the backend. That includes the HTML files which are fould in the `templates` directory. The HTML files are further subdivided into role views as an access control measure and for easier management for example, we have the admin view for the registered admins only(interface on which orders are made), the public views for public facing access. For example, CSS, JavaScript and Images are examples of static files which are found in the `static` directory.
### Controllers
The controllers contain app logic. In my case, I subdivided them into 4 files based on the type of database transaction being performed. They are described below.
- `create.py`: controller for performing all data creation transactions. These are simply database `INSERT` statements pertaining to any model.
- `read.py`: controller for performing all data reading functions. These are simply database `SELECT` statements pertaining to any model.
- `update.py`: controller for performing all data creation transactions. These are simply database `UPDATE` statements pertaining to any model.
- `delete.py`: controller for performing all data deletion transactions. In this applications, we leveraged on soft deletes for purposes of data consistency since this is a relational database and deleting would cause cascading effect. This further helps with data auditing for the organization. Instead of using `DELETE` statements, we toggle between statuses, for example, the `deleted` status signifies that the data is deleted and will not be visible in whatever view that calls data from the database.
### Other significant files
##### Unittest Files
These are files contain unit test modules that test the various functions throughout the application. The modules and methods in them are named using a convention that the unittest library will understand for seamless testing. The tests can be executed using a script that will be discussed in the testing part of this documentation.
##### /africastalking/sms.py
This file contains Africastalking SMS API gateway. This gateway is used to send SMSs of conformation to the customers who make orders or information for those whose orders have an updated state. This gateway interacts with Africastalking using authentication credentials which are environment variables stored in the config file.
##### admin_views.py
This file contains the routes pointing to the admin views (admin webpages).
##### auth_views.py
This file contains the routes pointing to the authentication views (authentication interface).
##### error_views.py
This file contains the routes pointing to the error views (HTTP error pages e.g. 404, 405 response code custom pages).
##### general_functions.py
This file contains some general functions that can be used through out the application, be it authentication, database transaction operations, e.g., UUID generation for the customer_code attribute of the customer model
##### forms.py  
This page utilizes Flask WTForms in creating standard forms that are used throughout the application.
##### views.py
This file contains the routes pointing to the public views (public webpages).
##### \_\_init\_\_.py
This file is used to initialize and start up the various services being used by the Flask application. Some of the services need API keys and/or credentials for authentication. These credentials are stored in as ENV variables that were created in the secret config.py file that we will discuss shortly. Example of services initialized here include, SQLAlchemy, Flask, Africastalking among others.
##### requirements.txt
Like all standard Python applications, this file is crucial in listing all app dependencies and their specific versions for a successful build of the app. The dependencies can be installed using the command in `pip install -r requirements.txt` any environment.
##### run.py
This is the file that contains the main function that runs the up once all the dependencies are set up.
##### config.py (gitignored file)
This file carries the apps security credentials that are required for initialization of the various services. Examples, include, PostgreSQL database(both localhost and live), Mailtrap (email sandbox for testing), Africastalking (for SMS API), among others. This file is read during the makefile executing process and the variables output in the shell from which the ENV variables are set. The structure of the file is as follows:
```sh
config_params = ''
#Localhost PostgreSQL credentials
service = "postgresql+psycopg2"
host = "localhost"
database = "******"
username = “******”
password = “******”
port = "5432"

# Connection
conn_string = f"{service}://{username}:{password}@{host}:{port}/{database}"
config_params += str(conn_string) + ' '

# MAILTRAP
mail_usr = '******'
config_params += str(mail_usr)+' '
mail_pwd = '******'
config_params += str(mail_pwd)+' '

# localhost app secret key
local_app_secret =  '******'
config_params += str(local_app_secret) + ' '

# recaptcha For localhost
L_RECAPTCHA_PUBLIC_KEY = '******'
config_params += str(L_RECAPTCHA_PUBLIC_KEY) + ' '
L_RECAPTCHA_PRIVATE_KEY = '******'
config_params += str(L_RECAPTCHA_PRIVATE_KEY) + ' '

# Organization settings
organization = {
    "mobile": "0711111111",
    "email": "info@savannah.com",
    "location": "This location"
}

config_params += str(organization.get('mobile')) + ' '
config_params += str(organization.get('email')) + ' '
config_params += str(organization.get('location'))

print(config_params)
```
Copy the snippet above and paste it in your config.py file and change the credentials denoted by the asterisk (*) symbol to your credentials. You will need to have a mailtrap, africastalking and google recaptcha account to obtain your personal credentials.
## Application setup
As mentioned earlier, this application was built to run on Linux environments. The Linux OS (Operating System) requires the following dependencies to be installed
|  |  |  |  |  | 
| ------ | ------ | ------ | ------ | ------ |
| Flask==2.2.5 | Flask-Bcrypt==1.0.1 | SQLAlchemy==2.0.15 | anyio==3.7.0 | africastalking==1.2.7 |
| Flask-Login==0.6.2 | Flask-Mail==0.9.1 | Werkzeug==2.2.3 | appnope==0.1.3 | decorator==5.1.1 |
| Flask-Mobility==1.1.0 | Flask-SQLAlchemy==3.0.3 | WTForms==3.0.1 | bleach==6.0.0 | oauthlib==3.0.1 |
| Flask-WTF==1.1.1 | ipykernel==6.23.1 | Flask-pymysql==0.2.3 | blinker==1.6.2 | urllib3==1.26.16 |
| ipython==8.13.2 | Jinja2==3.1.2 | click==8.1.3 | cryptography==40.0.2 | termimado=0.17.1 |
| MarkupSafe==2.1.2 | psycopg2-binary==2.9.6 | alembic==1.11.1 | email-validator==2.0.0 | pyzmq==25.0.2 |


A PostgreSQL database server is required either on the same server or on a remote server. The DB (database) server credentials should be entered on the `.config` file which is found on the root directory of the app. For security purposes, I have not uploaded the `.config` file on this public GitHub repository since it contains highly confidential credentials. However, I shall give the structure of the `.config` file in a later part of this documentation.
### Running the application
To run the application,  a makefile in the root directory of the application needs to be executed using as illustrated below.
```sh
root@pc:/home/savannah_online_services# ls
app/ env/ requirements.txt run_flask_shell.sh* reset_db.py* run.py server_config.sh* make*
root@pc:/home/savannah_online_services# make
starting build...
setting up virtual environment...
checking for app dependencies...
.
.
configuring server...
setting env dependencies...
CONN_STR set successfully
MAIL_USERNAME set successfully
MAIL_PASSWORD set successfully
starting server...
initializing database...
database initialization complete...
build successful...
```
The `make` command as illustrated in the above runs a series of shell scripts which are purposed to fully build the application environment by setting up the virtual environment, installing application package dependencies, initializing ENV(environment) variables, connecting to the database, populating the database with some initial dummy data (when in the test environment), activating debugger (in the test environment) and running the application.
### Application Testing
As mentioned earlier, testing is one of the major sections of this project. It falls under the `/tests` directory. There some unit tests are written with the help of the library `unittest`. Some of the test modules include:
- `test_create_controller.py`: This unit test module tests the various insert functions(and the database contraints) that are found in the `create.py` controller. All functions that create objects and commit to the database are tested here.
- `test_delete_controller.py`: Tests the various delete functions that are found in the `delete.py` controller. All delete functions are tested.
- `test_general_funcs.py`: This tests the general functions found in the `general_functions.py` module that contains functions used throughout the application.
- `test_models.py`: This module tests the SQLAlchemy model classes, how the objects are created and manipulated before being committed to the database.
- `test_update_controller.py`: Tests the various update functions(and the database contraints) that are found in the `update.py` controller. All functions that update database objects are tested in this module.
With the testing modules in place, an all rounded test of all modules can be done at once using the `run_tests.sh` script that is found in the root of the repository. The command is as follows:
```sh
root@pc:/home/savannah_online_services#./run_tests.sh
setting env dependencies...
CONN_STR set successfully
MAIL_USERNAME set successfully
MAIL_PASSWORD set successfully
LOCAL_APP_SECRET set successfully
AFRICASTALKING_USERNAME set successfully
.
.
.
----------------------------------------------------------------------
Ran 19 tests in 1.458s

OK
----------------------------------------
unit tests completed
```
The above command starts by setting ENV variables such as the database connection string which are required for the tests. This is followed by resetting of the database. The reason the database is reset, is to avoid errors related to database contraints that may come up when database related tests are being done. For example, when, running the test twice consecutively, you are likely to get duplicate data error for fields like 'email' in the users creation controller test. This is followed by the test commant which takes into consideration all the tests in the tests directory. The command used is as follows:
```sh
root@pc:/home/savannah_online_services#python -m unittest app/tests/test_*
```
The wildcard * instructs the shell to run all the modules beginning with the word 'test_' in the naming. This is also a standard naming convention required by the unittest module. If the test succeeds, we get the 'OK', status at the end of the test, otherwise we get a 'Failed' status at the end of the test, a brief description of the failed test in the preceding lines.

