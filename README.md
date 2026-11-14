# persian-rag

A local Persian RAG (retrieval-augmented generation) system. Ask a question in Persian, get an answer based only on Persian Wikipedia texts. Runs fully offline with Ollama.

## How it works

1. `download.py` downloads 5 Persian Wikipedia articles into `data/`
2. `chunk.py` splits the texts into 500-character chunks with 100 overlap
3. `index.py` embeds the chunks with `bge-m3` and stores them in ChromaDB
4. `ask.py` retrieves the 4 closest chunks and answers with `llama3.2:3b`
5. `eval.py` runs 5 test questions and checks for an expected keyword

## Run

```
pip install ollama chromadb
ollama pull llama3.2:3b
ollama pull bge-m3
python download.py
python index.py
python ask.py "حافظ در چه قرنی زندگی می‌کرد؟"
python eval.py
```

## Evaluation

Current score: 4/5 on a small keyword-based test set.

Known weaknesses:
- The Isfahan nickname question fails because retrieval misses the right chunk.
- Keyword matching is lenient: an answer can contain the right word and still be partly wrong.

## Decisions

- **Temperature 0:** results were random between runs, so evaluation was not reliable. Temperature 0 makes answers repeatable.
- **4 retrieved chunks:** with 3, the right chunk was often missing. With 6, the small 3B model got confused and said "not found". 4 worked best in my tests.
- **bge-m3:** a multilingual embedding model that handles Persian well.

## Next

Unit tests, ruff, GitHub Actions, FastAPI, Docker.