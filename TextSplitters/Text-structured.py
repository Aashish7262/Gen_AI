from langchain.text_splitter import TextSplitter
from langchain.document_loaders import PyPDFLoader
text = "My Name is John Doe. I am a software engineer. I love programming and solving problems."
loader = PyPDFLoader("TextSplitters/sample.pdf")
documents = loader.load()
class CustomTextSplitter(TextSplitter):
    def split_text(self, text: str) -> list[str]:
        sentences = text.split('. ')
        return sentences
text_splitter = CustomTextSplitter()
chunks = text_splitter.split_text(documents[0].page_content)
print(chunks)