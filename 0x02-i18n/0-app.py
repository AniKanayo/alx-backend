#!/usr/bin/env python3
"""Main Flask application file"""

from flask import Flask, render_template
from flask_babel import Babel
from config import Config  # Importing the Config class

app = Flask(__name__)
app.config.from_object(Config)  # Using Config class for configuration
babel = Babel(app)


@app.route('/')
def hello() -> str:
    """Renders a basic HTML template"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
