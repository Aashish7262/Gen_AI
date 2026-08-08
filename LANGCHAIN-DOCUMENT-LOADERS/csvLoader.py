from langchain_community.document_loaders import CSVLoader

loader = CSVLoader("LANGCHAIN-DOCUMENT-LOADERS/c.csv")
docs = loader.load()
print(docs)
