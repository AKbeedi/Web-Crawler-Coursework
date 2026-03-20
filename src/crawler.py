import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


BASE_URL = "https://quotes.toscrape.com/"


def fetch_page(url: str) -> str:
    print(f"Fetching: {url}")
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text


def extract_page_text(html: str) -> str:
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
    soup = BeautifulSoup(html, "html.parser")
    next_link = soup.select_one("li.next a")
    if not next_link:
        return None
    href = next_link.get("href")
    return urljoin(current_url, href)


def crawl_site(start_url: str = BASE_URL, delay_seconds: int = 6) -> list[dict]:
    pages = []
    visited = set()
    current_url = start_url

    while current_url and current_url not in visited:
        html = fetch_page(current_url)
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