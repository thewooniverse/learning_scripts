# Helper to read local files
import os
from dotenv import load_dotenv

# Vector Support
# from langchain.vectorstores import FAISS >> instead of FAISS we will use Chroma
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

# Model and chain
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.chains import RetrievalQA


# Text splitters
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader

# Schemas
from langchain.schema import HumanMessage, SystemMessage, AIMessage




# load API keys
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'YourAPIKey')

# construct models
embeddings = OpenAIEmbeddings(disallowed_special=(), openai_api_key=OPENAI_API_KEY)
llm = ChatOpenAI(temperature=0.5, model_name='gpt-4', openai_api_key=OPENAI_API_KEY)


# # construct the document embeddings
root_dir = './documentations/thefuzz'
documents = []

# # Go through each folder
for dirpath, dirnames, filenames in os.walk(root_dir):
    print(dirpath)
    print(dirnames)
    # Go through each file
    for file in filenames:
        try: 
            # Load up the file as a doc and split
            print (file)
            loader = TextLoader(os.path.join(dirpath, file), encoding='utf-8')
            documents.extend(loader.load_and_split())
        except Exception as e: 
            pass

# print (f"You have {len(documents)} documents\n")
# # print ("------ Start Document ------")
# # print (documents[0].page_content[:300])



# db = Chroma.from_documents(documents, embeddings, persist_directory="./chroma_db")
db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)

retriever = db.as_retriever()

qa_chain = RetrievalQA.from_chain_type(llm, retriever=retriever, verbose=True)
query = "Who is Donald Trump"
result = qa_chain.run(query)
print(result)


"""

QUERY: What is the Fuzz?
`thefuzz` is a Python library that provides functions for fuzzy string matching and similarity calculations. 
It is used for tasks such as string matching, searching, and deduplication. 
The library offers various algorithms and methods to calculate the similarity between strings, 
allowing users to find matches even when there are slight differences or variations in the strings. 
It is commonly used in applications like search engines, autocomplete suggestions, data deduplication, 
data cleaning and preprocessing, natural language processing, and spell checking and correction.
"""





