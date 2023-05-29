import os 
import dotenv
import streamlit as st 
from rich.console import Console
from langchain.llms import Cohere
from langchain import PromptTemplate, LLMChain
from langchain import ConversationChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

# load dotenv
dotenv.load_dotenv()
# get the api key
key = os.getenv("COHERE_API_KEY")

# initiate the llm model 
llm = Cohere()
console = Console()

conversation = ConversationChain(llm=llm, verbose=False)

# itterate 

def _conversation(user_input):
    response = conversation.predict(input=user_input)
    return response
   
while True:
    user_input = input('User: ')
    print(_conversation(user_input))