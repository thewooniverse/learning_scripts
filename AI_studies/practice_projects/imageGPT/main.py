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


# env variables, constants and API keys
load_dotenv()
openai_api_key=os.getenv('OPENAI_API_KEY', 'YourAPIKey_BACKUP')
serpapi_api_key=os.getenv("SERPAPI_API_KEY", "YourAPIKey_Backup")
print(serpapi_api_key) # check
print(openai_api_key)
