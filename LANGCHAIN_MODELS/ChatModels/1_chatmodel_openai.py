from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
model = ChatOpenAI(model = 'gpt-4',temperature=1.8,max_completion_tokens=10) # temperature is the parameter which is used to control the randomness of a language model output # 0.0 - 0.3 - factual answer (0.5-.0.7) - balanced answer high level above 1 
# max_completion_token is something how many nted to show
result = model.invoke("What is the Capital of India? ")
print(result.content)


