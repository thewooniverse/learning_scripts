
# Module and Library imports

from dotenv import load_dotenv
import os

import openai
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from templates import system_template

# Vector Support
# from langchain.vectorstores import FAISS >> instead of FAISS we will use Chroma
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

# Text loading and splitting
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter






# env variables, constants and API keys
load_dotenv()
OPENAI_API_KEY=os.getenv('OPENAI_API_KEY', 'YourAPIKey_BACKUP')
# print(openai_api_key) # check


CHROMA_DIR = os.path.join(os.path.dirname(__file__), f"Chroma_DB_store")
test_chroma_path = os.path.join(CHROMA_DIR, 'test_chroma') 
# /.../persistent_agent/test_chroma/ -- I can also later change the test_chroma to something else.
# I could use it for different Databases for different projects;
# And even within the database, I could have different collection names

embeddings = OpenAIEmbeddings(disallowed_special=(), openai_api_key=OPENAI_API_KEY)



"""
Development workflow:
Build and test querying and logging 
- 
Then build and test retrieval engines to pass into as contexts.
"""








# define function for constructing chat history to be passed to model
def construct_chat_history(query, context=""):
    """
    Returns: chat_history object that contains SystemMessage, AIMessage and HumanMessage
    context - a plain string containing the summarized retrieved context from the ChromaDB based on the query; default is an empty string.
    query - a plain string that was asked to the agent
    """
    system_message = system_template + context
    
    chat_history = [
        SystemMessage(content=system_message),
        HumanMessage(content=query)
    ]
    return chat_history

def chat_agent(chat_history):
    """
    Calls the Chat Model to give a response to the given chat history.
    """
    agent = ChatOpenAI(model='gpt-4-0613', openai_api_key=OPENAI_API_KEY, model_name="gpt-4-0613")
    response = agent(chat_history)
    return response


# create log script
def create_log(query, response):
    """
    Takes the query and response, and combine it into a log entry.
    """
    log_entry = f"""

HUMAN QUERY:
{query}
--------
AI RESPONSE:
{response}
"""
    return log_entry




def save_log(log_entry, chroma_path):
    """
    Takes the log entry and saves it to the persistent ChromaDB designated;
    """
    # get the chroma path and open the persistent library to that destination when it is called;
    vectorstore = Chroma(persist_directory=chroma_path, embedding_function=embeddings)

    embedded_document = embeddings.embed_documents(log_entry)
    document = Document(page_content=log_entry, embedding=embedded_document)
    vectorstore.add_documents([document])
    vectorstore.persist()






# define overarching querying function
def persistent_chat(query):
    """
    Function to bring context, query and
    """
    # extract the contexts from the database and construct the query/chat_history
    context = "" # later to be replaced by context extracting function
    chat_history = construct_chat_history(query, context)
    response = chat_agent(chat_history)

    log_entry = create_log(query, response)
    save_log(log_entry, test_chroma_path)

    print(log_entry)
    print("Saved")



persistent_chat("What is my name?")




