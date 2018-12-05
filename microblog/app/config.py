app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'