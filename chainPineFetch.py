#fetch data

import openai
import pinecone
from dotenv import load_dotenv
import os

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.document_loaders import TextLoader


load_dotenv()
pine_API_KEY = os.getenv("PINECONE_API_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")

embeddings = OpenAIEmbeddings()

loader = TextLoader("postTranscript/motivation.txt")
documents = loader.load()

pinecone.init(
        api_key=pine_API_KEY,
        environment="asia-southeast1-gcp-free"
    )
index = pinecone.Index('huberman-bot')

docsearch = Pinecone.from_existing_index('huberman-bot', embeddings)

# if you already have an index, you can load it like this
# docsearch = Pinecone.from_existing_index(index_name, embeddings)

query = "What is the best steps i can take to get more motivation?"
docs = docsearch.similarity_search(query)

print(docs[0].page_content)