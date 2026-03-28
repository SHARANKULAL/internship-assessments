import string
from nltk.corpus import stopwords

text = "Hello!!! This is a Sample text."

text = text.lower()
text = text.translate(str.maketrans('', '', string.punctuation))

stop_words = set(stopwords.words('english'))
words = [w for w in text.split() if w not in stop_words]

print(" ".join(words))