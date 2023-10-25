# Helper to read and write local files
import os
from dotenv import load_dotenv
import datetime
import json

# Vector Support
# from langchain.vectorstores import FAISS >> instead of FAISS we will use Chroma
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

# Loaders;
from langchain.document_loaders import UnstructuredPDFLoader, OnlinePDFLoader, PyPDFLoader

# Model and chain
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.chains.question_answering import load_qa_chain

# Text splitters and doc loaders
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Schemas
from langchain.schema import HumanMessage, SystemMessage, AIMessage

"""

TODO:
- logging messages
- different chain types for different usecases in constructing initial learning elements; using chat history as well to construct the actual learning paths
- and notes for each chapter + exercises and practice projects;
--> basically, building your own "chain" using langchain instead of just using one or another;
"""




# load API keys and constants
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'YourAPIKey')
DOCS_PATH = os.path.join(os.path.dirname(__file__), f"documentations")

# construct models - embekdding and language models
embeddings = OpenAIEmbeddings(disallowed_special=(), openai_api_key=OPENAI_API_KEY)
llm = ChatOpenAI(temperature=0.5, model_name='gpt-3.5-turbo', openai_api_key=OPENAI_API_KEY, model="gpt-3.5-turbo")




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
    return round((total_size / 1024 / 1024), 2)



def create_vectostore(target_directory, verbose=False):
    """
    create_vectostore(target_directory):
    - Creates a vectorstore containing of all of the relevant files and its embeddings
    - within the target directory and its sub directories by using os.walk() on the target_path
    - This creates a chroma_db within the /documentations/learn|target_directory/ path that contains the relevant embeddings.
    -- It also creates the learn|target_directory directory as well if it does not yet exist.

    Args:
    - target_directory - e.g. "thefuzz" this is a string name of the folder within documentations. 
                         The folder must be in documentations otherwise the function will raies an error.

        File format support:
            - File format wise the function currently, supports .txt and PDF
            - Supported filesize of directory is 50MB, anything larger should be broken up into smaller tasks:
            - You may also target sub directories within the target_directory, such as thefuzz/data/ or thefuzz/thefuzz, but you must turn on the subdir flag as True.
            -- subdir is something like thefuzz/thefuzz
            -- normal dir is something like thefuzz

    - is_subdir - default=False, use only when a sub directory is passed for example thefuzz/thefuzz

    Returns / Result:
    - Creates a localized chroma vectorstore
    - None

    -------    
    NOTE:
    If you define an embedding function in your Chroma object creation, 
    you do not need to create embeddings for the documents separately before adding them to the Chroma vector store.
    The embedding function specified in the Chroma object creation will handle the embedding process for you.

    This is why this current code works as it is.
    """
    # set the learning path
    target_path = os.path.join(DOCS_PATH, target_directory) # /thefuzz/data/examples/ -> it could be however long
    parent_directory = target_directory.split(os.path.sep)[0] # absolute parent dir, whether its a subdir or parent dir.
    learning_path = os.path.join(DOCS_PATH, f'learn|{parent_directory}') # /learnGPT/documentations/learn|thefuzz/
    chroma_path = os.path.join(learning_path, 'chroma_db') # /learnGPT/documentations/learn|thefuzz/chroma_db/

    # instantiate the database
    db = Chroma(persist_directory=chroma_path, embedding_function=embeddings, collection_name=f'{parent_directory}')

    # check the filesize of the database
    size = get_folder_size_MB(target_directory)
    # if the size is larger than 50, return and ask for sub directories to be added individually
    if size > 50:
        print(f"The directory is too big {size}MB, please target sub directories in this case.")
        return
    
    # walk the directory, split and load the documents, add it to the database / Chroma object (which itself already has the embedding functions)
    documents = []

    for dirpath, dirnames, filenames in os.walk(target_path):
        # Go through each file
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 2500,
            chunk_overlap  = 100,)

        for file in filenames:
            filetype = file.split(".")[1]
            if filetype.lower() == "pdf":
                try:
                    loader = PyPDFLoader(os.path.join(dirpath, file)) # this is a loader object
                    documents.extend(loader.load_and_split(text_splitter=text_splitter))
                    if verbose:
                        print(f"{file} has been added to vectostore")

                except Exception as e:
                    pass

            else:
                try:
                    # Load up the file as a doc and split
                    print(file)
                    loader = TextLoader(os.path.join(dirpath, file), encoding='utf-8')
                    documents.extend(loader.load_and_split(text_splitter=text_splitter))
                    if verbose:
                        print(f"{file} has been added to vectostore")

                except Exception as e: 
                    pass
            # more filetypes can be supported in the future, for example images.
    
    db.add_documents(documents)

    ## code snippet to calculate the last refreshed for future usage
    # timestamp = os.path.getmtime(target_path)
    # last_modified_date = datetime.datetime.fromtimestamp(timestamp)





def search_and_qa(target_directory, query, k=4, llm=llm, verbose=True):
    """
    search_and_qa(target_directory, query, llm):
    1. gets the vectorstore and loads it into a local variable
    2. run a docsearch on the vectorstore with the query;

    target_directory = library or directory of information to query against
    query = query to be sent to the LLM
    llm = LLM used, default is the chat model loaded

    result / returns:
    - 
    """
    # check the vectorstore path exists get the vectorstore, then construct the qa chain and retriever
    parent_directory = target_directory.split(os.path.sep)[0] # absolute parent dir, whether its a subdir or parent dir.
    learning_path = os.path.join(DOCS_PATH, f"learn|{parent_directory}")
    chroma_path = os.path.join(learning_path, 'chroma_db') # /learnGPT/documentations/learn|thefuzz/chroma_db/
    if not os.path.exists(chroma_path):
        print("VectorStore does not exist")
        return


    # TODO: add chat history here for context for chat model, especially for context and system message.

    db = Chroma(persist_directory=chroma_path, embedding_function=embeddings, collection_name=f'{parent_directory}') # See NOTE.
    retrieved_docs = db.similarity_search(query=query, k=k)

    if verbose:
        print(query)
        for document in retrieved_docs:
            print("----document start-----")
            print(document.page_content)
            print("----doucment end-----")

    qa_chain = load_qa_chain(llm, chain_type="stuff", verbose=True)
    result = qa_chain.run(question=query, input_documents=retrieved_docs)
    
    ## alternative approach using qa_chain
    # retriever = db.as_retriever()
    # qa_chain = RetrievalQA.from_chain_type(llm, retriever=retriever, verbose=True)


    # log the chat into the relevant directory

    return result



def log_chat(learning_path, query, chat_response):
    """
    log_chat(learning_path, query, chat_response):
    - log_chat stores the relevant chat history in the passed target directory along with other metadata

    Data formatfor example:{
        "time": datetime,
        "documents_matched": [Documents*],
        "chat":[
            SystemMessage(content="You are a nice AI bot that helps a user figure out where to travel in one short sentence"),
            HumanMessage(content="I like the beaches where should I go?"),
            AIMessage(content="You should go to Nice, France")],
        }

    resutls:
    - returns -> None
    - creates -> Writes to existing
    """
    # construct the json dump for this current conversation
    ## gather and parse the relevant information
    current_time = datetime.datetime.now()

    ## construct the logging string with pretty formatting:
    data = {str(current_time): {"Human_Message": query, "AI_message": chat_response}}


    # create the log_path
    formatted_time = datetime.datetime.now().strftime("%Y-%m")
    log_path = os.path.join(learning_path, f"chat_history{os.path.sep}{formatted_time}.json")
    




    












# testing with __main__ entry:
if __name__ == "__main__":
    # target directory is another way of saying target library that is contained within the learnGPT library:

    test_target_directory_to_learn = "PDF_test"
    # test_target_path = os.path.join(DOCS_PATH, test_target_directory_to_learn)
    # create_vectostore(test_target_directory_to_learn) # if testing for subdir, remember to put True as arg2
    q1 = "Can you give me a few real world examples and usecases of thefuzz? Along with code examples"
    q2 = "Give me an overview of each of the chapters in the book."
    result = search_and_qa(test_target_directory_to_learn, q2)
    print(result)
