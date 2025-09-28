from langchain_openai import OpenAI #integration of langchain with openai
from dotenv import load_dotenv #to load environment variables from a .env file

load_dotenv() # Load environment variables from .env file

# llm = OpenAI(model='gpt-3.5-turbo-instruct')  # Initialize the OpenAI LLM with the specified model

result = llm.invoke("What is the capital of India") # Invoke the LLM with a prompt

print(result)