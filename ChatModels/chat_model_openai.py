from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=10) #temperature is for creativity, max_completion_tokens is for length of response

result = model.invoke("Write a 5 line poem on cricket")

print(result.content)