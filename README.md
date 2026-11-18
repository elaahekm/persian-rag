# persian-rag

A local Persian RAG (retrieval-augmented generation) system. Ask a question in Persian, get an answer based only on Persian Wikipedia texts. Runs fully offline with Ollama.

## How it works

1. `download.py` downloads 5 Persian Wikipedia articles into `data/`
2. `chunk.py` splits the texts into 300-character chunks with 60 overlap
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

Current score: 8/10 on a small keyword-based test set.

Known weaknesses:
- The Isfahan nickname question fails because retrieval misses the right chunk.
- The question "When did Ferdowsi die?" fails because the answer is not found in the retrieved chunks.
- Keyword matching is lenient: an answer can contain the right word and still be partly wrong.

## Decisions

- **Temperature 0:** results were random between runs, so evaluation was not reliable. Temperature 0 makes answers repeatable.
- **4 retrieved chunks:** with 3, the right chunk was often missing. With 6, the small 3B model got confused and said "not found". 4 worked best in my tests.
- **bge-m3:** a multilingual embedding model that handles Persian well.

## API

```
uvicorn api:app --port 8000
curl -X POST http://127.0.0.1:8000/ask -H "Content-Type: application/json" -d '{"question": "حافظ در کدام شهر زندگی کرد؟"}'
```

Endpoints: `GET /health` and `POST /ask`.

## Docker

Run `python index.py` once first (the `db/` folder is not in git). Ollama must be running on the host.

```
docker build -t persian-rag .
docker run --rm -p 8000:8000 persian-rag
```

The container reaches Ollama on the host through `host.docker.internal`.

## Next

Better retrieval (the Isfahan question), a stricter evaluation than keyword matching, and more texts.