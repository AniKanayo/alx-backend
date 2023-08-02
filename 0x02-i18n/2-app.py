#!/usr/bin/env python3
"""Main Flask application file"""

from flask import Flask, render_template, request
from flask_babel import Babel, localeselector

class Config(object):
    """Class for Flask application configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)  # Using Config class for configuration
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """ Determine the best match language for user """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello() -> str:
    """Renders a basic HTML template"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
