#!/usr/bin/env python3
"""
Flask Application to display translated content based on the locale parameter.
"""

from flask import Flask, request

app = Flask(__name__)

# Define the supported locales
SUPPORTED_LOCALES = ['fr', 'en']

# Default locale (fallback when the locale parameter is not provided)
DEFAULT_LOCALE = 'en'


def get_locale() -> str:
    """
    Get the locale from the request args if present and supported,
    otherwise return the default locale.

    Returns:
        str: The selected locale.
    """
    locale = request.args.get('locale')

    if locale and locale in SUPPORTED_LOCALES:
        return locale

    return DEFAULT_LOCALE


@app.route('/')
def hello_world() -> str:
    """
    Display translated content based on the selected locale.

    Returns:
        str: Translated content.
    """
    locale = get_locale()

    translations = {
        'fr': 'Bonjour le monde!',
        'en': 'Hello, world!',
    }

    translation = translations.get(locale, translations[DEFAULT_LOCALE])
    return f'<h1>{translation}</h1>'


if __name__ == '__main__':
    app.run(debug=True)
