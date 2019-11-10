import json

def get_letter_map(file):
    letter_map = None

    with open(file) as json_file:
        json_contents = json.loads(json_file.read())
        letter_map = json_contents["letter_map"]

    if not letter_map:
        print("Error reading in config file")
        sys.exit()

    return letter_map

def get_language_map(file):
    languages = None

    with open(file) as json_file:
        json_contents = json.loads(json_file.read())
        languages = json_contents["languages"]

    if not languages:
        print("Error reading in config file")
        sys.exit()

    return languages
