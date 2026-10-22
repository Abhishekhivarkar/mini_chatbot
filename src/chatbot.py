from data.training_data import training_data
from src.naive_bayes_classifier import NaiveBayesClassifier 
from src.preprocessing import TextPreprocessor

class ChatBot:
    def __init__(self):
        self.preprocessor = TextPreprocessor()
        self.classifier = NaiveBayesClassifier()
        self.responses = {
            "greeting": "Hello! How can i help you?",
            "goodbye": "Goodbye! Have a great day!",
            "identity": "I am MiniChat AI, a simple chatbot built with Python.",
            "wellbeing": "I am doing well! Thanks for asking."
        }
        self._train()
    def _train(self):
        texts = [texts for texts,intent in training_data]
        labels = [intent for texts,intent in training_data]

        X = self.preprocessor.fit_transform(texts)

        self.classifier.fit(
                X,
                labels,
                self.preprocessor.vocabulary
            )
    def get_response(self,message):
        if not isinstance(message,str) or not message.strip():
            return "Please enter a valid message."

        vector = self.preprocessor.transform([message])[0]

        if not self.classifier.has_known_features(vector):
            return "I'm not sure i understand that yet."
        intent = self.classifier.predict(vector)

        return self.responses.get(
            intent,
            "I'm not sure how to respond to that"
        )

        