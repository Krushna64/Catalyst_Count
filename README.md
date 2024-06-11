# Catalyst Count

## Setup

Clone the repository:

```sh
$ git clone https://github.com/Krushna64/Catalyst_Count.git
$ cd Catalyst_Count
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv venv
$ source venv/bin/activate
```

Install dependencies:

```sh
(venv)$ pip install -r requirements.txt
```

Run migrations:
```sh
(venv)$ python manage.py makemigrations api
(venv)$ python manage.py migrate
```

Create a superuser (for admin access):
```
(venv)$ python manage.py createsuperuser
```

Run the server:
```
(venv)$ python manage.py runserver
```

And navigate to `http://127.0.0.1:8000/`.

## Tests

To run the tests, `cd` into the directory where `manage.py` is:
```sh
(venv)$ python manage.py test api
```