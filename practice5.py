import chromadb
from chromadb.config import Settings
from chromadb.utils.embedding_functions import EmbeddingFunction
from sentence_transformers import SentenceTransformer

# Custom embedding class
class SentenceTransformerEmbeddingFunction(EmbeddingFunction):
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def __call__(self, input):
        return self.model.encode(input).tolist()

embedding_fn = SentenceTransformerEmbeddingFunction()

# Setup persistent Chroma client

client = chromadb.Client()
client = chromadb.PersistentClient(path="my_chroma_db")

collection = client.get_or_create_collection(name="persistent_collection", embedding_function=embedding_fn)

collection.add(
    documents=["Persistent vector stores are useful", "Chroma saves to disk"],
    ids=["p1", "p2"]
)

# Persist it to disk
print("✅ Collection saved to disk.")
