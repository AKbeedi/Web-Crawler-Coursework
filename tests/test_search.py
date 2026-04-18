from src.search import find_pages, print_word
from src.indexer import build_index
from src.search import find_pages
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

def mock_index():
    return {
        "hello": {
            "page1": {"frequency": 2, "positions": [0, 2]}
        },
        "world": {
            "page1": {"frequency": 1, "positions": [1]},
            "page2": {"frequency": 1, "positions": [0]}
        }
    }


def test_print_word_exists():
    index = mock_index()
    result = print_word(index, "hello")

    assert "page1" in result


def test_print_word_not_exists():
    index = mock_index()
    result = print_word(index, "unknown")

    assert result == {}


def test_find_single_word():
    index = mock_index()
    results = find_pages(index, "world")

    assert len(results) == 2


def test_find_multiple_words():
    index = mock_index()
    results = find_pages(index, "hello world")

    assert len(results) == 1
    assert results[0]["url"] == "page1"


def test_find_no_results():
    index = mock_index()
    results = find_pages(index, "hello unknown")

    assert results == []


def test_find_empty_query():
    index = mock_index()
    results = find_pages(index, "")

    assert results == []

def test_find_results_sorted_by_score():
    index = {
        "hello": {
            "page1": {"frequency": 3, "positions": [0, 1, 2]},
            "page2": {"frequency": 1, "positions": [0]},
        },
        "world": {
            "page1": {"frequency": 1, "positions": [3]},
            "page2": {"frequency": 1, "positions": [1]},
        },
    }

    results = find_pages(index, "hello world")

    assert results[0]["url"] == "page1"
    assert results[0]["score"] >= results[1]["score"]


def test_full_pipeline():
    pages = [
        {"url": "page1", "text": "hello world"},
        {"url": "page2", "text": "world only"}
    ]

    index = build_index(pages)
    results = find_pages(index, "hello")

    assert len(results) == 1
    assert results[0]["url"] == "page1"