import os

from celery import Celery

redis_host = os.getenv("NA_REDIS_HOST", "localhost")
redis_port = os.getenv("NA_REDIS_PORT", "6379")
redis_pass = os.getenv("NA_REDIS_PASS", "")


celery = Celery(__name__)
celery.conf.broker_url = f"redis://:{redis_pass}@{redis_host}:{redis_port}/0"
celery.conf.result_backend = f"redis://:{redis_pass}@{redis_host}:{redis_port}/0"
celery.conf.broker_transport_options = {
    "health_check_interval": 5,
    "socket_timeout": 60,
    "socket_connect_timeout": 60,
}
celery.conf.update(result_persistent=True, redis_socket_keepalive=True)

