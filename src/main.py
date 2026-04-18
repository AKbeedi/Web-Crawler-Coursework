from crawler import crawl_site
from indexer import build_index, save_index, load_index
from search import print_word, find_pages
from indexer import build_index, save_index, load_index, tokenize


INDEX_PATH = "data/index.json"


def main():
    index = None

    while True:
        command = input("> ").strip()

        if command == "build":
            print("Building index...")
            pages = crawl_site(delay_seconds=6)  # change to 6 later
            index = build_index(pages)
            save_index(index, INDEX_PATH)
            print("Index built and saved.")

        elif command == "load":
            try:
                index = load_index(INDEX_PATH)
                print("Index loaded.")
            except FileNotFoundError:
                print("No index file found. Run 'build' first.")
        elif command == "print":
            print("Please enter a word to print.")
        elif command.startswith("print "):
            if index is None:
                print("Load or build index first.")
                continue

            word = command.split(" ", 1)[1].strip()
            tokens = tokenize(word)

            if len(tokens) != 1:
                print("Please enter exactly one word.")
                continue

            result = print_word(index, word)

            if not result:
                print(f"No results for '{word}'")
            else:
                for url, data in result.items():
                    print(f"{url} → freq={data['frequency']}, positions={data['positions']}")
        elif command == "find":
            print("Please enter a search query.")
        elif command.startswith("find "):
            if index is None:
                print("Load or build index first.")
                continue

            query = command.split(" ", 1)[1]
            results = find_pages(index, query)

            if not results:
                print("No matching pages found.")
            else:
                for r in results[:10]:
                    print(f"{r['url']} → score={r['score']}")
                    for word, data in r["matches"].items():
                        print(f"   {word}: freq={data['frequency']}, positions={data['positions']}")

        elif command in ["exit", "quit"]:
            print("Exiting.")
            break

        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()