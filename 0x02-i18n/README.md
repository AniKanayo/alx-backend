# i18n Flask App

![Project Logo](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/1/91e1c50322b2428428f9.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230801%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230801T211613Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5a4a4624e2f02ba104ebdae02729962cd1bfbf299c8b746f2b5eb51aed042e29)

This project is a Flask app that demonstrates internationalization (i18n) capabilities.
It allows users to view the website content in different languages and displays
the current time according to their preferred timezone.

## Table of Contents
- [Introduction](#introduction)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Tasks](#tasks)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

Welcome to the i18n Flask app! This project showcases how to create a multilingual website
using Flask-Babel and how to localize timestamps based on user preferences.

## Learning Objectives

By working on this project, you will:

- Learn how to parametrize Flask templates to display different languages.
- Learn how to infer the correct locale based on URL parameters, user settings, or request headers.
- Learn how to localize timestamps based on the user's preferred timezone.

## Requirements

To run this project, you need the following:

- Ubuntu 18.04 LTS
- Python 3.7
- [Flask-Babel](https://pypi.org/project/Flask-Babel/)
- [pytz](https://pypi.org/project/pytz/)

## Installation

1. Clone the repository from GitHub:

```
git clone https://github.com/username/i18n-flask-app.git
```

2. Change to the project directory:

```
cd i18n-flask-app
```

3. Install the required packages:

```
pip3 install -r requirements.txt
```

## Usage

1. Run the Flask app:

```
python3 app.py
```

2. Open your web browser and visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to access the website.

## Tasks

This project consists of several tasks, each building upon the previous one. The tasks are
located in separate files, and you can navigate through them to understand and implement the required functionality.

- **Task 0:** Basic Flask app
- **Task 1:** Basic Babel setup
- **Task 2:** Get locale from request
- **Task 3:** Parametrize templates
- **Task 4:** Force locale with URL parameter
- **Task 5:** Mock logging in
- **Task 6:** Use user locale
- **Task 7:** Infer appropriate time zone
- **Task 8 (Advanced):** Display the current time

Please follow the instructions in each task's file to complete the implementation.

## Contributing

Michael Anayo welcomes contributions to this project. If you find any issues or have suggestions
for improvements, feel free to open an issue or submit a pull request.
