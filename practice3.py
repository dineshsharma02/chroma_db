import chromadb

client = chromadb.Client()
client = chromadb.PersistentClient(path = "./chroma_db")


collection = client.get_or_create_collection(name = "mycollection")



collection.add(
    documents=[
        "The quick brown fox jumps over the lazy dog.",
        "ChromaDB is great for vector-based search.",
        "Artificial intelligence is transforming industries."
    ],
    ids=["doc_1", "doc_2", "doc_3"],
    metadatas=[
        {"language": "en", "category": "animals"},
        {"language": "en", "category": "technology"},
        {"language": "en", "category": "ai"}
    ]
)



# gives top 2 results of below query
query = "What is ChromaDB?"
result = collection.query(query_texts=[query],n_results=2)
# print(result)


# filters with metadata also
query = "What is AI?"

result = collection.query(
    query_texts=[query],
    n_results=2,
    where={"category": "ai"}
)




query = "What is AI?"
result = collection.query(
    query_texts=[query], 
    n_results=2, 
    include=["metadatas", "distances"]
)

print(result)



# print(result)