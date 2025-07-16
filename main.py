from stats import get_num_words, count_chars, sort_dict

def main():
    path = "books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")

    text = get_book_text(path)

    num = get_num_words(text)
    print(f"{num} words found in the document")

    print("--------- Character Count -------")
    char_count = sort_dict(count_chars(text))
    for i in range(0,len(char_count),2):
        #print(char_count[i])
        if char_count[i]["char"].isalpha():
            print(f"{char_count[i]["char"]}: {char_count[i]["num"]}")

    print("============= END ===============")

    # result_chars = count_chars(text)
    # print(result_chars)
    #print(sort_dict(count_chars(text)))





def get_book_text(path_to_book):
    with open(path_to_book) as book:
        # do something with path_to_book (the file) here
        file_contents = book.read()
    return file_contents



main()