from math import log

class NaiveBayesClassifier:
    def __init__(self):
        self.intent_count = {}
        self.words_count_in_each_intent = {}
        self.total_example = 0
        self.total_words_in_each_intent = {}
        self.vocabulary = []
        self.is_trained = False

    def fit(self,X,y, vocabulary):
        if not X or not y or len(X) != len(y):
            raise ValueError(
                "X and y must be non-empty and have equal lengths."
            )
        
        self.vocabulary = list(vocabulary)
        self.intent_count = {}
        self.words_count_in_each_intent = {}
        self.total_words_in_each_intent = {}
        self.total_example = len(y)
        self.is_trained = False

        for intent in y:
            self.intent_count[intent] = (
                self.intent_count.get(intent,0) + 1
            )
        for intent in self.intent_count:
            # counts words for each intent example {greeting = {hi:2,hello:3}}
            self.words_count_in_each_intent[intent] = {} 
            # counts total words example hi = 2
            self.total_words_in_each_intent[intent] = 0

        for vector,intent in zip(X,y):
            if(len(vector) != len(self.vocabulary)):
                raise ValueError(
                    "Vector length must match vocabulary size."
                )
            for index,present in enumerate(vector):
                if present:
                    word = self.vocabulary[index]
                    self.words_count_in_each_intent[intent][word] = (
                        self.words_count_in_each_intent[intent].get(word,0) + 1
                    )
                    self.total_words_in_each_intent[intent] += 1
        self.is_trained = True
    def predict_score()


class NaiveBayesClassifier:
 def __init__(self):
  self.intent_count = {}
  self.words_count_in_each_intent = {}
  self.total_words_count_in_each_intent = {}
 def fit(self,X,y,vocabulary):
  for intent in y:
   self.intent_count[intent] = (
      self.intent_count.get(intent,0) + 1
   )
  for intent in self.intent_count:
   self.words_count_in_each_intent[intent] = {}
   self.total_words_count_in_each_intent[intent] = 0

  for vector,intent in zip(X,y):
     