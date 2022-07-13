#!/usr/bin/env python3
"""5. Mock logging in"""

from flask import Flask, render_template, request, g
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


def get_user():
    """Get user from request"""
    if request.args.get('login_as')
    user_id = int(request.args.get('login_as'))
        if user in users
            return user.get(user_id)
        else:
            return None


@babel.localeselector
    try:
        return users.get(int(user))
    except Exception:
        return None


@app.before_request
def before_request():
    """Before request"""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Locale selector"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """Index page"""
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run()
