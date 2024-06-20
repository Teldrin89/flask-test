# FLASK TUTORIAL
This repository holds codebase of flask application tutorial.
The next sections describe consecutive parts of test flas app.
Reference of tutorial web page: 
[Flask](https://flask.palletsprojects.com/en/3.0.x/tutorial/)

## Typical app tree
Simple Flask application can be made with single python script - exampe in 
`hello.py`. ImportingFlask library and starting the app as Flask class. The 
more "complete" app may have a tree looking similar to this one
```
/home/user/Projects/flask-tutorial
|---- flaskr/
|     |---- __init__.py
|     |---- db.py
|     |---- schema.sql
|     |---- auth.py
|     |---- blog.py
|     |---- templates/
|     |     |---- base.html
|     |     |---- auth/
|     |     |     |---- login.html
|     |     |     |---- register.html
|     |     |---- blog/
|     |           |---- create.html
|     |           |---- index.html
|     |           |---- update.html
|     |---- static/
|           |---- style.css
|---- tests/
|     |---- conftest.py
|     |---- data.sql
|     |---- test_factory.py
|     |---- test_db.py
|     |---- test_auth.py
|     |---- test_blog.py
|---- .venv/
|---- pyproject.toml
|---- MANIFEST.in
```

## Initial app setup
The initial app file for more complex project is made in `flaskr` directory
and it starts with name `__init__` indicating for Python interpreter that it
should be treated as package. Inside it holds:
- a main function `create_app` that is the application factory function
- it creates a the Flask instance `app=Flask(__name__)`
- sets some default configuration `app.config.from_mapping()`
- allows for custom settings to be imported `app.config.from_pyfile()`
- also ensures that `app.instance.path` exists
- and creates a simple route - `@app.route` connecting URL `/hello` with 
  function that returns response

## Database connection
With this tutorial application the database used will be SQLite and this will
be accessed by `sqlite3` Python module. To start working with database the 1st
step is to make a connection. This connection is usually tied to the request
and closed once the the response is sent.
In `db.py` there are stored different functions that are used to operate on
SQLite database. To work with database there is a special object called `g` -
it stores data that might be accessed by multiple functions during the request.
Another special object `current_app` is used to point to the Flask app handling
the request. To connect to database the `sqlite3` has `connect()` function, it
has been configured with `DATABASE` configuration key (file can be created 
with database initialization). Another `sqlite3` function called `Row` is used
to return rows that behave like dicts. Dedicated function is also created to
close the connection to database (checking initialy if the connection exists).
The tutorial application database will store users and posts in separate 
tabels. The creation of DB can be sped up by using SQL schema (stored in 
`flaskr` directory). Required functions have been added to `db.py` - one 
function to run SQL schema building the database (directly in `flaskr`) and
the enable running from CLI (Command Line Interface). The initilizing and 
closing of database functions have to be registered with application. Separate
function has been created to enable it - `init_app(app)` in `db.py`. The new
function is then imported to app initialization function and invoked there.
The new command that can be run to initialize DB: `flask --app flaskr init-db`
This way a new `instance` directory is created with SQLite DB inside with 2
tables (posts and users) as per schema.

## Blueprints and Views
Flask app uses patterns to match the incoming request URL to the view that
should handle it. With `Blueprint` as a way to organize a group of related 
views and other code the tutorial app will have authentication and post 
functions implemented. The blueprint portion is acting as an intermediate 
step so that rather than registering views and other code directly with an 
app, they are registered with a blueprint and then blueprint is registered 
with the application.

```
 _____________         _____________             __________
|             |       |             |<--------->|__VIEW 1__|
|  FLASK APP  |<----->|  BLUEPRINT  |            __________            
|_____________|       |_____________|<--------->|__VIEW 2__|

```

The blueprint object has to know where it's defined, so `__name__` is passed
as the second argument. Blueprint is then imported and registered in app initialization script.
The first view that has been created is a register view. When user visits the
register URL (`/auth/register`) the view will return a form to fill out. In
`auth.py` there is only the code for page behavior/actions, specific page 
layout (`html`) is generated with templates. The function start with `@` 
decorator that assoicates the URL with function. Register page will have a 
space for users to put `username` and `password`. Once user submits the form,
`request.method` will be `POST` and the function will start validating the
input. A special `request.form` is used to map username and password in form of
key and value. The function checks if provided input is not empty and if that
is the case it proceeds to enter the new user into database. Function will try
to execute `INSERT` on databse by running an SQL query with `?` placeholders 
and tuple of input values provided to replace them. The database library will 
take care of escaping the values so that the app is not vulnerable to a SQL 
injection attack. For the password additional function is executed to hash it
before storing it in database. Lastly the `db.commit()` function is run to save
changes. If the `username` already exists an error is thrown and caught in 
`error` variable. Another function `flash()` is used to catch and store errors
that can be later shown to users. If user is successfuly registered app 
redirects using `url.for()` function to the login view based on username.
Instead of direct link the `redirect()` function is used - this allows for
easier change of URL without changing all the code that links to it.
