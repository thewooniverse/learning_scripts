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

# Text splitters
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader

# Schemas
from langchain.schema import HumanMessage, SystemMessage, AIMessage




# load API keys and constants
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'YourAPIKey')
SELF_PATH = os.path.join(os.path.dirname(__file__), f"documentations")

# construct models
embeddings = OpenAIEmbeddings(disallowed_special=(), openai_api_key=OPENAI_API_KEY)
llm = ChatOpenAI(temperature=0.5, model_name='gpt-4', openai_api_key=OPENAI_API_KEY)



# Define functions
def initialize_learn_dir(target_directory):
    """
    
    """
    pass









if __name__ == "__main__":
    test_target_dirname = "thefuzz"
    test_target_path = os.path.join(SELF_PATH, test_target_dirname)



