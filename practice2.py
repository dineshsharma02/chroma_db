import chromadb
from chromadb.config import Settings
client = chromadb.Client()
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(name = "my_collection")

collection.add(
    documents=[
        "The sun rises in the east.",
        "Cats are great pets",
        "Python is a versatile programming language"
    ],
    ids=[
        "doc1",
        "doc2",
        "doc3"
    ],
    metadatas=[
        {"topic":"nature"},
        {"topic":"animals"},
        {"topic":"technology"}
    ]
)

result = collection.get(ids=["doc1"])
client.delete_collection(name="my_collection")
print(result)