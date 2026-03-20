import json
import re


def tokenize(text: str) -> list[str]:
    return re.findall(r"\b\w+\b", text.lower())


def build_index(pages: list[dict]) -> dict:
    index = {}

    for page in pages:
        url = page["url"]
        words = tokenize(page["text"])

        for position, word in enumerate(words):
            if word not in index:
                index[word] = {}

            if url not in index[word]:
                index[word][url] = {
                    "frequency": 0,
                    "positions": []
                }

            index[word][url]["frequency"] += 1
            index[word][url]["positions"].append(position)

    return index


def save_index(index: dict, filepath: str):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2)


def load_index(filepath: str) -> dict:
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)