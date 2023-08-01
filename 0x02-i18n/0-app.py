#!/usr/bin/env python3
"""
0. Basic Flask App
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index() -> str:
    """Route handler for the index page."""
    return render_template('index.html', title="Welcome to Holberton",
                            header="Hello world")


if __name__ == '__main__':
    app.run()
