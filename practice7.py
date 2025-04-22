from dotenv import load_dotenv
import os

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain.chains import RetrievalQA

load_dotenv()
open_ai_api_key = os.getenv("OPENAI_API_KEY")

text = """
ChromaDB is an open-source vector database optimized for local-first, embedded, and cloud-native applications.
It supports fast similarity search, metadata filtering, and can be used with popular models like OpenAI and Sentence Transformers.
"""

splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=10)
docs = splitter.create_documents([text])

embedding = OpenAIEmbeddings(openai_api_key=open_ai_api_key)

db = Chroma.from_documents(docs, embedding, persist_directory="./rag_db")

qa_chain = RetrievalQA.from_chain_type(
    llm=OpenAI(openai_api_key=open_ai_api_key),
    retriever=db.as_retriever(),
    chain_type="stuff"
)

query = "What is chromadb used for?"
response = qa_chain.invoke(query)
print(response)
