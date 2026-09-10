<img width="858" height="272" alt="Screenshot 2026-09-10 171451" src="https://github.com/user-attachments/assets/7455d21a-dbc0-4bb6-a070-a5a4ece2dc32" />
<img width="875" height="238" alt="Screenshot 2026-09-10 171431" src="https://github.com/user-attachments/assets/522bd8bc-de01-43ba-9907-81a1059ba33e" />


# NLP Lab 04 — Viva / Reflection Answers

## 1. Word Order Invariance

### Question
Why does the sentence "Dog bites man" have the exact same Bag of Words representation as "Man bites dog"? How does this impact sentiment analysis?

### Answer
The Bag of Words (BoW) model represents a sentence by counting how many times each word occurs. It ignores grammar and word order.

Both sentences contain the same words — "dog", "bites", and "man" — with the same frequency, so they produce the same BoW representation.

This is a limitation for sentiment analysis because word order can change the meaning of a sentence. BoW may fail to understand relationships between words and sentence structure. Therefore, two sentences with different meanings can receive the same representation.

## 2. Sparsity Issue

### Question
What happens to the memory size and density of the BoW matrix when the corpus contains 100,000 unique vocabulary words?

### Answer
When the vocabulary contains 100,000 unique words, the BoW matrix becomes very large because every document gets a feature for every vocabulary word.

Most documents contain only a small portion of these words, so most matrix entries are zero.

Therefore, the matrix becomes high-dimensional and sparse. Storing it as a dense matrix can require a large amount of memory. Sparse matrix representations are preferred because they store mainly non-zero values and save memory.


## 3. Zero Similarity

### Question
Explain why Document 3 in Task 2 receives a Cosine Similarity score of 0.0000 when queried against "machine learning algorithms for data".

### Answer
Document 3 is:

"Natural language processing helps computers understand human language"

The query contains terms such as "machine", "learning", "algorithms", and "data" after English stop-word removal.

Document 3 does not contain any of these terms.

Because there is no overlapping term between the query and Document 3, their dot product is zero. Therefore, the cosine similarity is 0.0000.

This means that Document 3 has no term-based similarity with the given query.
