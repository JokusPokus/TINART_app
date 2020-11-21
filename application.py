from flask import Flask, render_template, request, jsonify

from language_model.inference import TalkshowGuests
from language_model.sentiment import SentimentClassifier
from language_model.conversation import Conversation


app = Flask(__name__)


# Load language models
guests = TalkshowGuests(politicians=["lindner", "wagenknecht"])

# Load sentiment classifier
classifier = SentimentClassifier()

convo = Conversation(guests)


@app.route("/")
def index():
    return render_template("landing.html")


@app.route("/simulator")
def start_simulator():
    return render_template("app.html")


@app.route("/message", methods=["POST"])
def message():
    """
    Called when client sends message.
    Generates and sends an answer to the original input message.
    """
    question = request.form.get("question")
    print("Received question:", question)

    next_speaker, answer = convo.next_utterance(question)

    print("Generated answer:", answer)

    sentiment = classifier.classify(answer)

    return jsonify(next_speaker=next_speaker.capitalize(),
                   answer=answer,
                   sentiment=sentiment["labels"][0])


if __name__ == "__main__":
    app.run()
