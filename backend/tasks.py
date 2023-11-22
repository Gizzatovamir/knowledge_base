from __future__ import absolute_import, unicode_literals

from celery import shared_task
import json
import requests
import os
from celery import Celery
from typing import Dict


app = Celery(
    "tasks",
    broker=os.getenv("CELERY_BROKER_URL"),
)


@shared_task
def generate_response(*args, **kwargs) -> json:
    request_url = "http://localhost:11434/api/generate"
    print(args)
    print(kwargs)
    print(args[0])
    response = requests.post(request_url, data=args[0])
    print(response)
    res: Dict[int, any] = dict()
    for index, line in enumerate(response):
        res.update({index: line})
    return res
