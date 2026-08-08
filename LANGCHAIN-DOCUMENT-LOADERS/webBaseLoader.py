## It is the document loader used to load documents from a web URL. It fetches the content from the URL and returns it as a list of documents. Each document is a dictionary that contains the text and metadata of the web page.
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://en.wikipedia.org/wiki/Cricket")

docs = loader.load()
print(docs[0])
print(docs[0].metadata)
print(docs[0].page_content)