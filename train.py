from gpt_index import SimpleDirectoryReader, GPTListIndex, GPTSimpleVectorIndex, LLMPredictor, PromptHelper, ServiceContext
from langchain import OpenAI
import sys
import os
os.environ["OPENAI_API_KEY"] = "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"


def create_index(path):
    max_input = 4096
    tokens = 200
    chunk_size = 600  # for LLM, we need to define chunk size
    max_chunk_overlap = 20

    # define prompt
    prompt_helper = PromptHelper(
        max_input, tokens, max_chunk_overlap, chunk_size_limit=chunk_size)

    # define LLM — there could be many models we can use, but in this example, let’s go with OpenAI model
    llm_predictor = LLMPredictor(llm=OpenAI(
        temperature=0, model_name="text-ada-001", max_tokens=tokens))

    # load data — it will take all the .txtx files, if there are more than 1
    docs = SimpleDirectoryReader(path).load_data()

    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)
    
    # create vector index
    vector_index = GPTSimpleVectorIndex.from_documents(
        documents=docs, service_context=service_context)
    vector_index.save_to_disk('vector_index.json')
    return vector_index


vector_index = create_index('./data/')
