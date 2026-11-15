import os


def chunk_text(text, size=300, overlap=60):
    chunks = []
    start = 0
    while start < len(text):
        piece = text[start:start + size].strip()
        if piece:
            chunks.append(piece)
        start += size - overlap
    return chunks


if __name__ == "__main__":
    for filename in sorted(os.listdir("data")):
        with open(f"data/{filename}", encoding="utf-8") as f:
            text = f.read()
        chunks = chunk_text(text)
        print(filename, len(chunks))