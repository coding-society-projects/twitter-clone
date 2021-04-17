# Twitter clone experiment

An exercise on Django. Trying to build a simplified clone of Twitter.

### Instructions

1. Clone or download the project 
1. Migrate to create db tables: ```python manage.py migrate```
1. Create the administrator's account: ```python manage.py createsuperuser```

**Warning**: The SECRET_KEY value in settings.py is exposed here and should be replaced in case you want to use
this project in a production server.


### History

**v.1**: Created model for Tweet and added relationship to the user, and a 
page displaying all tweets in reverse order.


