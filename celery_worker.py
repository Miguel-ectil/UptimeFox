from celery import Celery
from app.config import Config

celery = Celery('uptimefox',
                broker=Config.CELERY_BROKER_URL,
                backend=Config.CELERY_RESULT_BACKEND)

celery.conf.imports = ['app.tasks.monitor_tasks']
