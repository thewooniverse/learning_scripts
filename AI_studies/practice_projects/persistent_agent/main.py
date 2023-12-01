
# Module and Library imports

from dotenv import load_dotenv
import os

import openai
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage



# env variables, constants and API keys
load_dotenv()
openai_api_key=os.getenv('OPENAI_API_KEY', 'YourAPIKey_BACKUP')
# print(openai_api_key) # check




def chat_agent(query, context):
    """
    """
    chat = ChatOpenAI(model='gpt-4-0613', openai_api_key=openai_api_key, model_name="gpt-4-0613")
    
    chat_history = [HumanMessage(content=query)]
    response = chat(chat_history)

    return response





def create_log(query, response):
    """
    Takes the query and response, and combine it into a log entry.
    """
    log_entry = f"""
QUERY:
{query}
--------
RESPONSE:
{response}
"""
    return log_entry


def save_log(log_entry):
    """
    Takes the query and response, and combine it into a log entry.
    """
    
















response = chat(
    [
        SystemMessage(content="You are a helpful AI agent like SIRI."),
        HumanMessage(content="What is a Bildungsroman.")
    ]
)
print(response)