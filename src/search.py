def print_word(index: dict, word: str) -> dict:
    return index.get(word.lower(), {})


def find_pages(index: dict, query: str) -> list[dict]:
    words = [w.lower() for w in query.split() if w.strip()]

    if not words:
        return []

    if any(word not in index for word in words):
        return []

    page_sets = [set(index[word].keys()) for word in words]
    matching_pages = set.intersection(*page_sets)

    results = []
    for page in matching_pages:
        score = sum(index[word][page]["frequency"] for word in words)
        results.append({
            "url": page,
            "score": score,
            "matches": {
                word: index[word][page]
                for word in words
            }
        })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results