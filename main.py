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

def sort_dictionaries(char_dict) :
    alphabet_dict={}
    for character, quantity in char_dict.items() :
        if character.isalpha() == True :
            alphabet_dict[character] = quantity
    
    return sorted(alphabet_dict.items(), key=lambda x: x[1], reverse=True)

def count_characters(book_content) :
    char_dictionaries = {}
    lowered_strings = book_content.lower().split()
    for string in lowered_strings :
        for character in string :
            if character in char_dictionaries:
                char_dictionaries[character] += 1
            else :
                char_dictionaries[character] = 1
    return sort_dictionaries(char_dictionaries)


def main():
    status = 0
    
    path_to_book = "books/frankenstein.txt"
    print(f"--- Begin report of {path_to_book} ---")
    print(f"{return_word_counts(read_books(path_to_book))} words found in the document")
    print("")
    
    characters_dict = count_characters(read_books(path_to_book))
    for character, quantity in characters_dict :
        print(f"The '{character}' character was found {quantity} times")
    
    print("--- End report ---")
    return status

main()