import unittest

from data.training_data import training_data
from src.preprocessing import TextPreprocessor
from src.naive_bayes_classifier import NaiveBayesClassifier


class TestNaiveBayesClassifier(unittest.TestCase):

    def setUp(self):
        self.preprocessor = TextPreprocessor()

        texts = [text for text, intent in training_data]
        self.y = [intent for text, intent in training_data]

        self.X = self.preprocessor.fit_transform(texts)

        self.model = NaiveBayesClassifier()
        self.model.fit(
            self.X,
            self.y,
            self.preprocessor.vocabulary
        )

    def predict_message(self, message):
        vector = self.preprocessor.transform([message])[0]
        return self.model.predict(vector)
    def test_unknown_message_has_no_known_features(self):
        vector = self.preprocessor.transform(["gotta run"])[0]

        self.assertFalse(
            self.model.has_known_features(vector)
        )
    def test_greeting_prediction(self):
        self.assertEqual(
            self.predict_message("hello"),
            "greeting"
        )

    def test_identity_prediction(self):
        self.assertEqual(
            self.predict_message("who are you"),
            "identity"
        )

    def test_wellbeing_prediction(self):
        self.assertEqual(
            self.predict_message("how are you"),
            "wellbeing"
        )

    def test_goodbye_prediction(self):
        self.assertEqual(
            self.predict_message("see you later"),
            "goodbye"
        )
    def test_unseen_greeting(self):
        self.assertEqual(
        self.predict_message("yo mate"),
        "greeting"
      )

    def test_unseen_identity(self):
        self.assertEqual(
        self.predict_message("what's your name"),
        "identity"
    )

    def test_unseen_wellbeing(self):
        self.assertEqual(
        self.predict_message("how's life treating you"),
        "wellbeing"
    )

    def test_unseen_goodbye(self):
        self.assertEqual(
        self.predict_message("gotta run"),
        "goodbye"
    )
  
    def test_training_example_count(self):
        self.assertEqual(self.model.total_examples, 100)

    def test_debug_unseen_goodbye(self):
        vector = self.preprocessor.transform(["gotta run"])[0]

        print("\nVector:",vector)
        print("Scores:",self.model.predict_scores(vector))
        print("Prediction: ",self.model.predict(vector))

if __name__ == "__main__":
    unittest.main()