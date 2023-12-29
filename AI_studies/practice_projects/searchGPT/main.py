# Module and Library imports

from dotenv import load_dotenv
import os

import openai
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage

# Vector Support
# from langchain.vectorstores import FAISS >> instead of FAISS we will use Chroma
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

# Text loading and splitting
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain


# agents + toolkits
from langchain.agents import load_tools
from langchain.agents import initialize_agent


# env variables, constants and API keys
load_dotenv()
openai_api_key=os.getenv('OPENAI_API_KEY', 'YourAPIKey_BACKUP')
serpapi_api_key=os.getenv("SERPAPI_API_KEY", "YourAPIKey_Backup")
# print(serpapi_api_key) # check

# loading toolkits
llm = OpenAI(temperature=0, openai_api_key=openai_api_key)
toolkit = load_tools(["serpapi"], llm=llm, serpapi_api_key=serpapi_api_key)

agent = initialize_agent(toolkit, llm, agent="zero-shot-react-description", verbose=True, return_intermediate_steps=True)
response = agent({"What is the meaning of life?"})
print(response)
