#!/usr/bin/env sh

# wait for postgresql up and running
sleep 10

# apply migrate
python manage.py migrate --no-input

# load fixtures
python manage.py loaddata front/fixtures/users.json
python manage.py loaddata clinic/fixtures/specialities.json
python manage.py loaddata clinic/fixtures/doctors.json
python manage.py loaddata timetables/fixtures/timetables.json

# collect static files
python manage.py collectstatic --no-input

# start application
uwsgi --ini uwsgi.ini
