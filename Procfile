release: python manage.py migrate
web: gunicorn app.wsgi
worker: python manage.py process_tasks