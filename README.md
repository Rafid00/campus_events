Campus Events Directory

This is a Django web application for a campus events directory. The main idea of the project is that normal users can submit events through the website, but those events do not appear publicly straight away. An admin has to review and approve them first through the Django admin panel.

This project was built using Django and SQLite.

Main features

Users can:
- view approved events
- view event details
- browse event categories
- submit a new event

Admin can:
- create and manage categories
- review submitted events
- approve pending events so they appear on the public site

Important note

All newly submitted events are saved as pending by default. They only become visible on the website after admin approval.

How to run the project

1. Open terminal in the project folder.

2. Create a virtual environment:
python -m venv venv

3. Activate the virtual environment.
On Windows:
.\venv\Scripts\activate

4. Install Django:
pip install django

5. Run migrations:
python manage.py makemigrations
python manage.py migrate

6. Create a superuser:
python manage.py createsuperuser
Then enter a username, email, and password when prompted.

7. Start the server:
python manage.py runserver

8. Open the website in browser:
http://127.0.0.1:8000/
Admin page:
http://127.0.0.1:8000/admin/

How the project works

The homepage shows only approved events.

Users can submit an event using the event submission form. After submission, the event is stored in the database with is_approved set to False.

The admin logs into the Django admin panel and reviews submitted events. Once an event is approved, it becomes visible on the public pages.

Project structure

campus_events/
- campus_events/ -> project settings and main urls
- events_app/ -> app logic including models, views, admin, forms, and urls
- templates/ -> html templates
- db.sqlite3 -> database file
- manage.py -> Django management file

Validation and security

This project includes:
- required field validation
- email validation
- check that end date/time is later than start date/time
- CSRF protection in forms
- safe object retrieval using get_object_or_404()
- custom 404 and 500 error pages