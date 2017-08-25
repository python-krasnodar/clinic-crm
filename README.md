# clinic-crm

[![Build Status](https://travis-ci.org/memclutter/clinic-crm.svg?branch=master)](https://travis-ci.org/memclutter/clinic-crm)

An example of a simple Django application. 

## Running

The launch of the application in the product environment is carried out by a couple of simple steps. 
Go to `deploys/production` dir and run `up.sh` script.

```sh
cd deploys/production
./up.sh
```

The `deploys/production` directory contains the `docker-compose.yml` and `Dockerfiles` for various services
(like a database), as well as the configuration for services.

After running `up.sh` in a couple of minutes application will be available at the address http://localhost.
Default admin user is `admin/password123`.

Use the `down.sh` command to stop the application and remove all docker containers.

## Testing

In the `deploys/testing` folder are all the files to run the test environment. There is also used docker and 
docker-compose.

Go to `deploys/testing` dir and run `up.sh` script.

```sh
cd deploys/testing
./up.sh
```

During start-up, you will see how the environment is going. After that regulat django tests will be launched. 

## Development

You can also start the project in development mode. This will allow you to run tests faster, and the webserver.

### 1. Virtualenv

First, initialize the virtual environment with Python3.

```sh
virtualenv -p python3 .venv
source .venv/bin/activate
```

The last command also activates this evnironment.

### 2. Install dependencies

All project dependencies are divided into *system packages* and *python packages*. 
Of the first need only PostgreSQL 9.6 or higher. 

All *python packages* are listed in the `requirements.txt` file and can be install by this command


```sh
pip install -r requirements.txt
```

### 3. Database

First, we create the role and the database. See the SQL script bellow to help create a role and a database. 

```sql
CREATE ROLE clinic_crm WITH SUPERUSER LOGIN ENCRYPTED PASSWORD 'clinic_crm';
CREATE DATABASE clinic_crm WITH OWNER clinic_crm;
CREATE DATABASE test_clinic_crm WITH OWNER clinic_crm;
```

To set this username/password and database name, the environment variable is used. For convenience, all 
environment variables are listed in the `.env.dist` file. Create a new `.env` file and copy everything from the 
`.env.dist` file. Change the environment variable `DATABASE_URL` to match your PostgreSQL database, for the case above


```
DATABASE_URL=postgres://clinic_crm:clinic_crm@localhost:5432/clinic_crm
```

The last thing you need to do is make our database ready, roll the migrations.

```sh
cd src
./manage.py migrate --no-input
```

### 4. Testing application

First we'll test the application

```sh
./manage.py test --no-input --keepdb
```

### 5. Fixtures (optional)

In order that it would be convenient to the application in the work we load a few fixtures.
 
- `src/front/fixtures/users.json`
- `src/clinic/fixtures/specialities.json`
- `src/clinic/fixtures/doctors.json`
- `src/timetables/fixtures/timetables.json`

We'll do it with this script

```sh
./manage.py loaddata front/fixtures/users.json
./manage.py loaddata clinic/fixtures/specialities.json
./manage.py loaddata clinic/fixtures/doctors.json
./manage.py loaddata timetables/fixtures/timetables.json
```

### 6. Development web-server

To start the development server, run

```sh
./manage.py runserver
```

Our application will be available at http://localhost:8000.
