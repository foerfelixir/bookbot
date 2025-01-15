def read_books(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents


def main():
    status = 0
    print(read_books("books/frankenstein.txt"))
    return status

main()