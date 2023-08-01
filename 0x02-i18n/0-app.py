#!/usr/bin/env python3
"""A basic Flask application.
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index() -> str:
    """The main route which will display 'Hello, World'.
    Returns:
        str: The HTML template to display.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
