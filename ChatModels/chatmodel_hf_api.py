# through api call
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
) # You can change the model here, but make sure it is a chat model


model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")

print(result.content)






