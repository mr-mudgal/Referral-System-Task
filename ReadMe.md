How to execute and run the Django Application with docker?
- Note: The Django application is Dockerized using Dockerfile and Docker Compose.
- Open terminal in the root directory of the project, where Dockerfile and manage.py file exists.
- Execute the following command 'docker-compose up' to start the container.
- If the container doesn't start or display some error, execute command 'docker-compose build' and wait until the built is over, then execute 'docker-compose up' again and it would work fine now.
- When successfully started, open browser and go to http://localhost:8000

How to execute and run the Django Application without Docker?
- Make sure you have all the dependencies installed as mentioned in requirements.txt. To install all at once execute command 'pip -r requirements.txt'.
- Open the terminal and execute the following command: 'python manage.py runserver'
- Then go to browser and open http://localhost:8000

Points to Remember:
- Django Application contain only one app userRegistration.
- Unit Tests for Django apps are written in sub-directories inside tests directory.
- db.sqlite3 is our database file and manage.py is our entry point file.
- forms.py inside userRegistration directory is the form for registration.
- models.py inside userRegistration directory contains the database schema for the user.
- urls.py inside userRegistration directory contains all the API endpoints which can be used for different functinality over the website. Comments are written beside it and in their respective view function to know what API and view function does what.
- views.py inside userRegistration directory contains all the logical function which are being used all over the userRegistration app and API endpoints.
- templates sub-directory inside userRegistration directory contains html file to be rendered when some API endpoint is being called.

For any query raise issue or comment in the repository.

Thank You

coded by: <Rishabh Mudgal />
