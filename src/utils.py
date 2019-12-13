import json
import re

# Read digit map from config
def get_digit_map(file):
    digit_map = None

    with open(file) as json_file:
        json_contents = json.loads(json_file.read())
        digit_map = json_contents["digit_map"]

    if not digit_map:
        print("Error reading in config file")
        sys.exit()

    return digit_map

# Read langauges from config
def get_language_map(file):
    languages = None

    with open(file) as json_file:
        json_contents = json.loads(json_file.read())
        languages = json_contents["languages"]

    if not languages:
        print("Error reading in config file")
        sys.exit()

    return languages

# Removes acceptable non alphanumeric characters
# Converts characters to uppercase
def clean_input(input):
    cleaned = re.sub('[/()\+.-]','',input.upper())
    return cleaned

# Creates dictionary of {char: number,}
def reverse_dict(digit_map):
    char_map = {}
    for digit,chars in digit_map.items():
        for char in chars:
            char_map[char] = digit
    return char_map

# Makes sure input is contains appropriate characters
def is_valid_input(input,regex):
    regex = re.compile(regex)
    if regex.search(input):
        print("Input phone number may only contain the following non alphanumeric characters /().-+")
        return False
    if not (len(input) == 10 or len(input) == 11):
        print("Input phone number must have 10 or 11 digits")
        return False
    return True

#https://stackoverflow.com/questions/2556108/rreplace-how-to-replace-the-last-occurrence-of-an-expression-in-a-string
def rreplace(s,old,new,occurence):
    li = s.rsplit(old,occurence)
    return new.join(li)


# https://stackoverflow.com/questions/35091557/replace-nth-occurrence-of-substring-in-string
# Replace nth occurence of a substring
# Used when multiple instances of a digit, e.g. '96' repeats in 96196
def nth_substr_repl(s, sub, repl, nth):
    # print("s {}".format(s))
    # print("sub {}".format(sub))
    # print("repl {}".format(repl))
    # print("nth {}".format(nth))
    find = s.find(sub)
    # if find is not p1 we have found at least one match for the substring
    i = find != -1
    # loop util we find the nth or we find no match
    while find != -1 and i != nth:
        # find + 1 means we start at the last match start index + 1
        find = s.find(sub, find + 1)
        i += 1
    # if i  is equal to nth we found nth matches so replace
    if i == nth:
        return s[:find]+repl+s[find + len(sub):]
    return s
