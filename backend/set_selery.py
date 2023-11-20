from __future__ import absolute_import, unicode_literals

from celery import Celery


app = Celery(
    "proj",
    broker="amqp://admin:CT2gNABH8eJ9yVh@rabbit:5672",
    backend="rpc://",
    include=["proj.tasks"],
)

if __name__ == "__main__":
    app.start()
