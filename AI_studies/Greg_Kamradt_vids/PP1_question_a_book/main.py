import os
from langchain.vectorstores import Chroma, Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import UnstructuredPDFLoader, OnlinePDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from dotenv import load_dotenv
import pinecone

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
PINECONE_API_ENV = os.getenv('PINECONE_API_ENV')



# load the PDF file, read it and split the texts
PDF_PATH = os.path.join(os.path.dirname(__file__), "field-guide-to-data-science.pdf")
loader = UnstructuredPDFLoader(PDF_PATH)

data = loader.load()
print(len(data)) # documents in your data
print(len(data[0].page_content)) # characters in document

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(data)
print(len(texts))

# Create embeddings of your documents
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

pinecone.init(
    api_key=PINECONE_API_KEY,
    environment=PINECONE_API_ENV
)
index_name = "langchain2"

docsearch = Pinecone.from_texts([t.page_content for t in texts], embeddings, index_name=index_name)

# Query those docs to get your answer;
llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)
chain = load_qa_chain(llm, chain_type='stuff')

query = "What are examples of good data science teams?"
docs = docsearch.similarity_search(query)

output = chain.run(input_documents=docs, question=query)

print(output)
