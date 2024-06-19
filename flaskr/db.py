'''
SQLite database functions for actions performed on database
'''

import sqlite3
import click
from flask import current_app, g

def get_db():
    '''
    function to establish the connection to dabase
    '''
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.gb.row_factory = sqlite3.Row

        return g.bd

    return None

def close_db(e=None):
    '''
    function to close database connection
    TODO: "e" param could be used in later development
    '''
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    '''
    function to initialize database
    '''
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
def init_db_command():
    '''
    clear the existing data and create new tables
    '''
    init_db()
    click.echo('Initialized the database')

def init_app(app):
    '''
    registering init and close db functions with the app
    '''
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
