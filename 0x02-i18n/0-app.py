#!/usr/bin/env python3
"""
app's module
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """ A config class for our app.
    This configures the languages that the app supports
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCAL = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/')
def index():
    """ The home page for the website
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    """Run the app
    """
    app.run()
