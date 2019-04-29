release: python manage.py migrate
web: daphne api.asgi:application -p $PORT --bind 0.0.0.0