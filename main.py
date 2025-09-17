# Course #4 of Boot.Dev

# Bookbot

from stats import get_words, get_chars

def get_book_text(filepath):
    #opens a file from its filepath,
    #and returns its contents as a string
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    string  = get_book_text("books/frankenstein.txt")
    num_words = get_words(string)
    print(f"{num_words} words found in the document")
    print()
    print(get_chars(string))

main()
