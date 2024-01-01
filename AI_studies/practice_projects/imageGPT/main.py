# Module and Library imports

from dotenv import load_dotenv
import os
import pyperclip

import openai
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage

# Vector Support
# from langchain.vectorstores import FAISS >> instead of FAISS we will use Chroma
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

# Image generation:
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.utilities.dalle_image_generator import DallEAPIWrapper



# env variables, constants and API keys
load_dotenv()
openai_api_key=os.getenv('OPENAI_API_KEY', 'YourAPIKey_BACKUP')
serpapi_api_key=os.getenv("SERPAPI_API_KEY", "YourAPIKey_Backup")
# print(serpapi_api_key) # check
# print(openai_api_key)


# Functions for testing image generation / DALL-E - This I also need to learn with OpenAI module as Langchain module / docs is outdated
## in most cases, learning OpenAI module directly is more useful than learning only langchain - as langchain is in the end a wrapper for OpenAI and other language model APIs.

# Functions for testing image based querying (AI Vision) - for this, I must use OpenAI module




