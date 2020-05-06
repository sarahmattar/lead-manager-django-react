# lead-manager-django-react

This is an in-depth tutorial application build from Brad Traversy's Youtube series [Fullstack React & Django](https://www.youtube.com/playlist?list=PLillGF-RfqbbRA-CIUxlxkUpbq0IFkX60). 

### Why I Did This

Once I began to get comfortable with Django and creating template based frontends, I began to wonder: how would React fit on the front end? People do it, but how? The answer to this was remembering that React components, while we are used to seeing them as UI "building blocks" in our application, eventually transpile to a single Javascript file. That Javascript file can be served as a static asset along with any CSS files in Django, and will be referenced inside `index.html`. 

### What I Learned from This

How to allow the backend of the application in Django to communicate with a front end in built in React.  Serializers via the Django Rest Framework convert the querysets and models from SQL to JSON based data for the front end, and Viewsets to manage permissions for each Model. 

- How to configure Webpack for monitoring React component builds in development. 

- Reinforcement of Redux knowledge for the front end state management. 

- Deployment of an application that concurrently runs both Node and Python based applications. 

### Deployment and DevOps

This was a complicated deploy to [Heroku](https://morning-sea-14847.herokuapp.com/), as it required an 'outer' Node application to run Webpack, and an 'inner' Python installation to run Django. Furthermore, all the files that Heroku needed for running the Python or Node buildpacks needed to be brought up to the root level of the project, which meant dismantling the folder structure of the Django project, while keeping the project and its apps intact: 

- Buildpacks were installed for both Node and Python, and instructed to run in that order
- Python and Django-specific files - `Pipfile`, `Procfile`, `requirements.txt` and `runtime.txt` - were brought up from inside the Django project folder to the project root folder
- The Django project folder was deleted, so the Django apps and the project's API folder were moved to the root project level
- A Postgres Database was provisioned for the application to replace the SQLite3 starter database
- Adding a `release` phase to the Procfile for automatic database migration upon build
- Config variables were set to match local environment variables
- A `postinstall` script was added to `package.json` to instruct Webpack to run in production mode immediately after the buildpack installation
- Webpack scripts were modified to reflect the changes to the output location
- `engines` were added to `package.json` to specify the versions of Node and NPM used 

### Installation Instructions

1. Clone the project repository
2. Use Pipenv to create a virtual environment: 
   1. `pip install pipenv`
   2. `pipenv shell`
3. Change directories into `lead_manager`
4. `python manage.py runserver`
5. This will launch the application on `localhost:8000`

