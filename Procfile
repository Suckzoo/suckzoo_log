web: newrelic-admin run-program gunicorn --pythonpath="$PWD/suckzoo_log" wsgi:application
worker: python suckzoo_log/manage.py rqworker default