from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
model1 = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')
model2 = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')
prompt1 = PromptTemplate(
    template = 'Generate short and simple notes from the following text {text}',
    input_variables=['text']
)
prompt2 = PromptTemplate(
    template = 'Generate 5 short Question answer from the following text {text}',
    input_variables=['text']
)
prompt3 = PromptTemplate(
    template = 'Merge the provided inputs into single output {text1} 2 {text2}',
    input_variables=['text1','text2']
)
parser = StrOutputParser()
document = """
Artificial Intelligence (AI) is a branch of computer science that focuses on creating intelligent machines that can perform tasks that normally require human intelligence. These tasks include learning, reasoning, problem-solving, and decision-making. AI is widely used in healthcare, finance, education, and automation to improve efficiency and accuracy.
"""
chain1 = prompt1 | model1 | parser
output1 = chain1.invoke({'text':document})
chain2 = prompt2 | model2 | parser 
output2 = chain2.invoke({'text':document})
chain3 = prompt3 | model1 | parser
result = chain3.invoke({'text1':output1,'text2':output2})
print(result)