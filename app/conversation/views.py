from flask import request, jsonify, current_app

from . import lm


@lm.route("/message", methods=["POST"])
def message():
    """
    Called when client sends message.
    Generates and sends an answer to the original input message.
    """
    question = request.form.get("question")
    print("Received question:", question)

    convo = current_app.config["CONVERSATION"]
    next_speaker, answer = convo.next_utterance(question)

    print("Generated answer:", answer)

    classifier = current_app.config["SENTIMENT_CLASSIFIER"]
    sentiment = classifier.classify(answer)

    return jsonify(next_speaker=next_speaker.capitalize(),
                   answer=answer,
                   sentiment=sentiment["labels"][0])
