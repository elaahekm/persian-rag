import chromadb
import ollama

client = chromadb.PersistentClient(path="db")
collection = client.get_collection("persian")

question = "اصفهان به چه لقبی معروف است؟"
emb = ollama.embed(model="bge-m3", input=[question])["embeddings"]
result = collection.query(query_embeddings=emb, n_results=3)

for doc, meta in zip(result["documents"][0], result["metadatas"][0]):
    print("---", meta["source"])
    print(doc)