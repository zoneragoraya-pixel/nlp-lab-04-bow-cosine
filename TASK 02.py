import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Machine learning algorithms analyze structured data effectively",
    "Deep learning and neural networks excel at processing unstructured data",
    "Natural language processing helps computers understand human language",
    "Python is widely used for machine learning and data science"
]

query = ["machine learning algorithms for data"]

vectorizer = CountVectorizer(stop_words="english")

doc_vectors = vectorizer.fit_transform(documents)

query_vector = vectorizer.transform(query)

similarity_scores = cosine_similarity(
    query_vector,
    doc_vectors
)

scores = similarity_scores[0]

results = pd.DataFrame({
    "Document": documents,
    "Similarity Score": scores
})

results = results.sort_values(
    by="Similarity Score",
    ascending=False
)

results = results.reset_index(drop=True)

results.insert(0, "Rank", range(1, len(results) + 1))

print("Search Query:")
print(query[0])

print("\nRanked Documents:")
print(results.to_string(index=False))