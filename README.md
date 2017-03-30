Install
-------

### Both dev and prod

Install python dependencies:

    python3 -m venv env
    source env/bin/activate

    pip install -r music_portal/settings/requirements.txt

Create postgres datapbase:

    createdb music_portal

Create tables:

    ./manage.py migrate

Create an admin:

    ./manage.py createsuperuser

### Dev

Run the dev server:

    ./manage.py runserver