import sys
from stats import get_num_words


def read_books(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def return_word_counts(book_content) :
    count = 0
    words = book_content.split()
    for whole_word in words:
        count += 1

    return count

def sort_on(dict):
    return dict["num"]

def main():
    status = 0
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_book>")
        return 1
    path_to_book = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {return_word_counts(read_books(path_to_book))} total words")
    print("--------- Character Count -------")
    
    characters_dict = get_num_words(read_books(path_to_book))
    for character, quantity in characters_dict :
        print(f"{character}: {quantity}")
    
    print("============= END ===============")
    return status

main()