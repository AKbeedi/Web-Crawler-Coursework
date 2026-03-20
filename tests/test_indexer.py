from src.indexer import tokenize, build_index
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

def test_tokenize_basic():
    text = "Hello, World!"
    tokens = tokenize(text)
    assert tokens == ["hello", "world"]


def test_build_index_frequency():
    pages = [
        {"url": "page1", "text": "hello hello world"}
    ]

    index = build_index(pages)

    assert index["hello"]["page1"]["frequency"] == 2
    assert index["world"]["page1"]["frequency"] == 1


def test_build_index_positions():
    pages = [
        {"url": "page1", "text": "a b a"}
    ]

    index = build_index(pages)

    assert index["a"]["page1"]["positions"] == [0, 2]