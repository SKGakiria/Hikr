# Hikr


## Installation

```sh
$ git clone https://github.com/evanceodoyo/Hikr.git
$ python3 -m venv venv
$ source venv/bin/activate
$ cd hikr
$ pip install -r requirements.txt
```

Create a new PostgreSQL database

```sh
 $ psql postgres
 $ CREATE DATABASE databasename$
 $ \connect databasename
```

Set the environment variables and make migrations

```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

Create a superuser

```sh
$ python manage.py createsuperuser
```

Start the development server

```sh
$ python manage.py runserver
```

## Populate the database with sample data
- To populate the database with sample data, ensure you are in the folder `hikr` (The folder with `manage.py`). If you have images you want to use for the events/groups, ensure they are in the same directory in folders named `event_images` and `group_images` respectively. You can find sample events and groups images in [this folder](https://drive.google.com/drive/folders/1e7oFwf6U5u1plsp12ZuGyTBxGwjVqaV3?usp=sharing).

- Once in the folder, run the script as follows:  
```sh
$ ./populated_db.py
```
or 
```sh
$ python3 populated_db.py
```