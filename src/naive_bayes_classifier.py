
from math import log


class NaiveBayesClassifier:

    def __init__(self):
        self.intent_counts = {}
        self.word_counts = {}
        self.total_examples = 0
        self.total_words = {}
        self.vocabulary = []
        self.is_trained = False
    def has_known_features(self,vector):
        return any(vector)
    
    def fit(self, X, y, vocabulary):
        if not X or not y or len(X) != len(y):
            raise ValueError(
                "X and y must be non-empty and have equal lengths."
            )

        self.vocabulary = list(vocabulary)
        self.intent_counts = {}
        self.word_counts = {}
        self.total_words = {}
        self.total_examples = len(y)
        self.is_trained = False

        # Count examples for each intent
        for intent in y:
            self.intent_counts[intent] = (
                self.intent_counts.get(intent, 0) + 1
            )

        # Initialize word counts for each intent
        for intent in self.intent_counts:
            self.word_counts[intent] = {}
            self.total_words[intent] = 0

        # Count words using Bag of Words vectors
        for vector, intent in zip(X, y):
            if len(vector) != len(self.vocabulary):
                raise ValueError(
                    "Vector length must match vocabulary size."
                )

            for index, present in enumerate(vector):
                if present:
                    word = self.vocabulary[index]

                    self.word_counts[intent][word] = (
                        self.word_counts[intent].get(word, 0) + 1
                    )

                    self.total_words[intent] += 1

        self.is_trained = True

    def predict_scores(self, vector):
        if not self.is_trained:
            raise RuntimeError("Train the model before prediction.")

        if len(vector) != len(self.vocabulary):
            raise ValueError(
                "Vector length must match vocabulary size."
            )

        scores = {}
        vocabulary_size = len(self.vocabulary)

        for intent in self.intent_counts:
            # Log prior probability
            prior = (
                self.intent_counts[intent] / self.total_examples
            )

            score = log(prior)

            # Word likelihood with Laplace smoothing
            denominator = (
                self.total_words[intent] + vocabulary_size
            )

            for index, present in enumerate(vector):
                if present:
                    word = self.vocabulary[index]

                    count = self.word_counts[intent].get(word, 0)

                    probability = (count + 1) / denominator
                    score += log(probability)

            scores[intent] = score

        return scores

    def predict(self, vector):
        scores = self.predict_scores(vector)
        return max(scores, key=scores.get)
