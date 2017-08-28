from celery import Celery
from pymongo import MongoClient

if __name__ == '__main__':
    print 'running celery_config as main method'


class _CeleryConfig:
    CELERY_ENABLE_UTC = True
    CELERY_TIMEZONE = 'America/Chicago'
    CELERY_CREATE_MISSING_QUEUES = True
    CELERY_DEFAULT_QUEUE = 'load'
    CELERY_DEFAULT_EXCHANGE = 'load'
    CELERY_DEFAULT_ROUTING_KEY = 'load'
    BROKER = 'amqp://gest:gest@localhost:5672'


load_app = Celery()
load_app.config_from_object(_CeleryConfig)

_mongo_client = MongoClient()
_collection = _mongo_client.test_db.test_collection


@load_app.task(serializer="json", name="load")
def load(message):
    _collection.insert_one(message)
    print "{} written to mongo".format(message)
