from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    google_api_key="AIzaSyBCQEQRT-ETQmNtdXik9fEm236WB3i1440"
)
prompt = PromptTemplate(
    template = 'Write a poem obout {topic}',
    input_variables = ['topic']
)

loader = TextLoader("LANGCHAIN-DOCUMENT-LOADERS/cricket.txt")
docs = loader.load()
print(docs[0])
print(docs[0].metadata)
print(docs[0].page_content)

chain = prompt | model | StrOutputParser()
result = chain.invoke({'topic': docs[0].page_content})
print(result)