Install
-------

### Both dev and prod

Install python dependencies:

    pip install -r music_portal/settings/requirements.txt

Create postgres datapbase:

    createdb spotify_parser

Create tables:

    ./manage.py migrate

Create an admin:

    ./manage.py createsuperuser

### Dev

Run the dev server:

    ./manage.py runserver
