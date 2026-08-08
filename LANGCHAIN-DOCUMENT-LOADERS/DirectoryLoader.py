## It is the document loader used to load multiple documents from a directory. It uses the glob library to load all the files from the directory and return it as a list of documents. Each document is a dictionary that contains the text and metadata of the file. It also returns the metadata of the file such as the file name, file size, and file type.
from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader
loader = DirectoryLoader("LANGCHAIN-DOCUMENT-LOADERS/books", glob="*.pdf",loader_cls=PyPDFLoader)
docs = loader.load()
print(docs[0])
print(docs[0].metadata)
print(docs[0].page_content)
