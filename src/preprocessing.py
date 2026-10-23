import string
class TextPreprocessor:

    def __init__(self):
        self.vocabulary = []
    def normalize(self,text):
        text = text.lower()
        text = text.translate(
            str.maketrans("","",string.punctuation)
        )
        return text
    def fit(self, texts):
        vocabulary = set()
        for text in texts:
            text = self.normalize(text)
            for word in text.split():
                vocabulary.add(word)
        self.vocabulary = sorted(vocabulary)

    def transform(self, texts):
        if not self.vocabulary:
            raise ValueError("Vocalbulary is empty. Call fit() first.")

        vectors = []
        for text in texts:
            text = self.normalize(text)
            words = text.split()
            vector = []
            for word in self.vocabulary:
                if word in words:
                    vector.append(1)
                else:
                    vector.append(0)
            vectors.append(vector)

        return vectors

    def fit_transform(self, texts):
        self.fit(texts)
        return self.transform(texts)
