# start backend
gunicorn --bind localhost:5000 wsgi:app --reload
