import json
import urllib.parse
import urllib.request

titles = {
    "tehran": "تهران",
    "hafez": "حافظ",
    "ferdowsi": "فردوسی",
    "ai": "هوش مصنوعی",
    "isfahan": "اصفهان",
}

for name, title in titles.items():
    params = urllib.parse.urlencode({
        "action": "query",
        "prop": "extracts",
        "explaintext": 1,
        "redirects": 1,
        "format": "json",
        "titles": title,
    })
    url = "https://fa.wikipedia.org/w/api.php?" + params
    req = urllib.request.Request(url, headers={"User-Agent": "persian-rag-learning/0.1"})
    data = json.load(urllib.request.urlopen(req))
    page = next(iter(data["query"]["pages"].values()))
    text = page.get("extract", "")
    with open(f"data/{name}.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(name, len(text))