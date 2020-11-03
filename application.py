from flask import Flask, render_template, request, jsonify

from language_model.inference import load_model, generate_response
from language_model.sentiment import SentimentClassifier


app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


# MODEL LOADING
POLITICIAN = "lindner"
PATH_TEMPLATE = ".\\language_model\\gpt2-{}"
model_path = PATH_TEMPLATE.format(POLITICIAN)


# Load fine-tuned GPT-2 language model
tokenizer, model = load_model(model_path=model_path, fine_tuned=True)


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

    answer = generate_response(question, model, tokenizer)
    print("Generated answer:", answer)

    sentiment = classifier.classify(answer)

    return jsonify(answer=answer, sentiment=sentiment)


if __name__ == "__main__":
    app.run()
