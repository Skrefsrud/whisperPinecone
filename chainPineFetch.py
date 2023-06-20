#fetch data

import openai
import pinecone
from dotenv import load_dotenv
import os

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.document_loaders import TextLoader
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain




load_dotenv()
pine_API_KEY = os.getenv("PINECONE_API_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")

embeddings = OpenAIEmbeddings(model="ada")

pinecone.init(
    api_key=pine_API_KEY,
    environment="asia-southeast1-gcp-free"
)

index_name = "huberman-test"

index = Pinecone.from_existing_index(index_name, embeddings)

def get_similiar_docs(query, k=2, score=False):
  if score:
    similar_docs = index.similarity_search_with_score(query, k=k)
  else:
    similar_docs = index.similarity_search(query, k=k)
  return similar_docs

model_name = "text-davinci-003"
# model_name = "gpt-3.5-turbo"
#model_name = "gpt-4"
llm = OpenAI(model_name=model_name)

chain = load_qa_chain(llm, chain_type="stuff")

def get_answer(query):
  similar_docs = get_similiar_docs(query)
  answer = chain.run(input_documents=similar_docs, question=query)
  return answer

query = "How do I loose weight?"
answer = get_answer(query)
print(answer)