import sys
from stats import get_num_words, get_symbol_counts, get_counts_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def print_report(filepath):
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    counts = get_symbol_counts(text)
    cl = get_counts_list(counts)
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in cl:
        s = i['symbol']
        if s.isalpha():
            print(f"{s}: {i['count']}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print_report(sys.argv[1])
    print("============= END ===============")
    # text = get_book_text("books/frankenstein.txt")
    # num_words = get_num_words(text)
    # print(f"{num_words} words found in the document")
    # counts = get_symbol_counts(text)
    # print(counts)
    # print(get_counts_list(counts))

main()
