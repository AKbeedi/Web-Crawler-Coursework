from math import log
from indexer import tokenize


def print_word(index: dict, word: str) -> dict:
    tokens = tokenize(word)
    if not tokens:
        return {}
    return index.get(tokens[0], {})


def find_pages(index: dict, query: str) -> list[dict]:
    words = tokenize(query)

    if not words:
        return []

    if any(word not in index for word in words):
        return []

    page_sets = [set(index[word].keys()) for word in words]
    matching_pages = set.intersection(*page_sets)

    # total number of unique pages in the whole index
    all_pages = set()
    for postings in index.values():
        all_pages.update(postings.keys())
    total_docs = len(all_pages)

    results = []
    for page in matching_pages:
        score = 0.0
        matches = {}

        for word in words:
            posting = index[word][page]
            tf = posting["frequency"]
            df = len(index[word])  # how many pages contain this word

            # simple TF-IDF-like score
            idf = log((total_docs + 1) / (df + 1)) + 1
            score += tf * idf

            matches[word] = posting

        results.append({
            "url": page,
            "score": round(score, 3),
            "matches": matches
        })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results