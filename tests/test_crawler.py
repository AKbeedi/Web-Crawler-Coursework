import os
import sys
from unittest.mock import patch

import requests

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from src.crawler import extract_page_text, fetch_page, find_next_page


def test_extract_page_text_basic():
    html = """
    <div class="quote">
        <span class="text">Test quote</span>
        <small class="author">Author</small>
        <div class="tags">
            <a class="tag">life</a>
        </div>
    </div>
    """

    text = extract_page_text(html)

    assert "Test quote" in text
    assert "Author" in text
    assert "life" in text


def test_find_next_page():
    html = """
    <li class="next">
        <a href="/page/2/">Next</a>
    </li>
    """

    next_page = find_next_page(html, "https://quotes.toscrape.com/page/1/")

    assert next_page == "https://quotes.toscrape.com/page/2/"


@patch("src.crawler.requests.get")
def test_fetch_page_success(mock_get):
    mock_response = mock_get.return_value
    mock_response.text = "<html>OK</html>"
    mock_response.raise_for_status.return_value = None

    result = fetch_page("https://example.com")

    assert result == "<html>OK</html>"


@patch("src.crawler.requests.get")
def test_fetch_page_failure(mock_get):
    mock_get.side_effect = requests.RequestException("Network error")

    result = fetch_page("https://example.com")

    assert result is None