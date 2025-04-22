import chromadb
from chromadb.utils.embedding_functions import EmbeddingFunction
from sentence_transformers import SentenceTransformer


class SentenceTransformerEmbeddingFunction(EmbeddingFunction):
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
    
    def __call__(self, input):
        return self.model.encode(input).tolist()
    

embedding_fn = SentenceTransformerEmbeddingFunction()

client = chromadb.HttpClient(host = "localhost",port = 8000)

collection = client.get_or_create_collection(
    name="server_embeddings",
    embedding_function = embedding_fn
)

collection.add(
    documents=["Chroma is now running as a service!", "Client-server mode is scalable"],
    ids=["s1", "s2"]
)

# Query
results = collection.query(query_texts=["scalable storage"], n_results=2)
print(results)