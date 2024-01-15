

## What are embeddings?
OpenAI’s text embeddings measure the relatedness of text strings. 
Embeddings are commonly used for:

- Search (where results are ranked by relevance to a query string)
- Clustering (where text strings are grouped by similarity)
- Recommendations (where items with related text strings are recommended)
- Anomaly detection (where outliers with little relatedness are identified)
- Diversity measurement (where similarity distributions are analyzed)
- Classification (where text strings are classified by their most similar label)

An embedding is a vector (list) of floating point numbers. The distance between two vectors measures their relatedness. Small distances suggest high relatedness and large distances suggest low relatedness.

* Assistants API comes with retrieval and built in message history management. If you don't want to worry about making and storing embeddings yourself, check out the Assistants API to learn more.



## How to get embeddings
To get an embedding, send your text string to the embeddings API endpoint along with the embedding model ID (text-embedding-ada-002). The response will contain an embedding, which you can extract, save, and use. (examples / exercises in embeddings.py)

https://cookbook.openai.com/examples/get_embeddings_from_dataset






