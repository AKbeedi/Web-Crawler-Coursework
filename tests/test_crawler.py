from src.crawler import extract_page_text
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

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