# gunicorn_config.py

command = 'gunicorn'
pythonpath = '/app/django-staff'
bind = '0.0.0.0:8000'
workers = 4

# Additional parameters
timeout = 120  # Workers silent for more than this many seconds are killed and restarted.
graceful_timeout = 120  # Timeout for graceful workers restart.
keepalive = 5  # The number of seconds to wait for the next request on a Keep-Alive HTTP connection.
errorlog = '-'
accesslog = '-'
loglevel = 'info'
preload_app = True  # Load application code before the worker processes are forked.