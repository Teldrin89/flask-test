from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    '''
    index view function with list of posts
    '''
    db = get_db() # get database
    # read posts from database with set of parameters
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ODER BY created DESC'
    ).fetchall()

    return render_template('blog/index.html', posts=posts)
