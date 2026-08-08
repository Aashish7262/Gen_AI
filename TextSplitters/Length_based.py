from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import PyPDFLoader 

loader = PyPDFLoader("TextSplitters/sample.pdf") 
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=50, chunk_overlap=8)
chunks = text_splitter.split_text(documents[0].page_content)
print(chunks)