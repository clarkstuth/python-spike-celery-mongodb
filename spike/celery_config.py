from celery import Celery

if __name__ == '__main__':
    print 'running celery_config as main method'


class CeleryConfig:
    CELERY_ENABLE_UTC = True
    CELERY_TIMEZONE = 'America/Chicago'
    CELERY_CREATE_MISSING_QUEUES = True
    CELERY_DEFAULT_QUEUE = 'load'
    CELERY_DEFAULT_EXCHANGE = 'load'
    CELERY_DEFAULT_ROUTING_KEY = 'load'
    BROKER = 'amqp://gest:gest@localhost:5672'


app = Celery()
app.config_from_object(CeleryConfig)


@app.task(serializer="json", name="load")
def load(message):
    print message
