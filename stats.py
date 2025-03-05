def sort_dictionaries(char_dict) :
    alphabet_dict={}
    for character, quantity in char_dict.items() :
        if character.isalpha() == True :
            alphabet_dict[character] = quantity
    
    return sorted(alphabet_dict.items(), key=lambda x: x[1], reverse=True)

def get_num_words(book_content) :
    char_dictionaries = {}
    lowered_strings = book_content.lower().split()
    for string in lowered_strings :
        for character in string :
            if character in char_dictionaries:
                char_dictionaries[character] += 1
            else :
                char_dictionaries[character] = 1
    return sort_dictionaries(char_dictionaries)