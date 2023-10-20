# Helper to read local files
import os
from dotenv import load_dotenv
import datetime

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
DOCS_PATH = os.path.join(os.path.dirname(__file__), f"documentations")

# construct models
embeddings = OpenAIEmbeddings(disallowed_special=(), openai_api_key=OPENAI_API_KEY)
llm = ChatOpenAI(temperature=0.5, model_name='gpt-4', openai_api_key=OPENAI_API_KEY)



# Define functions
def initialize_learn_dir(target_directory):
    """
    initialize_learn_dir(target_directory):
    - Initializes the learn directory with all of the relevant notes and any other important structures

    Args:
    - target_directory - this is a string name of the folder within documentations. The folder must be in documentations otherwise the function will raies an error.

    returns:
    - None
    """
    target_path = os.path.join(DOCS_PATH, target_directory)
    learning_path = os.path.join(DOCS_PATH, f'learn|{target_directory}')
    if not os.path.exists(learning_path):
        os.mkdir(learning_path)
    else:
        pass



def get_folder_size_MB(target_directory):
    """
    get_folder_size(folder_path):
    - calculates and returns the size of the contents of a given directory.

    Args:
    - target_directory - this is a string name of the folder within documentations. The folder must be in documentations otherwise the function will raies an error.

    Returns:
    - size(bytes)
    """
    target_path = os.path.join(DOCS_PATH, target_directory)
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(target_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    return total_size / 1024 / 1024





def create_vectostore(target_directory, is_subdir = False):
    """
    create_vectostore(target_directory):
    - Creates a vectorstore containing of all of the relevant files within the target directory and its sub directories by using os.walk() on the target_path
    - This creates a chroma_db within the /documentations/learn-target_directory/ path that contains the relevant embeddings.
    - File format wise the function currently, supports .txt and PDF

    - You may also target sub directories within the target_directory, such as thefuzz/data/ or thefuzz/thefuzz, but you must turn on the subdir flag as True

    Args:
    - target_directory - e.g. "thefuzz" this is a string name of the folder within documentations. 
                         The folder must be in documentations otherwise the function will raies an error.

    - is_subdir - default=False, use only when a sub directory is passed for example thefuzz/thefuzz

    Returns:
    None
    """
    # if it is a sub directory, like thefuzz/data/ -> then we must extract only "thefuzz" 
    # so that /documentations/learn|thefuzz/ is craeted and not /documentations/learn|thefuzz/data/
    if is_subdir:
        target_directory = target_directory.split(os.path.sep)[0]
    
    # establish the relevant paths
    target_path = os.path.join(DOCS_PATH, target_directory) # /learnGPT/documentations/thefuzz/
    learning_path = os.path.join(DOCS_PATH, f'learn|{target_directory}') # /learnGPT/documentations/learn|thefuzz/
    chroma_path = os.path.join(learning_path, 'chroma_db') # /learnGPT/documentations/learn|thefuzz/chroma_db/

    ## code snippet to calculate the last refreshed for future usage
    # timestamp = os.path.getmtime(target_path)
    # last_modified_date = datetime.datetime.fromtimestamp(timestamp)

    # instantiate the database
    db = Chroma(persist_directory=chroma_path, embedding_function=embeddings, collection_name=f'{target_directory}')

    # check the filesize of the database
    size = get_folder_size_MB(target_directory)
    # if the size is larger than 50
    if size > 50:
        print("The library is too big, please target sub directories")
        return
    else:
        print(size)









if __name__ == "__main__":
    test_target_directory_to_learn = "PDF_test"
    test_target_path = os.path.join(DOCS_PATH, test_target_directory_to_learn)
    create_vectostore(test_target_directory_to_learn)



