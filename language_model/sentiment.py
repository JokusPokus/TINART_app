from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

classifier = pipeline("zero-shot-classification",
                      model="joeddav/xlm-roberta-large-xnli")

sequence_to_classify = "Ich hatte gehofft, wir könnten vernünftig miteinander sprechen. Schade."

candidate_labels = ["glücklich", "traurig"]

hypothesis = "Dieser Text ist {}."

sentiments = classifier(sequence_to_classify, candidate_labels, hypothesis)

best_guess = sentiments["labels"][0]
probability = sentiments["scores"][0]

message = f"Dieser Text ist mit {round(probability * 100, 1)} % Wahrscheinlichkeit {best_guess}."
print(message)
