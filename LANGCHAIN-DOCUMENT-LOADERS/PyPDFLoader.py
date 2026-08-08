## it is a document Loader in Langchain which is used to Load the PDF files and extract the text from it. It uses the PyPDF2 library to extract the text from the PDF files.
# it is extract the text from the PDF files and return it as a string. It also returns the metadata of the PDF file such as the title, author, and number of pages. or in the form of a list of documents. Each document is a dictionary that contains the text and metadata of the PDF file.
from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader("LANGCHAIN-DOCUMENT-LOADERS/sample.pdf")
docs = loader.load()
print(docs[0])
print(docs[0].metadata)
print(docs[0].page_content)
