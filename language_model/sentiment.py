"""
This modules provides a text classification pipeline
for sentiment analysis.
"""

from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline


def load_sentiment_classifier(model="joeddav/xlm-roberta-large-xnli"):
    classifier = pipeline("zero-shot-classification",
                          model=model)
    return classifier


def classify_sentiment(sequence,
                       classifier,
                       candidate_labels=("wütend", "empört", "ängstlich", "glücklich", "traurig", "schockiert"),
                       hypothesis="Dieser Text ist {}."):
    """
    Classifies a given string w.r.t. the defined candidate labels inserted into the hypothesis.

    @param sequence: A natural language sample (string) to be classified
    @param candidate_labels: The potential labels that should be evaluated
    @param hypothesis: A hypothesis with a placeholder for each candidate label
    @return: An estimation dictionary with the candidate labels and respective probability estimates.
    The scores sum to 1.0 and labels and scores are sorted in descending order.
    """
    sentiments = classifier(sequence, candidate_labels, hypothesis)
    estimation = {
        "labels": sentiments["labels"],
        "scores": sentiments["scores"],
        "sequence": sentiments["sequence"]
    }
    return estimation


def test_sequence(classifier):
    """
    Allows the user to enter a test sequence and prints sentiment estimations
    for different candidate labels.
    Repeats until user enters "exit".
    """
    def print_test(sequence, classifier, labels):
        """
        Test utility that runs classifier and prints the results.
        """
        estimation = classify_sentiment(sequence, classifier, labels)

        print("Sequence: " + estimation["sequence"] + "\n")
        for label, score in zip(estimation["labels"], estimation["scores"]):
            print("Label: " + label)
            print("Score: " + str(round(score, 2)) + "\n")

    # Lists of candidate labels for which the classifier shall be tested.
    label_options = [
        ["wütend", "empört", "ängstlich", "glücklich", "traurig", "schockiert"],
        ["wütend", "ängstlich", "glücklich", "traurig"]
    ]

    while True:
        sequence = input("Please enter a sequence to test:  ")
        if sequence == "exit":
            return

        for labels in label_options:
            print_test(sequence, classifier, labels)


def main():
    sentiment_classifier = load_sentiment_classifier()
    test_sequence(sentiment_classifier)


if __name__ == "__main__":
    main()
