from flask import Flask, render_template, request, jsonify

from language_model.inference import TalkshowGuests
from language_model.sentiment import SentimentClassifier


app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


# Load language models
chatbots = TalkshowGuests(politicians=["lindner", "wagenknecht"])


# Load sentiment classifier
classifier = SentimentClassifier()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/message", methods=["POST"])
def message():
    """
    Called when client sends message.
    Generates and sends an answer to the original input message.
    """
    question = request.form.get("question")
    print("Received question:", question)

    answer = chatbots["lindner"].generate_response(question)
    print("Generated answer:", answer)

    sentiment = classifier.classify(answer)

    return jsonify(answer=answer, sentiment=sentiment)


if __name__ == "__main__":
    app.run()
