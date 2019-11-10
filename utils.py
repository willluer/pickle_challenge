import json
import re

def get_digit_map(file):
    digit_map = None

    with open(file) as json_file:
        json_contents = json.loads(json_file.read())
        digit_map = json_contents["digit_map"]

    if not digit_map:
        print("Error reading in config file")
        sys.exit()

    return digit_map

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

def construct_char_map(digit_map):
    char_map = {}
    for digit,chars in digit_map.items():
        for char in chars:
            char_map[char] = digit
    return char_map
