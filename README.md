# Savannah Online Services
## _A simple order placement system for Savannah Limited._

## _***<Image will come here>***_

![Build Status](https://img.shields.io/github/directory-file-count/samariwa/savannah_online_services?style=flat-square) ![Build Status](https://img.shields.io/github/languages/count/samariwa/savannah_online_services?color=red&style=flat-square) ![Build Status](https://img.shields.io/github/languages/top/samariwa/savannah_online_services?color=green&style=flat-square)
![Build Status](https://img.shields.io/github/contributors/samariwa/savannah_online_services?color=green&style=flat-square)

## General Description

This system is a web application that is used by Savannah Limited's staff to place customer orders. It is built using Python's Flask framework which leverages on HTML, CSS, JavaScript and Python as the major programming languages. PostgreSQL was used as the database and it was manipulated by SQLAlchemy ORM (Object Relational Mapper) on the application side. The software has been built to run on a Linux environment that has a number of dependencies installed. These prerequisites shall be discussed at a later part of this documentation.

## Features

- User authentication with both locally created credentials and OpenID Connect + OAuth2 data authorization
- Customer management (CRUD [create, read, update, delete]) using REST APIs
- Order placement with CRUD operations using REST APIs
- Customer SMS alerts once their order has been placed

## Application Structure

The web application uses the general MVC (Model, View, Controller) convention provided by modern frameworks such as Flask and Django. The app structure is illustrated in the diagram below.
##### _***<Application structure diagram>***_
### Models

### Views

### Controllers

## Application setup
As mentioned earlier, this application was built to run on Linux environments. The Linux OS (Operating System) requires the following dependencies to be installed
##### _***<List all dependencies from requirements.txt>***_
A PostgreSQL database server is required either on the same server or on a remote server. The DB (database) server credentials should be entered on the `.config` file which is found on the root directory of the app. For security purposes, I have not uploaded the `.config` file on this public GitHub repository since it contains highly confidential credentials. However, I shall give the structure of the `.config` file in a later part of this documentation.
#### Initial application setup

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
##### Setting up the virtual environment
This is a step in which a virtual Python environment is set up. This environment will run the entire application in isolation from the server's. This step is achieved using the following command.
```sh
root@pc:/home/savannah_online_services# source env/bin/activate
```
##### Installing application package dependecies
All the application's Python dependencies are which are listed in the `requirements.txt` are installed. This is achieved 
##### Initializing environment variables

##### Connecting to the database

##### Populating the database with dummy data

##### Activating debugger

##### Running the application

### Application Testing


