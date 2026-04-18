import json
import re


def tokenize(text: str) -> list[str]:
    """
    Convert text into normalized tokens.

    Lowercases the text and removes punctuation using regex.

    Args:
        text: Input text.

    Returns:
        A list of cleaned word tokens.
    """
    return re.findall(r"\b\w+\b", text.lower())


def build_index(pages: list[dict]) -> dict:
    """
    Build an inverted index from crawled pages.

    Maps each word to the pages it appears in, storing:
    - frequency of occurrence
    - positions within the page

    Args:
        pages: List of page dictionaries with 'url' and 'text'.

    Returns:
        A dictionary representing the inverted index.
    """
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