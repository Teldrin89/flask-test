# FLASK TUTORIAL
This repository holds codebase of flask application tutorial.
The next sections describe consecutive parts of test flas app.
Reference of tutorial web page: 
[Flask](https://flask.palletsprojects.com/en/3.0.x/tutorial/)

## Initial app setup
Simple Flask application can be made with single python script. Importing
Flask library and starting the app as Flask class. The more "complete" app
may have a tree looking similar to this one
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