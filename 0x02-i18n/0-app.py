#!/usr/bin/env python3
"""Module for Flask application"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world() -> str:
    """Returns index.html when route '/' is requested"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
