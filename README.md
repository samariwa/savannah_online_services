# Savannah Online Services
## _A simple order placement system for Savannah Limited._

![Alt](https://github.com/samariwa/savannah_online_services/blob/main/app/static/img/savannah_logo.png?raw=true)

![Build Status](https://img.shields.io/github/directory-file-count/samariwa/savannah_online_services?style=flat-square) ![Build Status](https://img.shields.io/github/languages/count/samariwa/savannah_online_services?color=red&style=flat-square) ![Build Status](https://img.shields.io/github/languages/top/samariwa/savannah_online_services?color=green&style=flat-square)
![Build Status](https://img.shields.io/github/contributors/samariwa/savannah_online_services?color=green&style=flat-square)

## General Description
>This system is a web application that is used by Savannah Limited's staff to place customer orders. It is built using Python's Flask framework which leverages on HTML, CSS, JavaScript and Python as the major programming languages. PostgreSQL was used as the database and it was manipulated by SQLAlchemy ORM (Object Relational Mapper) on the application side. The software has been built to run on a Linux environment that has a number of dependencies installed. These prerequisites shall be discussed at a later part of this documentation.

## Features
- User authentication with both locally created credentials and OpenID Connect + OAuth2 data authorization
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
## Application setup
As mentioned earlier, this application was built to run on Linux environments. The Linux OS (Operating System) requires the following dependencies to be installed
##### _***<List all dependencies from requirements.txt>***_
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


