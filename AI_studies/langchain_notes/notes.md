

Certainly! Here are the basics of using ChromaDB to store vectors with LangChain:

• Installation: First, you need to install the chromadb package. You can do this by running pip install chromadb.

• Creating a Chroma vector store: To create a Chroma vector store, you can use the Chroma class from the langchain.vectorstores module. You'll need to provide a collection name and an embedding function. For example:
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()
vectorstore = Chroma(collection_name="my_collection", embedding_function=embeddings)
In this example, we create a Chroma vector store named "my_collection" using the OpenAIEmbeddings as the embedding function.

• Adding documents: You can add documents to the Chroma vector store using the add_documents() method. This method takes a list of Document objects as input. For example:
from langchain.schema import Document

docs = [
    Document(page_content="Document 1", metadata={"key": "value1"}),
    Document(page_content="Document 2", metadata={"key": "value2"})
]

vectorstore.add_documents(docs)
In this example, we create two Document objects and add them to the Chroma vector store.

• Querying for similar vectors: You can perform similarity search on the Chroma vector store using the similarity_search() method. This method takes a query vector as input and returns the most similar vectors from the store. For example:
query_vector = embeddings.embed_query("query text")
similar_docs = vectorstore.similarity_search(query_vector)
In this example, we embed the query text using the embedding function and then perform a similarity search on the Chroma vector store.


These are the basic steps for using ChromaDB to store vectors with LangChain. You can also explore other functionalities provided by ChromaDB, such as updating documents, deleting documents, and more. Refer to the LangChain documentation for more details and examples. 2