from gpt_index import SimpleDirectoryReader, GPTListIndex, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain import OpenAI
import sys
import os
os.environ["OPENAI_API_KEY"] = ""

def answer_me(vector_index):
    v_index = GPTSimpleVectorIndex.load_from_disk(vector_index)
    while True:
        user_input = input('Please ask: ')
        response = v_index.query(user_input, response_mode='compact')
        print(f'Response: {response} \n')


answer_me('vector_index.json')
