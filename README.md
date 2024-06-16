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