# django-employee

Steps to go about
=================

------Step1---------
cd django-employee
py -m venv env
env\scripts\activate
--------------------

------Step 2--------
pip install django
--------------------

------Step 3--------
django-admin startproject webapp .
python manage.py startapp employee
--------------------

------Step 4--------
Creating Model
--------------------

------Step 5--------
Create a file 'form.py' in employee and add details
--------------------

------Step 6--------
Add your app in the settings Installed_app (i.e) employee
--------------------

------Step 7--------
# Migration to create tables in database
python manage.py makemigrations
python manage.py migrate
--------------------

------Step 8--------
url, html, view > Welcome page
Create employee/templates/welcome.html
 
In views of employee, add the class for welcome
Then set the url in webapp

python manage.py runserver
--------------------

------Step 9---------
url, html, url > for Add and Load_Form

create a view for form in employee views (load_form.py)
then create index.html in templates of employee and add form

Create one more view with name add for adding functionality

Then go to urls of webapp and add the paths for load_form and add
---------------------

-------Step 10--------
url, html, view Data Show

create show.html in templates
Add view for it
Add url for it
Now add html for it

Redirect after saving - code
----------------------

------Step 11---------
DO same as show for edit operation

Add update functionality to add edited data to db
---------------------

------Step 12--------
Delete by adding view and redirecting to show
---------------------

------Step 13--------
Search by adding view and redirecting to show
---------------------

-----step 14---------
Add styles to the project with bootstrap
---------------------