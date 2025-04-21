import chromadb
client = chromadb.Client()
collection = client.create_collection(name="test")
collection.add(documents=["Hello world", "How are you?"], ids=["1", "2"])
results = collection.query(query_texts=["Hello"], n_results=1)
print(results)
