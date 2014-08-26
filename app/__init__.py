from flask import Flask
from flask.ext.assets import Environment, Bundle
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True, static_url_path='/static')
app.config.from_object('config')
try:
    # Configuration from instance folder
    app.config.from_pyfile('config.py')
except EnvironmentError:
    pass

assets = Environment(app)
scss = Bundle('sass/normalize.scss', 'sass/colors.scss', 'sass/main.scss',
    filters='pyscss cssmin', output='gen/all.css')
js = Bundle('js/jquery-1.10.2.min.js', 'js/modernizr-2.6.2.min.js', 'js/plugins.js',
    'js/main.js',
    filters='jsmin', output='gen/packed.js')
assets.register('scss_all', scss)
assets.register('js_all', js)

db = SQLAlchemy(app)

from app import views, models
