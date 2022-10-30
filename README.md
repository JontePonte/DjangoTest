# DjangoTest
A test of Django based on a 3h youtube video. This to help choose between Flask and Django for my StudentResultSaver project



To create Django project:
django-admin startproject DjangoTest

To run server type in terminal:
py DjangoTest/manage.py runserver

To create Django-app:
cd DjangoTest
py manage.py startapp main
cd ..

To update (commit) database:
py DjangoTest/manage.py migrate

To stage database changes:
py DjangoTest/manage.py makemigrations main

Get into manual manager control:
cd DjangoTest
py manage.py shell

