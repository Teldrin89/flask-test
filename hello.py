''' example of flask minimalistic app '''

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    '''
    Simple flask function
    '''
    return 'Hello Flask!'
