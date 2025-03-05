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
    
    path_to_book = "books/frankenstein.txt"
    print(f"--- Begin report of {path_to_book} ---")
    print(f"{return_word_counts(read_books(path_to_book))} words found in the document")
    print("")
    
    characters_dict = get_num_words(read_books(path_to_book))
    for character, quantity in characters_dict :
        print(f"The '{character}' character was found {quantity} times")
    
    print("--- End report ---")
    return status

main()