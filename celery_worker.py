from app import create_app
from app.extensions import celery
from app.config import Config
from celery.schedules import crontab
from datetime import timedelta

def make_celery(app):
    celery.conf.broker_url = Config.CELERY_BROKER_URL
    celery.conf.result_backend = Config.CELERY_RESULT_BACKEND
    celery.conf.imports = ['app.tasks.monitor_tasks']

    # Configuração do Celery Beat para executar a tarefa a cada 5 minutos
    celery.conf.beat_schedule = {
        'verificar-sites-cada-5-minutos': {
            'task': 'app.tasks.monitor_tasks.verificar_sites',
            'schedule': timedelta(seconds=30),  # a cada 5 minutos
        },
    }
    celery.conf.timezone = 'UTC'  # Ajuste para seu fuso horário, se quiser

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

flask_app = create_app()
celery = make_celery(flask_app)
flask_app.extensions['celery'] = celery

if __name__ == '__main__':
    celery.worker_main()
