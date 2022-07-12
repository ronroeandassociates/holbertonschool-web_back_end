#!/usr/bin/env python3
"""7. Infer appropriate time zone"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import timezone, UnknownTimeZoneError

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
    user_id = request.args.get('login_as')
    try:
        return users.get(int(user_id))
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
    return render_template('7-index.html')


@babel.timezoneselector
def get_timezone():
    """Timezone selector"""
    timezone = request.args.get('timezone')
    if timezone:
        try:
            timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            pass
    user = g.user
    if user:
        try:
            timezone(timezone)
            return user['timezone']
        except UnknownTimeZoneError:
            pass
    return request.args.get('timezone')


if __name__ == "__main__":
    app.run()
