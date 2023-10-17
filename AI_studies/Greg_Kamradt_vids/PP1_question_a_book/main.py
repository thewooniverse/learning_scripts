
# modules necessary for API keys
import os
from dotenv import load_dotenv

# PDF Loaders. If unstructured gives you a hard time, try PyPDFLoader
from langchain.document_loaders import UnstructuredPDFLoader, OnlinePDFLoader, PyPDFLoader
from langchain.schema import Document

# text splitters
from langchain.text_splitter import RecursiveCharacterTextSplitter

# vector stores and embedding
from langchain.vectorstores import Chroma
import chromadb
from langchain.embeddings.openai import OpenAIEmbeddings
from tqdm.autonotebook import tqdm
from chromadb.utils import embedding_functions



# importing
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain



# loading the environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'YourAPIKey')
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

# Loading the PDF into documents
# loader = PyPDFLoader("./field-guide-to-data-science.pdf") # this is a loader object
# print(type(loader)) # <class 'langchain.document_loaders.pdf.PyPDFLoader'>
## Other options for loaders 
# loader = UnstructuredPDFLoader("../data/field-guide-to-data-science.pdf")
# loader = OnlinePDFLoader("https://wolfpaulus.com/wp-content/uploads/2017/05/field-guide-to-data-science.pdf")

# loading the PyPDF loader as data
# data = loader.load() # data is a list collection of documents that have been loaded.

# Note: If you're using PyPDFLoader then we'll be splitting for the 2nd time.
# This is optional, test out on your own data.
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=0)
# texts = text_splitter.split_documents(data)
# Note: If you're using PyPDFLoader then it will split by page for you already
# print (f'You have {len(data)} document(s) in your data')
# print (f'There are {len(data[5].page_content)} characters in your document')



# query for similarity search;
query = "Who is the author of field guide to data science? And who is Karthik Raghunathan?"

# Using Chroma wrapper
# save to disk
# db2 = Chroma.from_documents(texts, embeddings, persist_directory="./chroma_db", collection_name="DATASCI")
# docs = db2.similarity_search(query)

# load from disk
db3 = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
# print(type(db3)) # <class 'langchain.vectorstores.chroma.Chroma'>
docs = db3.similarity_search(query)
# print(docs[0].page_content)

llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)
chain = load_qa_chain(llm, chain_type="stuff", verbose=True)
output = chain.run(input_documents=docs, question=query)
print(output)

"""
OUTPUT: "Who is the author of field guide to data science? And who is Karthik Raghunathan?"
CONTEXT: Same as the below context in loading without specifying collection name, but also commenting out the rest of the vector dance above
and simply loading the Chroma_db.
db3 = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)

Interesting to note that the model seems to be hallucinating a bit, this 
---
The author of the field guide to data science is Karthik Raghunathan.
He is a data scientist and the founder of the Data Science Lab.







OUTPUT: "Give me the answers in bullet points. 
- 1.) What is the data science process. 
- 2.) What do graduate admission committee look for in a personal statement?"

CONTEXT: Loaded from disk, without specifying collection name
db3 = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)

This shows when the collection is not specified, the vectorstore loads all the vectors in the chromadb
--
1.) The data science process typically involves data collection, data cleaning, exploratory 
data analysis, data visualization, predictive modeling, and model evaluation.

2.) Graduate admission committees typically look for a personal statement that demonstrates 
a student's academic and professional goals, their qualifications and experience, and their ability to communicate effectively.




OUTPUT: "Who is the author of the field guide to data science?"
- Context: DATASCI collection exists, but in loading from disk, collection name of DAGAP was called.
db3 = Chroma(persist_directory="./chroma_db", embedding_function=embeddings, collection_name="DAGAP")
This shows that even if the collection DATASCI exists, if DAGAP collection is loaded, then the vectorstore does not have context
into what the answer to the question specific to DATASCI is.

The author of the field guide to data science is not mentioned in the given context.




OUTPUT: "What is the data science process?"
- Context is that DATASCI collection was created and queried against. Gives correct answer.
The data science process is the process of transforming data into actionable insights through the use of tradecraft,
data products, and inductive reasoning.


OUTPUT: "What is the data science process?"
- Context is that the chroma_db only has the "DAGAP" collection, and the DAGAP collection was called.
I don't know.


OUTPUT: "What does the author mean by 'Letters for which the right to read has been waived'"

Letters for which the right to read has been waived means letters where 
the applicant has given up their right to read the letter before it is sent to the committee.
This ensures confidentiality of the letters and reduces the chance that the letter writer was influenced by the applicant.


OUTPUT: "What are do the admission committee look for in reference letters? Please answer in bullet points"

- Letters that are composed in confidentiality by the person it claims to be
- Letters that cite personal experiences or facts to support their claims
- Letters that talk in detail about the applicant's work and how they fared
- Letters that highlight projects, achievements, and other salient information
- Letters that give an idea of the applicant's impression on the recommender
- Letters that are not overly glorifying
- Letters for which the right to read has been waived



OUTPUT - What are some of the things that the graduate admission committee looks at from an applicant?
...
 The graduate admission committee looks at the applicant's GRE and TOEFL scores, academic record, statement of purpose, and recommendation letters. 
 They also consider other factors such as the applicant's résumé and any awards or medals they have received.


OUTPUT - What is the data science process?
...
The data science process involves setting up the infrastructure, aggregating and preparing the data, incorporating domain expert knowledge, 
trying different analytic techniques and models on subsets of the data, evaluating the models, refining, evaluating again, 
and selecting a model, and then doing something with the models and results.
"""



"""

"""
















# Using Chroma client;
"""
You can use this method if you have an existing Chroma client;
"""
# persistent_client = chromadb.PersistentClient(path="./chroma_db")
# collection = persistent_client.get_or_create_collection("my_collection", embedding_function=embeddings)
# # print(type(collection)) #<class 'chromadb.api.models.Collection.Collection'>
# collection.add(texts)

# langchain_chroma = Chroma(
#     client=persistent_client,
#     collection_name="collection_name",
#     embedding_function=embeddings,
# )


# Usign Chroma and docsearch to retrieve relevant documents based on embeddings of query and docs;

# vectorstore = Chroma(collection_name="my_collection", embedding_function=embeddings)
# print(type(vectorstore)) #<class 'langchain.vectorstores.chroma.Chroma'>

# vectorstore.add_documents(texts)
# collection.persist()

# print(vectorstore)


# query = "What is the data science process?"
# results = vectorstore.similarity_search(query)
# print(results)

# openai_ef = embedding_functions.OpenAIEmbeddingFunction(
#                 api_key=OPENAI_API_KEY,
#                 model_name="text-embedding-ada-002"
#             )

# docsearch = Chroma.from_documents(data, embeddings)

# query = "What is the data science process?"
# docs = docsearch.similarity_search(query) 
# # print(docs)

# # combining the returned docs with LLMs 
# llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)
# chain = load_qa_chain(llm, chain_type="stuff", verbose=True)
# output = chain.run(input_documents=docs, question=query)

# # docs = docsearch.similarity_search(query)
# # print(output)







