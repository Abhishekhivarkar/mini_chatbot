from math import log

class NaiveBayesClassifier:
    def __init__(self):
        self.intent_count = {}
        self.word_counts = {}
        self.total_example = 0
        self.total_words = {}
        self.vocabulary = []
        self.is_trained = False

    def fit(self,X,y, vocabulary):
        if not X or not y or len(X) != len(y):
            raise ValueError(
                "X and y must be non-empty and have equal lengths."
            )
        
        self.vocabulary = list(vocabulary)
        self.intent_count = {}
        self.word_counts = {}
        self.total_words = {}
        self.total_example = len(y)
        self.is_trained = False

        for intent in y:
            self.intent_count.get(intent,0) + 1
        for intent in self.intent_count:
            self.intent_count[intent] = {}
            self.total_words[intent] = 0

        for vector,intent in zip(X,y):
            if(len(vector) != len(self.vocabulary)):
                raise ValueError(
                    "Vector length must match vocabulary size."
                )
            for index,present in enumerate(vector):
                