# goal learn CRUD in chroma

import chromadb
from chromadb.config import Settings
client = chromadb.Client()
client = chromadb.PersistentClient(path="./chroma_db")


collection = client.get_or_create_collection(name = "my_collection")


# CREATE
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

#READ
#By ID 
result1 = collection.get(ids=["doc1"])
#By metadata
result2 = collection.get(where={"topic":"nature"})
#By semantic similarity
result3 = collection.query(query_texts=["pets"],n_results=1)




#UPDATE 


collection.upsert(
    documents=["Cats are lovely companions"],
    ids=["doc2"],
    metadatas=[{"topic": "pets"}]
)



#DELETE

# Delete specific doc
collection.delete(ids=["doc3"])

# Delete by metadata
collection.delete(where={"topic": "technology"})

# OR delete entire collection
client.delete_collection(name="my_collection")



# print(result1)
# print(result2)
print(result3)