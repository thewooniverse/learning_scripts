import os
from dotenv import load_dotenv
from langchain.llms import OpenAI


from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings

# load env variables and set the 
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')



embeddings = OpenAIEmbeddings(disallowed_special=(), openai_api_key=openai_api_key)


