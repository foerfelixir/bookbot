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

def count_characters(book_content) :
    char_dictionaries = {}
    lowered_strings = book_content.lower().split()
    for string in lowered_strings :
        for character in string :
            if character in char_dictionaries:
                char_dictionaries[character] += 1
            else :
                char_dictionaries[character] = 1
    return char_dictionaries


def main():
    status = 0
    path_to_book = "books/frankenstein.txt"
    #print(read_books(path_to_book))
    print(count_characters(read_books(path_to_book)))
    print(f"total word count :{return_word_counts(read_books(path_to_book))}")
    return status

main()