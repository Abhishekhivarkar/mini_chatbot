class NaiveBayesClassifier:
    def __init__(self):
        self.intent_count = {}
        self.word_counts = {}
        self.total_example = 0