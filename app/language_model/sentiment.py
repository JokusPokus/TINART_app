"""
This modules provides a text classification pipeline
for sentiment analysis.
"""

from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline, Pipeline
from typing import Dict, List


class SentimentClassifier:
    """A sentiment classifier loads a masked language model and accepts candidate labels
    and a hypothesis about some piece of text.

    It can then estimate which of the candidate labels completes the hypothesis w.r.t. to a
    given piece of text. It also returns the according confidence scores between 0 and 1.
    """

    def __init__(self,
                 model="joeddav/xlm-roberta-large-xnli",
                 candidate_labels=("wütend", "ängstlich", "glücklich", "traurig", "schockiert"),
                 hypothesis="Dieser Text ist {}."):
        self.model = model
        self.candidate_labels = candidate_labels
        self.hypothesis = hypothesis

        print("\nLoading Sentiment Classifier...")
        self.classifier = pipeline("zero-shot-classification", model=self.model)
        print("Done.\n")

    def classify(self, sequence: str, labels: List[str] = None) -> Dict:
        """
        Classifies a given string w.r.t. the instance's candidate labels inserted into the hypothesis.

        @param sequence: A natural language sample (string) to be classified

        @param labels: Candidate labels that are evaluated w.r.t. to the hypothesis

        @return: An estimate dictionary with the candidate labels and respective probability estimates.
        The scores sum to 1.0 and labels and scores are sorted in descending order.
        """
        if not labels:
            labels = self.candidate_labels

        sentiments = self.classifier(sequence, labels, self.hypothesis)
        estimate = {
            "labels": sentiments["labels"],
            "scores": sentiments["scores"],
            "sequence": sentiments["sequence"]
        }
        print("Estimated sentiment: {} ({} %)".format(
            estimate['labels'][0],
            round(estimate['scores'][0] * 100)
        ))
        return estimate

    def _print_test(self, sequence, labels):
        """
        Test utility that runs classifier and prints the results.
        """
        estimation = self.classify(sequence, labels)

        print("Sequence: " + estimation["sequence"] + "\n")
        for label, score in zip(estimation["labels"], estimation["scores"]):
            print("Label: " + label)
            print("Score: " + str(round(score, 2)) + "\n")

    def prompt_tests(self):
        """
        Allows the user to enter a test sequence and prints sentiment estimations
        for different candidate labels.
        Repeats until user enters "exit".
        """
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
                self._print_test(sequence, labels)
    

def main():
    """
    Lets the user input text for testing purposes.
    """
    classifier = SentimentClassifier()
    classifier.prompt_tests()


if __name__ == "__main__":
    main()
