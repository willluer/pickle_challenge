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
def construct_char_map(digit_map):
    char_map = {}
    for digit,chars in digit_map.items():
        for char in chars:
            char_map[char] = digit
    return char_map

# Makes sure input is contains appropriate characters
def is_valid_input(input,regex):
    regex = re.compile(regex)
    if regex.search(input):
        print("Input phone number only accepts the following non alphanumeric characters /().-+")
        return False
    if not (len(input) == 10 or len(input) == 11):
        print("Input phone number must have 10 or 11 digits")
        return False
    return True
