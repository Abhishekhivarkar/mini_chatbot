
class TextPreprocessor:

 def __init__(self):
  self.vocabulary = []

 def fit(self, texts):
  vocabulary = set()
  for text in texts:
   for word in text.lower().split():
    vocabulary.add(word)
  self.vocabulary = sorted(vocabulary)
 
 def transform(self,text):
  