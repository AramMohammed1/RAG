import chromadb

client = chromadb.PersistentClient(path="/chromaDBPresistent")

collection = client.get_or_create_collection(name="test") 


collection.add(
    documents=["doc1", "doc2", "doc3"],
    ids=["id1", "id2", "id3"]
)


ans = collection.query(
    query_texts=["doc1"],
    n_results=3
)



print(ans)