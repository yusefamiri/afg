# fxrate

## ToDo:

- https://simpleit.rocks/python/django/generating-slugs-automatically-in-django-easy-solid-approaches/

## ToRead:

- https://realpython.com/django-redirects/#django-redirects-a-super-simple-example

## Create fixture out of database data 

Load data from database into a fixture:
```
python3 manage.py dumpdata app.model --indent 5 > name.json
```

## Load test data into the database

Clear old data from databse:
```
python3 manage.py sqlflush | python3 manage.py dbshell
```

Load fixtures for user table:
```
python3 manage.py loaddata fixtures/users.json
```

Make sure you have loaded the user fixtures properly than, load fixtures for post table:
```
python3 manage.py loaddata blog/fixtures/posts.json
```
You will now have test posts in your database.

Insert 4 images into the media folder named like:
- fixture1.jpg 
- fixture2.jpg 
- fixture3.jpg 
- fixture4.jpg 

For currency exchange table do the following: 
```
python3 manage.py loaddata exchange/fixtures/currency.json
python3 manage.py loaddata exchange/fixtures/exchange-rate.json
```