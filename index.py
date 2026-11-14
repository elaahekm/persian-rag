import os

import chromadb
import ollama
from chunk import chunk_text

client = chromadb.PersistentClient(path="db")
try:
    client.delete_collection("persian")
except Exception:
    pass
collection = client.create_collection("persian")

for filename in sorted(os.listdir("data")):
    with open(f"data/{filename}", encoding="utf-8") as f:
        chunks = chunk_text(f.read())
    for i in range(0, len(chunks), 20):
        batch = chunks[i:i + 20]
        result = ollama.embed(model="bge-m3", input=batch)
        collection.add(
            ids=[f"{filename}-{i + j}" for j in range(len(batch))],
            documents=batch,
            embeddings=result["embeddings"],
            metadatas=[{"source": filename}] * len(batch),
        )
    print(filename, len(chunks))

print("count", collection.count())