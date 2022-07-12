#!/usr/bin/env python3
"""5. Mock logging in"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)
""" instantiate the Babel object """
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
# mock database user table


class Config(object):
    """ config class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
""" Use that class as config for Flask app """


@babel.localeselector
def get_locale():
    """ to determine the best match with our supported languages """
    locallang = request.args.get('locale')
    supported_languages = app.config['LANGUAGES']
    if locallang in supported_languages:
        return locallang
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def root():
    """ basic Flask app """
    return render_template("5-index.html")


def get_user():
    """ get user from database """
    user_id = request.args.get('user_id')
    if user_id:
        return users[int(user_id)]
    else:
        return None


@app.before_request
def before_request():
    """ before request """
    user = get_user()
    if user:
        if user['locale']:
            babel.locale = user['locale']
        if user['timezone']:
            babel.timezone = user['timezone']


if __name__ == "__main__":
    app.run()
