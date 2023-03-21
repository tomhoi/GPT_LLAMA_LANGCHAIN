# Importing 
from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain.chat_models import ChatOpenAI
import os

# Set working directory
working_directory = 'D:\Documents_D\GitHub\GPT_LLAMA_LANGCHAIN'

# Function to generate index.json
def construct_index(directory_path):
    # set maximum input size
    max_input_size = 4096
    # set number of output tokens
    num_outputs = 256
    # set maximum chunk overlap
    max_chunk_overlap = 20
    # set chunk size limit
    chunk_size_limit = 600

    # define LLM (ChatGPT gpt-3.5-turbo)
    llm_predictor = LLMPredictor(llm = ChatOpenAI(temperature=0, 
                                              model_name = "gpt-3.5-turbo", 
                                              max_tokens = num_outputs))
    
    prompt_helper = PromptHelper(max_input_size, 
                                 num_outputs, 
                                 max_chunk_overlap, 
                                 chunk_size_limit = chunk_size_limit)
 
    documents = SimpleDirectoryReader(directory_path).load_data()
    
    index = GPTSimpleVectorIndex(
        documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper
        )

    index.save_to_disk(working_directory + '\index.json')

    return index


if __name__ == "__main__":
   # Generating index.json
   construct_index(working_directory + '\data')     