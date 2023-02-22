# tree-menu


The application provides tools for building nested menus.

Endpoints:

| Endpoint | Method | Description |
|----------|---------|---------|
| / | GET |  List of available menus. |
| /menus/{id}/components/{id} | GET | Draws menu tree. All parent components and child components of the requested component will be presented. |


## Links
This project was built using these tools:
| Tool | Description |
|----------|---------|
| [Django ](https://www.djangoproject.com/) |  "A high-level Python web framework" |
| [poetry](https://python-poetry.org/) |  "Python dependency management and packaging made easy" |


## Installation
**Copy a project**

```
$ git clone git@github.com:Dddarknight/tree-menu.git
$ cd tree-menu
```

**Set up environment variables**
```
$ touch .env

You have to write into .env file SECRET_KEY for Django app. See .env.example.
To get SECRET_KEY for Django app:
$ python manage.py shell
>>> from django.core.management.utils import get_random_secret_key
>>> get_random_secret_key()

Then add new SECRET_KEY to .env file
```

**Set up the environment**
```
$ pip install poetry
$ make install
```

**Dealing with migrations**
```
$ make migrate
```

**Launch**
```
$ make run
```

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)