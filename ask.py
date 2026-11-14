import sys

import chromadb
import ollama

client = chromadb.PersistentClient(path="db")
collection = client.get_collection("persian")


def ask(question):
    emb = ollama.embed(model="bge-m3", input=[question])["embeddings"]
    result = collection.query(query_embeddings=emb, n_results=4)
    context = "\n\n".join(result["documents"][0])
    prompt = (
        "فقط با توجه به متن زیر به سوال جواب بده. "
        "اگه جواب توی متن نیست بگو «در متن پیدا نشد». "
        "جواب رو کوتاه و به فارسی بنویس.\n\n"
        f"متن:\n{context}\n\nسوال: {question}"
    )
    response = ollama.chat(
        model="llama3.2:3b",
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": 0},
    )
    return response["message"]["content"]


if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else "حافظ در چه شهری به دنیا آمد؟"
    print(ask(q))