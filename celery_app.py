from celery import Celery
from .config import settings

celery_app = Celery('demo_app', broker=settings.RABBITMQ_URL)
# You may configure result backend if needed
# celery_app.conf.result_backend = 'rpc://'

# optional: task serializer
celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)

# ensure tasks auto-discovery if package structure grows
# celery will import tasks by direct import in this repo
