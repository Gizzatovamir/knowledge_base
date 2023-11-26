from __future__ import absolute_import, unicode_literals

from celery import shared_task
import json
import requests
import os
from celery import Celery
from typing import Dict
from flask import jsonify


app = Celery(
    "tasks",
    broker=os.getenv("CELERY_BROKER_URL"),
)


@shared_task
def generate_response(msg) -> str:
    request_url = "http://127.0.0.1:11434/api/generate"
    llama_response = requests.post(request_url, data=msg)
    print(f"RESPONSE - {llama_response}")
    res: Dict[int, any] = dict()
    for index, line in enumerate(llama_response):
        res.update({index: line})
    return llama_response
