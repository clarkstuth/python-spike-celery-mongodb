from celery_config import load

load.delay({"data": "value", "subvalue": {"something": "else"}})
