from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate


load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation",
    temperature=0.7,
    max_new_tokens=512
)

model = ChatHuggingFace(llm=llm)


template1 = PromptTemplate(
    template='Write a detailed report on the topic: {topic}',
    input_variables=['topic']
)


template2 = PromptTemplate(
    template='Write a 5 line summary of the following text:\n{text}',
    input_variables=['text']
)


prompt1 = template1.invoke({'topic': 'black hole'})
result1 = model.invoke(prompt1)


prompt2 = template2.invoke({'text': result1.content})
result2 = model.invoke(prompt2)


print("----- REPORT -----")
print(result1.content)

print("\n----- SUMMARY -----")
print(result2.content)