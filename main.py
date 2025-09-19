# Course #4 of Boot.Dev

# Bookbot

from stats import get_words, get_chars, sort_dict
import sys

def get_book_text(filepath):
    #opens a file from its filepath,
    #and returns its contents as a string
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>|")
        sys.exit(1)

    filepath = sys.argv[1]
    string  = get_book_text(filepath)
    num_words = get_words(string)

    output_line1 = "============ BOOKBOT ============"
    output_line2 = f"Analyzing book found at {filepath}"
    output_line3 = "----------- Word Count ----------"
    output_line5 = "--------- Character Count -------"
    output_line_end = "============= END ==============="

    print(output_line1)
    print(output_line2)
    print(output_line3)
    print(f"Found {num_words} total words")
    print(output_line5)

    for item in sort_dict(get_chars(string)):
        if item["char"].isalpha():
            print(f'{item["char"]}: {item["num"]}')

    print(output_line_end)
main()
