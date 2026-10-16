class TextPreprocessor:

    def __init__(self):
        self.vocabulary = []

    def fit(self, texts):
        vocabulary = set()
        for text in texts:
            for word in text.lower().split():
                vocabulary.add(word)
        self.vocabulary = sorted(vocabulary)

    def transform(self, texts):
        if not self.vocabulary:
            raise ValueError("Vocalbulary is empty. Call fit() first.")

        vectors = []
        for text in texts:
            words = text.lower().split()

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
