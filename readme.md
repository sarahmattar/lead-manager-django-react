# lead-manager-django-react

This is an in depth tutorial application build from Brad Traversy's Youtube series [Fullstack React & Django](https://www.youtube.com/playlist?list=PLillGF-RfqbbRA-CIUxlxkUpbq0IFkX60). 

### Why I Did This

Once I began to get comfirtable with Django and creating template based frontends, I began to wonder: how would React fit on the front end? People do it, but how?The answer to this was remembering that React components, while we are used to seeing them as UI "building blocks" in our application, eventually compiles down to a single Javascript file. That Javascript file can be served as a static file along with any CSS files, and will be referenced inside `index.html`. 

### What I Learned from This

How to allow the backend of the application in Django to communicate with a non native front end in React.  Serializers via the Django Rest Framework convert the querysets and models from SQL to JSON based data for the front end, and Viewsets to manage permissions for each Model. 

How to configure Webpack for monitoring React component builds in development. 

Reinforcement of Redux knowledge for the front end state management. 

And evidently, through much bleary eyed command-lining.... how to deploy a subtree of a git repository to Heroku. 

### Installation Instructions

Installation requires Python 3.8 and Django 3 to be installed on your local machine. 

1. Clone the project repository
2. Use Pipenv to create a virtual environment: 
   1. `pip install pipenv`
   2. `pipenv shell`
3. Change directories into `lead_manager`
4. `python manage.py runserver`
5. This will launch the application on `localhost:8000`

