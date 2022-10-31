# DjangoTest
A test of Django based on a 3h youtube video. This to help choose between Flask and Django for my StudentResultSaver project



-Command line:
cd DjangoTest
cd ..

-Activate virtual environment without relaunch
.env/Scripts/Activate.ps1

-To create Django project:
django-admin startproject DjangoTest

-To run server type in terminal:
py manage.py runserver

-To create Django-app:
py manage.py startapp main

-To update (commit) database:
py manage.py migrate

-To stage database changes:
py manage.py makemigrations main

-Get into manual manager control:
py manage.py shell

-My admin is "John_admin" (standard password)
python manage.py createsuperuser John_admin
http://127.0.0.1:8000/admin/

