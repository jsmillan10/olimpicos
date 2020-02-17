release: python olimpicos/manage.py makemigrations tokio
release: python olimpicos/manage.py migrate tokio
web: gunicorn --chdir olimpicos olimpicos.wsgi — log-file -
