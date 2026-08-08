from  langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding = OpenAIEmbeddings(model = 'text-embedding-3-large',dimensions = 300)
documents = [
    "Delhi is the capital of India",
    "Paris is the capital of France",
    "AI stands for Artificial Intelligence"
]
query = 'tell me obout virat kohli'
doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_documents(query)
scores = cosine_similarity([query_embedding],doc_embeddings)[0]
index , score = sorted(list(enumerate(scores)),key = lambda x : x[1])[-1]
print(documents[index])
print('similarity score is : ',score)





