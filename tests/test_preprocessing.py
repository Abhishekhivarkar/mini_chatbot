import unittest

from src.preprocessing import TextPreprocessor


class TestTextPreprocessor(unittest.TestCase):

    def setUp(self):
        self.preprocessor = TextPreprocessor()

    def test_vocabulary_creation(self):
        self.preprocessor.fit(["hi", "hello", "hi"])

        self.assertEqual(self.preprocessor.vocabulary, ["hello", "hi"])

    def test_bag_of_words(self):
        self.preprocessor.fit(["hi", "hello"])

        result = self.preprocessor.transform(["hello"])

        self.assertEqual(result, [[1, 0]])

    def test_multiple_messages(self):
        self.preprocessor.fit(["hi", "hello"])

        result = self.preprocessor.transform(["hello", "hi", "hello hi"])

        self.assertEqual(result, [[1, 0], [0, 1], [1, 1]])

    def test_transform_before_fit(self):
        with self.assertRaises(ValueError):
            self.preprocessor.transform(["hello"])
    def test_normalize(self):
        self.assertEqual(
            self.preprocessor.normalize("HELLO!!!"),
            "hello"
        )

if __name__ == "__main__":
    unittest.main()

