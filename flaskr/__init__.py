''' 
init file for flask app - name indicates dir should be treated as package 
'''

import os
from flask import Flask

def create_app(test_config=None):
    '''create and configure the app'''
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABSE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello Flask!'

    # testing landing page route - '/'
    @app.route('/')
    def defult_page():
        return 'This is a landing page test'

    return app
