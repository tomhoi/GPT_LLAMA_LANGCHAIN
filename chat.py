from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain.chat_models import ChatOpenAI
import os

# path to index.json
path_to_index_json = "D:\Documents_D\GitHub\GPT_LLAMA_LANGCHAIN\index.json"

# bot_name
bot_name = "TestBot"

index = GPTSimpleVectorIndex.load_from_disk(path_to_index_json)

def get_response(msg):
    response = index.query(msg, response_mode = "compact")
    return response
