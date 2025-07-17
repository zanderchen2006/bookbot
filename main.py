from stats import get_num_words, count_chars, sort_dict
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")

    text = get_book_text(path)

    num = get_num_words(text)
    print(f"Found {num} total words")

    print("--------- Character Count -------")
    char_count = sort_dict(count_chars(text))
    for char in char_count:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")

    print("============= END ===============")

def get_book_text(path_to_book):
    with open(path_to_book) as book:
        # do something with path_to_book (the file) here
        file_contents = book.read()
    return file_contents



main()