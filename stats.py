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

def sort_on(items):
    return items["num"]

def sort_dict(dict):
    list_of_dicts = []
    for char in dict:
        sub_dict = {}
        sub_dict["char"] = char
        sub_dict["num"] = dict[char]
        #print(sub_dict)
        list_of_dicts.append(sub_dict)

    list_of_dicts.sort(reverse=True, key=sort_on)

    return list_of_dicts
