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
`flaskr` directory).