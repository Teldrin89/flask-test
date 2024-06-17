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
    '''
    db = g.pop('db', None)

    if db is not None:
        db.close()
