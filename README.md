## Crypto Backend
Responsible for processing api requests from the React frontend as well as requests from the phone app.

### Project properties
1. Python 3.9.6
2. Flask, gunicon
3. SqlAlchemy, Marshmallow

### Requirements
1. mysql
2. pyenv (python version management) OR your own installation


### Setup (Mac / Linux)
1. Create a virtual environment & activate it
```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

2. Install required packages
```bash
$ pip install -r requirements.txt
$ pip install marshmallow_enum
```

3. Create a .env file in the root directory of the project using .env.default as a template
```bash
$ cp .env.default .env
```

4. Start up the mysql database

5. Download the cryptolib package and store it in the root directory of the project. Bug fixes can be made directly to this package and then pushed to the repository. This folder itself should never be committed to this projects repo however, only the cryptolibrary repo.
```bash
$ git clone https://github.com/everdeep/crypto-library.git
```

6. Run the server
```bash
$ python3 wsgi.py # for testing
$ gunicorn --bind
```


