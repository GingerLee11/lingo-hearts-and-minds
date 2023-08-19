from flask import Flask, request
from config import Config
from flask_babel import Babel


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

from myapp import routes

def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

babel.init_app(app, locale_selector=get_locale)




