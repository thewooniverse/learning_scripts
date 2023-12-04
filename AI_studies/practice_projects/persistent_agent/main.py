
# Module and Library imports

from dotenv import load_dotenv
import os

import openai
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from templates import system_template



# env variables, constants and API keys
load_dotenv()
openai_api_key=os.getenv('OPENAI_API_KEY', 'YourAPIKey_BACKUP')
# print(openai_api_key) # check


CHROMA_DIR = os.path.join(os.path.dirname(__file__), f"Chroma_DB_store")
test_chroma_path = os.path.join(CHROMA_DIR, 'test_chroma') 
# /.../persistent_agent/test_chroma/ -- I can also later change the test_chroma to something else.
# I could use it for different Databases for different projects;
# And even within the database, I could have different collection names






"""
Development workflow:
Build and test querying and logging 
- 
Then build and test retrieval engines
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
    chat = ChatOpenAI(model='gpt-4-0613', openai_api_key=openai_api_key, model_name="gpt-4-0613")
    response = chat(chat_history)
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
    pass 











