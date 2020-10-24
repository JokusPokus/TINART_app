from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer

from flask import Flask, render_template, request

import random
import os

from language_model.inference import load_model, generate_seq


app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

# Load GPT-2 language model
path_name = ".\language_model\gpt"
model_wrapper = load_model(path_name)

N_UTTERANCES = 3


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/message")
def message():
    """
    Called when client sends message.
    Generates and immediately sends three sentences as
    an answer to the original input message.
    """
    if request.environ.get("wsgi.websocket"):
        ws = request.environ["wsgi.websocket"]
        while True:
            prefix = ws.receive()
            for i in range(N_UTTERANCES):
                answer = generate_seq(model_wrapper, prefix)
                answer = answer[len(prefix)+1:]
                ws.send(answer)

                prefix += " " + answer
    return


if __name__ == "__main__":
    http_server = WSGIServer(("0.0.0.0", 5000), app, handler_class=WebSocketHandler)
    http_server.serve_forever()
