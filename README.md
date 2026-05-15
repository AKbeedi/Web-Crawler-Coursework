# Search Engine Tool (COMP3011 Coursework 2)

## Overview
This project implements a simple search engine that crawls a website, builds an inverted index, and allows users to search for words or phrases using a command-line interface.

The system consists of three main components:
1. Web crawler
2. Inverted index builder
3. Search and query processor

The target website used is:
https://quotes.toscrape.com/

---

## Features

- Web crawler with politeness delay
- Inverted index storing:
  - word frequency
  - word positions
- Command-line interface with the following commands:
  - `build` – crawl the website and build the index
  - `load` – load a previously saved index
  - `print <word>` – display index entries for a word
  - `find <query>` – search for pages containing query terms
- TF-IDF-style ranking for search results
- Unit and integration tests covering core functionality and edge cases

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/AKbeedi/Web-Crawler-Coursework.git
cd Web-Crawler-Coursework
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

Run the application:

```bash
python src/main.py
```

### Commands

Build the index:

```text
> build
```

Load the index:

```text
> load
```

Print a word entry:

```text
> print life
```

Search for pages:

```text
> find good friends
```

---

## Search Algorithm

The system uses an inverted index mapping words to pages.

Each word stores:

- frequency of occurrence in each page
- positions within the page

Search results are ranked using a TF-IDF-style scoring approach:

- Term Frequency (TF): number of times a word appears in a page
- Inverse Document Frequency (IDF): reduces weight of common words across many pages

This improves the relevance of returned results.

---

## Testing

Run tests and coverage reporting using:

```bash
python -m pytest --cov=src --cov-report=term-missing
```

The test suite achieves approximately 79% coverage across the core logic modules.

Tests include:

- HTML extraction and pagination handling
- mocked HTTP request success/failure cases
- tokenization and case-insensitive processing
- index construction (frequency and positions)
- search functionality (single and multi-word queries)
- ranking behaviour
- edge cases (empty queries, missing terms)
- a simple full-pipeline integration test

---

## Design Decisions

### Inverted Index

An inverted index was chosen to allow efficient search by mapping words directly to the pages that contain them, avoiding full document scans.

A dictionary-of-dictionaries structure was used because dictionaries provide very fast lookup for both words and pages while also supporting storage of additional statistics such as frequency and positions.

### Tokenization

Text is:

- converted to lowercase
- stripped of punctuation using regex

This ensures consistent indexing and querying while making searches case-insensitive.

### Ranking

A TF-IDF-style scoring function is used to prioritise relevant pages over those containing very common terms.

### Crawler

The crawler:

- uses Requests for HTTP requests
- uses BeautifulSoup for HTML parsing
- follows pagination links
- enforces a politeness delay of at least 6 seconds between requests

The crawler is intentionally sequential rather than parallel to ensure the politeness requirement is respected.

---

## Limitations

- Only crawls a single website
- No parallel crawling (intentionally sequential for politeness)
- Basic query handling (no phrase search or boolean operators)
- Index stored as JSON (not optimised for very large-scale data)

---

## Future Improvements

- Phrase search support
- Boolean queries (AND, OR, NOT)
- More advanced ranking (full TF-IDF or BM25)
- Caching crawled pages
- Web-based interface instead of CLI

---

## Dependencies

- requests
- beautifulsoup4
- pytest
- pytest-cov

---

## GenAI Usage

Generative AI tools were used to assist with:

- planning and structuring the project
- understanding ranking and search concepts
- debugging and resolving errors
- improving code clarity and testing

All generated suggestions were critically reviewed, tested, and adapted to ensure full understanding of the implementation and compliance with the coursework requirements.

---