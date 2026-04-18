import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


BASE_URL = "https://quotes.toscrape.com/"


def fetch_page(url: str) -> str | None:

    """
    Fetch the HTML content of a given URL.

    Sends an HTTP GET request and returns the page content as text.

    Args:
        url: The URL of the page to fetch.

    Returns:
        The HTML content of the page as a string.

    Raises:
        requests.RequestException: If the request fails.
    """
    print(f"Fetching: {url}")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Failed to fetch {url}: {e}")
        return None


def extract_page_text(html: str) -> str:
    """
    Extract relevant text content from a page.

    Parses the HTML and extracts:
    - quote text
    - author names
    - tags

    Args:
        html: Raw HTML content of the page.

    Returns:
        A single string containing all extracted text.
    """
    soup = BeautifulSoup(html, "html.parser")

    quotes = soup.select(".quote")
    parts = []

    for quote in quotes:
        text_el = quote.select_one(".text")
        author_el = quote.select_one(".author")
        tag_els = quote.select(".tags .tag")

        if text_el:
            parts.append(text_el.get_text(" ", strip=True))
        if author_el:
            parts.append(author_el.get_text(" ", strip=True))
        for tag in tag_els:
            parts.append(tag.get_text(" ", strip=True))

    return " ".join(parts)


def find_next_page(html: str, current_url: str) -> str | None:
    """
    Find the URL of the next page using pagination.

    Looks for the 'Next' button in the page and constructs
    the absolute URL of the next page.

    Args:
        html: Raw HTML content of the current page.
        current_url: The URL of the current page.

    Returns:
        The absolute URL of the next page, or None if no next page exists.
    """
    soup = BeautifulSoup(html, "html.parser")
    next_link = soup.select_one("li.next a")
    if not next_link:
        return None
    href = next_link.get("href")
    return urljoin(current_url, href)


def crawl_site(start_url: str = BASE_URL, delay_seconds: int = 6) -> list[dict]:
    """
    Crawl the target website and collect page data.

    Visits pages sequentially using pagination, extracts text content,
    and respects a politeness delay between requests.

    Args:
        start_url: The URL to start crawling from.
        delay_seconds: Delay between requests to respect politeness.

    Returns:
        A list of dictionaries containing:
        - 'url': the page URL
        - 'text': extracted text content
    """
    pages = []
    visited = set()
    current_url = start_url

    while current_url and current_url not in visited:
        html = fetch_page(current_url)
        if html is None:
            break
        text = extract_page_text(html)

        pages.append({
            "url": current_url,
            "text": text,
        })

        visited.add(current_url)
        next_url = find_next_page(html, current_url)

        if next_url and next_url not in visited:
            unit = "second" if delay_seconds == 1 else "seconds"
            print(f"Sleeping {delay_seconds} {unit}...")
            time.sleep(delay_seconds)

        current_url = next_url

    return pages