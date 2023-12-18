

### importing modules ###
import os
from dotenv import load_dotenv

## Telegram + formatting libraries
import telebot

## config support
import json
import requests

## OpenAI libraries
import openai
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from msg_templates import system_template, start_template

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
# default_agent = ChatOpenAI(model='gpt-4-0613', openai_api_key=OPENAI_API_KEY, model_name="gpt-4-0613", temperature=0.7)



### Defining Telegram Bot functions and decorators ###

## Helper functions ##
def load_config(group_id):
    chats_path = os.path.join(os.path.dirname(__file__), f"chats") # tele_gpt/chats/
    group_path = f'{chats_path}{os.path.sep}{group_id}' # ex. tele_gpt/chats/2849193
    config_path = f"{group_path}{os.path.sep}config.json" # ex. tele_gpt/chats/2849193/config.json
    if not os.path.exists(config_path):
        # check if the group path itself exists, if it doesn't create it.
        if not os.path.exists(group_path):
            os.mkdir(group_path)
      
      # then open the default config, and write its content (default settings) into the config_path file
        with open(f"{os.path.dirname(__file__)}{os.path.sep}default_config.json", 'r') as rf:
            default_config = json.load(rf)
            # print(default_config)
            wf = open(config_path, 'w')
            json.dump(default_config, wf)
            wf.close()

   # load and return the configuration
    with open(config_path, 'r') as rf:
        config_dict = json.load(rf)
        return config_dict


def set_config(group_id, new_config):
    """
    group_id == chatid
    new_config should be a dict config that has the same structure but with new settings
    """
    chat_path = f'{os.getcwd()}{os.path.sep}chats'
    group_path = f'{chat_path}{os.path.sep}{group_id}'
    config_path = f"{group_path}{os.path.sep}config.json"

    with open(config_path, 'w') as wf:
        json.dump(new_config, wf)


def check_can_delete(group_id):
    """
    Returns - True or False based on whether the bot can delete messages in a given group
    """
    bot_token = TG_API_KEY
    chat_id = group_id # Replace with your group chat ID
    bot_user_id = bot.get_me().id # get the bot's own user ID
    url = f"https://api.telegram.org/bot{bot_token}/getChatMember?chat_id={chat_id}&user_id={bot_user_id}"
    response = requests.get(url).json()
    if response["ok"]:
        status = response["result"]["status"]
        can_delete_messages = response["result"].get("can_delete_messages", False)

        if status == "administrator" and can_delete_messages:
            # print("bot can delete messages")
            return True
        else:
            # print("bot cannot delete messages")
            return False
    else:
        print("Error in fetching chat member details.")











## settings comamands ##
# Defining a command handler
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f"{start_template}", parse_mode='HTML')
    # all the configurations / guide tutorial strings here


@bot.message_handler(commands=['set_apikey'])
def set_api_key(message):
    api_key_entered = message.text.split()[1]
    config = load_config(message.chat.id)
    config['OPENAI_API_KEY'] = api_key_entered
    set_config(message.chat.id, config)
    
    if check_can_delete(message.chat.id):
        # Attempt to delete the message
        bot.reply_to(message, "API Key has been saved, deleting message.")
        bot.delete_message(message.chat.id, message.message_id)
    else:
        bot.reply_to(message, "API Key was saved, however I do not have permission to delete this message. Please delete this message and set me as an admin.")






## chatting commands ##
# Defining the query command handler
@bot.message_handler(commands=['chat'])
def send_chat_response(message):
    # load the config
    config = load_config(message.chat.id)

    # split the query:
    query = " ".join(message.text.split()[1:])

    # get the context / retrieved summary of documents
    context = "" # later this will

    # construct the chat history based on the context and configurations
    context_aware_chat_history = construct_chat_history(query, config['additional_system_message'], context)

    # construct the chat agent and query it;
    response = chat_agent(context_aware_chat_history, config)
    if not response:
        bot.reply_to(message, "API Key is invalid, please /set_apikey to set your OpenAI API Key again")
    else:
        bot.reply_to(message, response.content, parse_mode='Markdown')



### Defining ChatGPT query related functionality ###
def chat_agent(chat_history, configurations):
    """
    Creates a chat model based on the configurations passed to it by unpacking it;
    """
    agent = ChatOpenAI(model=configurations['model_name'], openai_api_key=configurations['OPENAI_API_KEY'], model_name=configurations['model_name'], temperature=configurations['temperature'])
    try:
        response = agent(chat_history)
        return response
    except openai.AuthenticationError:
        return False
        

def construct_chat_history(query, addl_system_message, context=""):
    """
    Returns: chat_history object that contains SystemMessage, AIMessage and HumanMessage
    query - a plain string that was asked to the agent
    addl_system_message - Addtional System instructions for the agent, for example - "You are an expert travel guide..."
    context - a plain string containing the summarized retrieved context from the ChromaDB based on the query; default is an empty string.
    """
    system_message = system_template + context
    
    chat_history = [
        SystemMessage(content=system_message),
        SystemMessage(content=f"Additional System Messages:\n{addl_system_message}"),
        HumanMessage(content=query)
    ]
    return chat_history



### Starting the bot ###
bot.polling()




