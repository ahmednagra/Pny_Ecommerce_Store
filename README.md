{% if False %}

# Introduction

The goal of this project is to provide Ecomeerece Solution. Am working time to time and add further functionalities with time.

![Default Home View](__screenshots/1.png))
![Default Home View](__screenshots/2.png))

### Main features

* User Section
* User registration and logging 

* Categories CRUD section
* Product by category and user

* 

* Separated requirements files

* SQLite by default if no env variable is set

# Usage

To use this Web Solution to start your own project:

### Existing virtualenv

If your project is already in an existing python3 virtualenv first install django by running

    $ pip install django
    
And then run the `django-admin.py` command to start the new project:

    $ django-admin.py startproject \
      --template=https://github.com/ahmednagra/Pny_Ecommerce_Store.git \
      --extension=py,md \
      <project_name>
      
### No virtualenv

This assumes that `python3` is linked to valid installation of python 3 and that `pip` is installed and `pip3`is valid
for installing python 3 packages.

Installing inside virtualenv is recommended, however you can start your project without virtualenv too.

If you don't have django installed for python 3 then run:

    $ pip3 install django
    
And then:

    $ python3 -m django python_portfolio \
      --template=https://github.com/ahmednagra/Pny_Ecommerce_Store.git \
      --extension=py,md \
      <project_name>
      
      
After that just install the local dependencies, run migrations, and start the server.

{% endif %}

# {{ project_name|title }}

# Getting Started

First clone the repository from GitHub and switch to the new directory:

    $ git clone git@github.com/ahmednagra/{{ Pny_Ecommerce_Store }}.git
    $ cd {{ Pny_Ecommerce_Store }}
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver
