from __future__ import absolute_import, unicode_literals

from set_selery import app
from celery import shared_task
import json
import requests


@app.task
def generate_response(msg: str, *args, **kwargs) -> json:
    request_url = "http://localhost:11434/api/generate"
    response = requests.post(request_url, json=msg)
    print(response)
    print(args)
    print(kwargs)
    print(msg)
    return response
