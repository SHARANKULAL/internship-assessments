import string

stopwords = [
    "is", "am", "are", "the", "a", "an", "and",
    "to", "in", "of", "for", "on", "at", "this",
    "it", "that", "was", "were"
]

def clean_text(text):
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Split into words
    words = text.split()

    # Remove stopwords
    filtered_words = [word for word in words if word not in stopwords]

    cleaned_text = " ".join(filtered_words)
    return cleaned_text


# Test the cleaner
test_sentences = [
    "Hello!!! This is a Simple TEXT cleaning program.",
    "The Quick Brown Fox Jumps Over the Lazy Dog.",
    "Python is great for Data Science and Machine Learning!",
]

for sentence in test_sentences:
    print("Original:", sentence)
    print("Cleaned :", clean_text(sentence))
    print()
