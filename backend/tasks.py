from __future__ import absolute_import, unicode_literals

from set_selery import app
from celery import shared_task
import json
import requests


@app.task
def generate_response(*args, **kwargs) -> json:
    request_url = "http://localhost:11434/api/generate"
    print(args)
    print(kwargs)
    print(args[0])
    response = requests.get(request_url, json=args[0])
    print(response)
    return response
