import chromadb
from chromadb.utils.embedding_functions import EmbeddingFunction
from sentence_transformers import SentenceTransformer

# Step 1: Define a proper embedding class
class SentenceTransformerEmbeddingFunction(EmbeddingFunction):
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def __call__(self, input):
        return self.model.encode(input).tolist()

# Step 2: Create client and use this
embedding_fn = SentenceTransformerEmbeddingFunction()

client = chromadb.Client()
collection = client.get_or_create_collection(
    name="custom_embeddings",
    embedding_function=embedding_fn
)

# Step 3: Add & query
collection.add(
    documents=["I love pizza", "I enjoy machine learning", "Deep learning is fun"],
    ids=["doc1", "doc2", "doc3"]
)

results = collection.query(query_texts=["AI is amazing"], n_results=2)
print(results)
