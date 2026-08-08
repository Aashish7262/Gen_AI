from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    temperature=1.5,
    max_new_tokens=100
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the Capital of India?")
print(result.content)
