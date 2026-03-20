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
- Unit tests covering core functionality and edge cases

---

## Installation

### 1. Clone the repository
```bash
git clone <your-repo-link>
cd <your-repo-name>
````

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

```
> build
```

Load the index:

```
> load
```

Print a word entry:

```
> print life
```

Search for pages:

```
> find good friends
```

---

## Search Algorithm

The system uses an inverted index mapping words to pages.

Each word stores:

* frequency of occurrence in each page
* positions within the page

Search results are ranked using a TF-IDF-style scoring approach:

* Term Frequency (TF): number of times a word appears in a page
* Inverse Document Frequency (IDF): reduces weight of common words across many pages

This improves the relevance of returned results.

---

## Testing

Run tests using:

```bash
python -m pytest
```

Tests include:

* tokenization correctness
* index construction (frequency and positions)
* search functionality (single and multi-word queries)
* edge cases (empty queries, missing terms)

---

## Design Decisions

### Inverted Index

An inverted index was chosen to allow efficient search by mapping words directly to the pages that contain them, avoiding full document scans.

### Tokenization

Text is:

* converted to lowercase
* stripped of punctuation using regex

This ensures consistent indexing and querying.

### Ranking

A TF-IDF-style scoring function is used to prioritise relevant pages over those containing very common terms.

### Crawler

The crawler:

* uses Requests for HTTP requests
* uses BeautifulSoup for HTML parsing
* follows pagination links
* enforces a politeness delay of at least 6 seconds between requests

---

## Limitations

* Only crawls a single website
* No parallel crawling (intentionally sequential for politeness)
* Basic query handling (no phrase search or boolean operators)
* Index stored as JSON (not optimised for large-scale data)

---

## Future Improvements

* Phrase search support
* Boolean queries (AND, OR, NOT)
* More advanced ranking (full TF-IDF or BM25)
* Caching crawled pages
* Web-based interface instead of CLI

---

## Dependencies

* requests
* beautifulsoup4
* pytest

---

## GenAI Usage

Generative AI tools were used to assist with:

* planning and structuring the project
* debugging and resolving errors
* improving code clarity and testing

All generated suggestions were reviewed, tested, and adapted to ensure full understanding of the implementation.


---


