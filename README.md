##  API Django project

--------
This web application creates a API blog, where users can create post and comments.

--------
**How to start project**
* install all from requirements.txt
* for start project write in terminal:
```
python manage.py runserver
```
* for creating 10 users write in terminal:
```
./manage.py create_users
```
* for create 500 posts
```
./manage.py create_post
```
* for create 2000 comments
```
./manage.py create_comment
```
* for loading fixtures:
  * clear table:
```
./manage.py flush
```
  * load fixtures
```
./manage.py loaddata fixtures/db.json
```
* for check apps:
```
http://127.0.0.1:8000/
```

* Quit the server with CONTROL-C.
--------
Project checked by flake8