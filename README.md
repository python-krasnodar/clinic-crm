# clinic-crm

[![Build Status](https://travis-ci.org/memclutter/clinic-crm.svg?branch=master)](https://travis-ci.org/memclutter/clinic-crm)

An example of a simple Django application

## Testing
Go to `deploys/testing` dir.

```sh
cd deploys/testing
./up.sh
```

## Running

Go to `deploys/production` dir.

```sh
cd deploys/production
./up.sh
```

Wait a few minutes and open http://localhost:80.

## Manual

Init virtualenv with Python3

```sh
virtualenv -p python3 .venv
source .venv/bin/activate
```

Install dependencies

```sh
pip install -r requirements.txt
```

Create PostgreSQL database 

```sql
CREATE ROLE clinic_crm WITH SUPERUSER LOGIN ENCRYPTED PASSWORD 'clinic_crm';
CREATE DATABASE clinic_crm WITH OWNER clinic_crm;
CREATE DATABASE test_clinic_crm WITH OWNER clinic_crm;
```

Create dotenv file and edit.

```sh
cp .env.dist .env
```

Apply migrations

```sh
cd src
./manage.py migrate --no-input
```

Run tests

```sh
./manage.py test --no-input --keepdb
```

Run development webserver

```sh
./manage.py runserver
```
