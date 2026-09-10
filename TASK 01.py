import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

corpus = [
    "The product performance is amazing and fast",
    "The service was fast and performance was great",
    "Terrible customer service and bad performance"
]

vectorizer = CountVectorizer(stop_words="english")

X = vectorizer.fit_transform(corpus)

vocabulary = vectorizer.get_feature_names_out()

bow_matrix = pd.DataFrame(
    X.toarray(),
    columns=vocabulary
)

print("Vocabulary:")
print(list(vocabulary))

print("\nBag of Words Matrix:")
print(bow_matrix)