training_data = [
    # Greeting
    ("hi", "greeting"),
    ("hello", "greeting"),
    ("hey", "greeting"),
    ("hi there", "greeting"),
    ("good morning", "greeting"),

    # Goodbye
    ("bye", "goodbye"),
    ("goodbye", "goodbye"),
    ("see you", "goodbye"),
    ("see you later", "goodbye"),
    ("talk to you later", "goodbye"),

    # Identity
    ("who are you", "identity"),
    ("what is your name", "identity"),
    ("tell me your name", "identity"),
    ("what should I call you", "identity"),
    ("introduce yourself", "identity"),

    # Wellbeing
    ("how are you", "wellbeing"),
    ("how are you doing", "wellbeing"),
    ("are you fine", "wellbeing"),
    ("how is it going", "wellbeing"),
    ("are you doing well", "wellbeing"),
]
 
vocabulary = set()

for text,intent in training_data:
 for word in text.lower().split():
  vocabulary.add(word)
  


vocabulary  = sorted(vocabulary)

def bag_of_words(text):
 words = text.lower().split()
 
 vector = []
 for word in vocabulary:
  if(word in words):
   vector.append(1)
  else:
   vector.append(0)
   
 return vector

X = []
y = []

for text,intent in training_data:
 X.append(bag_of_words(text))
 y.append(intent)

intent_counts = {}
for intent in y:
 intent_counts[intent] = intent_counts.get(intent,0)+1
 
word_count = {}
for text, intent in training_data:
 if intent not in word_count:
  word_count[intent] = {}
  
 for word in text.lower().split():
  word_count[intent][word] = (
   word_count[intent].get(word,0) + 1
   )
   
   
print("vocabulary : ",vocabulary)
print("X",X)
print("y",y)
print("Word_count",word_count)
print(intent_counts)