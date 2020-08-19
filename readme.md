# lead-manager-django-react

This is an in-depth tutorial application build from Brad Traversy's Youtube series [Fullstack React & Django](https://www.youtube.com/playlist?list=PLillGF-RfqbbRA-CIUxlxkUpbq0IFkX60) , which uses Django to create a web server, and React (compiled with Node running Webpack) to create the UI. 

This repo contains the destructured application optimized for Heroku deployment. To see the Node and Django applications in their original state, check out [lead-manager-django-react_pre-deploy](https://github.com/sarahmattar/lead-manager-django-react_pre-deploy).

### Deployment and DevOps

This was a complicated deploy to [Heroku](https://morning-sea-14847.herokuapp.com/), as it required an 'outer' Node application to run Webpack, and an 'inner' Python installation to run Django. Furthermore, all the files that Heroku needed for running the Python and Node buildpacks needed to be brought up to the root level of the project, which meant dismantling the folder structure of the Django project, while keeping the project and its apps intact: 

- Buildpacks were installed for both Node and Python applications, and instructed to run in that order
- The Python and Django-specific files - `Pipfile`, `Procfile`, `requirements.txt` and `runtime.txt` - were brought up from inside the Django project folder to the project root folder
- The Django project folder was deleted, so the Django apps and the project's API folder were moved to the root project level
- A Postgres Database was provisioned for the application to replace the SQLite3 starter database
- A `release` phase was added to the `Procfile` for automatic database migration upon a successful build
- Heroku config variables were set to match local environment variables that were stored in an `.env` file
- A `postinstall` script was added to `package.json` to instruct Webpack to run in production mode immediately after the buildpack installation
- Webpack scripts were modified to reflect the changes to the output location
- `engines` were added to `package.json` to specify the versions of Node and NPM used 
