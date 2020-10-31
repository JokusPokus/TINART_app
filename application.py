from flask import Flask, render_template, request, jsonify

from language_model.inference_hf import load_model, generate_response


app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

POLITICIAN = "lindner"
N_UTTERANCES = 3

MODEL_PATH = f".\\language_model\\gpt2-{POLITICIAN}"

# Load GPT-2 language model
tokenizer, model = load_model(model_path=MODEL_PATH)


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
    print(question)
    answer = generate_response(question, model, tokenizer)
    print(answer)
    return jsonify(answer=answer)


app.run()
