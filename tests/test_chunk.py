from chunk import chunk_text


def test_chunks_are_not_longer_than_size():
    chunks = chunk_text("الف" * 1200, size=500, overlap=100)
    assert all(len(c) <= 500 for c in chunks)


def test_chunks_overlap():
    text = "".join(str(i % 10) for i in range(1000))
    chunks = chunk_text(text, size=500, overlap=100)
    assert chunks[0][-100:] == chunks[1][:100]


def test_empty_text_gives_no_chunks():
    assert chunk_text("") == []