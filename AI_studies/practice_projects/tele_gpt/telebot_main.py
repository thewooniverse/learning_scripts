

### importing modules ###
import os
from dotenv import load_dotenv

## Telegram + formatting libraries
import telebot

## OpenAI libraries
import openai
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from msg_templates import system_template

# Vector Support
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings



### importing API Keys and setting constants ###
load_dotenv()
TG_API_KEY = os.getenv('TG_API_KEY')
OPENAI_API_KEY = os.getenv('OPEN_AI_API_KEY')
# print(OPEN_API_KEY) # prints 'test ABC' correctly
# print(TG_API_KEY)


bot = telebot.TeleBot(TG_API_KEY)
embeddings = OpenAIEmbeddings(disallowed_special=(), openai_api_key=OPENAI_API_KEY)
default_agent = ChatOpenAI(model='gpt-4-0613', openai_api_key=OPENAI_API_KEY, model_name="gpt-4-0613")



### Defining Telegram Bot functions and decorators ###

# Defining a command handler
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f"Hello! I'm here to help! {bot.get_my_name().name}")
    # all the configurations / guide tutorial strings here



# Defining the query command handler
@bot.message_handler(commands=['chat'])
def send_chat_response(message):
    # split the query:
    query = " ".join(message.text.split()[1:])
    context_aware_chat_history = construct_chat_history(query)
    response = chat_agent(context_aware_chat_history)
    bot.reply_to(message, response.content, parse_mode='Markdown')



### Defining ChatGPT query related functionality ###
def chat_agent(chat_history, agent=default_agent):
    """
    Calls the Chat Model to give a response to the given chat history.
    """
    response = agent(chat_history)
    return response

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






### Starting the bot ###
bot.polling()




