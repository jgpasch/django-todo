# Setup
1. get Repo
- clone this repo
- cd into the project root
- switch to the local branch
```
git checkout local
```

2. use your virtual env tool of choice to create a python3 virtual environment. I use python3's native venv module.
```
python3 -m venv ./venv
```

This will create a folder called venv inside of your project root.

3. Activate the venv by running in the project root folder.
```
source env/bin/activate
```

4. install the libs (from proj root)
```
pip install -r requirements.txt
```

5. make sure postgres is installed, and start the postgres server

6. create the file *django-todo/todo/config.json*

7. Paste this json object into the file, filling out your approriate details

```
{
  "database": {
    "NAME": "<your db n ame>",
    "USER": "<your psql username>",
    "PASSWORD": "<your psql password>"
  }
}
```
- You can also change the host/port in settings.py if you are not using the default port on localhost.


8. Go into the psql command line, and create the database with the same name from previous step.

9. Now we need to create a django super user
```
python manage.py createsuperuser
```

- enter the details as prompted (you can leave out email).

10. Start the server
```
python manage.py runserver
```

11. Now we need to create an 'oauth application' in order to get an access token to use the api.

12. navigate to http://localhost:8000/api/admin/ and login with the super user credentials you just made.

13. Under the 'django oauth toolkit' section, click applications. Then choose add application.

14. You just need to set:
- client type: public
- authorization grant type: resource owner password-based
- name: whatever you want

  Then cick save

15. Save the client_id and client_secret, you will need these in the Angular 2 frontend, in order to hit the api.

16. The server setup is complete. Now navigate over to the angular 2 front-end repo in order to set up the front end. https://github.com/jgpasch/ng2-todo-django
