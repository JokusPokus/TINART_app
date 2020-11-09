from flask import Flask, render_template, request, jsonify, session
from flask_session import Session

from language_model.inference import TalkshowGuests
from language_model.sentiment import SentimentClassifier
from language_model.conversation import Conversation


app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Load language models
guests = TalkshowGuests(politicians=["lindner", "wagenknecht"])

# Load sentiment classifier
classifier = SentimentClassifier()


@app.route("/")
def index():
    session["conversation"] = Conversation(guests)
    return render_template("index.html")


@app.route("/message", methods=["POST"])
def message():
    """
    Called when client sends message.
    Generates and sends an answer to the original input message.
    """
    question = request.form.get("question")
    print("Received question:", question)

    next_speaker, answer = session["conversation"].next_utterance(question)
    print("Generated answer:", answer)

    sentiment = classifier.classify(answer)

    return jsonify(next_speaker=next_speaker.capitalize(),
                   answer=answer,
                   sentiment=sentiment)


if __name__ == "__main__":
    app.run()
