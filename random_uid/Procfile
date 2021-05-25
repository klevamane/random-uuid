release: python manage.py migrate
web: gunicorn random_uid.wsgi --log-file - --log-level debug
