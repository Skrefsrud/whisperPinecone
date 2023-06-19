from langchain.text_splitter import RecursiveCharacterTextSplitter
import pandas as pd
from langchain import OpenAI
import openai
from dotenv import load_dotenv
from langchain.vectorstores.pinecone import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone
import os
from datasets import load_dataset
import random
import itertools
#import streamlit as st, pinecone

load_dotenv()
pine_API_KEY = os.getenv("PINECONE_API_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")

#check for auntentication
openai.Engine.list()


def textChunking(text):
    text_splitter = RecursiveCharacterTextSplitter(  
        separators = ['\n\n', '\n', ' ', ''],      
        chunk_size = 400,
        chunk_overlap  = 20,
        length_function = len,
)
    chunks = text_splitter.split_text([text])
    return chunks

    
def createEmbedding(chunks):
    MODEL = "text-embedding-ada-002"
    
    response = openai.Embedding.create(
    input=chunks,
    engine=MODEL
)
    
    # extract embeddings to a list
    embeds = [record['embedding'] for record in response['data']]
    
    
    # initialize connection to pinecone (get API key at app.pinecone.io)
    pinecone.init(
        api_key=pine_API_KEY,
        environment="asia-southeast1-gcp-free"
    )
    index = pinecone.Index('huberman-bot')
    i = 0
    for x in chunks:
        index.upsert(vectors=[{f'id': 'vec{i}', 'values': embeds[i], 'metadata':{'topic': 'motivation'}}])
    
    
    
  



if __name__ == "__main__":
    with open('postTranscript/motivation.txt') as f:
        text = f.read()
        
    chunks = textChunking(text)

    createEmbedding(chunks)



#st.subheader('Generative Q&A with LangChain & Pinecone')
#query = st.text_input("Enter your query")
#if st.button("Submit"):
    #print("hey")