from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation",
    temperature=0.7,
    max_new_tokens=512
)

model = ChatHuggingFace(llm=llm)
parser = JsonOutputParser()

template1 = PromptTemplate(
    template='Give me 5 facts obout {topic}\n {format_instruction}',
    input_variables=['topic'],
    partial_variables = {'format_instruction':parser.get_format_instructions()}
)
prompt = template1.invoke({'topic':'black-hole'})

result = model.invoke(prompt)
final_result = parser.parse(result.content)
print(final_result)
print(type(final_result))