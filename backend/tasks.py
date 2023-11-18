from __future__ import absolute_import, unicode_literals

from celery import shared_task
import json
import requests


@shared_task
def generate_response(question: json):
    request_url = "http://localhost:11434/api/generate"
    response = requests.post(request_url, json=question)
    print(response)
