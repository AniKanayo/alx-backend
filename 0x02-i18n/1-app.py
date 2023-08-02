#!/usr/bin/env python3
"""
1. Basic Babel Setup
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """Configuration class for available
       languages and default settings.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

babel = Babel(app)


@app.route('/')
def index():
    """Route handler for the index page."""
    return render_template(
        'index.html', 
        title="Welcome to Holberton", 
        header="Hello world"
    )


if __name__ == '__main__':
    app.run()
