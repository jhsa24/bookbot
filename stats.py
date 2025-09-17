# Course #4 of Boot.Dev

# Bookbot


def get_words(string):
    #takes a string and returns the
    # number of words found in it
    split_string = string.split()
    return len(split_string)

def get_chars(string):
    #takes a string and returns a dictionary
    #of characters and how often they occur
    char_dict = {}
    for char in string:
        if char.lower() in char_dict:
            char_dict[char.lower()] += 1
        else: char_dict[char.lower()] = 1

    return char_dict
