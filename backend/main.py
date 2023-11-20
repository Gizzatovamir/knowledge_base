from flask import Flask, jsonify, render_template
from set_selery import app as celery_app
from tasks import generate_response
import json

app = Flask(__name__)
app.config["CELERY_BROKER_URL"] = "amqp://admin:CT2gNABH8eJ9yVh@rabbit:5672"
app.config["CELERY_RESULT_BACKEND"] = "amqp://admin:CT2gNABH8eJ9yVh@rabbit:5672"


def on_raw_message(body):
    print(body)


@app.route("/")
def main():
    msg = {"model": "llama2", "prompt": "Why is the sky blue?"}
    task = generate_response.delay(msg)
    result_msg = task.get(on_message=on_raw_message, propagate=False)
    response = {
        "state": task.state,
        "msg": result_msg,
    }
    print(response)
    return f"{response}"


@app.route("/result/")
def result():
    pass


if __name__ == "__main__":
    app.debug = True
    app.run()
    celery_app.start()
