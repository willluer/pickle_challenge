import re
import enchant

letter_map = {"0":[],\
              "1":[],\
              "2":["A","B","C"],\
              "3":["D","E","F"],\
              "4":["G","H","I"],\
              "5":["J","K","L"],\
              "6":["M","N","O"],\
              "7":["P","Q","R","S"],\
              "8":["T","U","V"],\
              "9":["W","X","Y","Z"]}

char_map = {}
for digit,chars in letter_map.items():
    for char in chars:
        char_map[char] = digit

vowel_map = {"2":"A","3":"E","4":"I","6":"O","8":"U"}

def number_to_words(number):
    # Clean input (remove any non alphanumeric characters and make uppercase)
    number = clean_input(number)

    # Check input
    if not is_valid_input(number):
        return "Input phone number must have 10 or 11 digits (xxx-xxx-xxxx or x-xxx-xxx-xxxx) and only accepts the following non alphanumeric characters /().- "

    # words has numbers replaced with letters
    words = find_words(number)

    return "DONE"

# Iterate through backwards
# naive heuristic of words are more likely to be at the back of a number than the front
def generate_next_number(number):
    min_word_size = 3 # letters
    for i in range(1,len(number)):
        for j in range(i+min_word_size,len(number)+1):
            yield(number[-j:-i])

def find_words(number):
    number = "1800724683799710"
    for current_digit in generate_next_number(number):
        # print(current_digit)
        valid,word = is_valid_word(current_digit)
        if valid:
            return word


def is_valid_word(test_digits):
    # print("Checking {}".format(test_digits))
    digits_set = [False for i in range(len(test_digits))]
    digits_list = list(test_digits) # lists are easier than strings to work with

    # May not contain a 0 or 1
    if any(d in digits_list for d in ["0","1"]):
        print("{} contains a 0 or  1".format(test_digits))
        return False,None

    # Make sure word contains a vowel
    vowel_digits = ["2","3","4","6","8"]
    vowel_count = 0
    vowel_index = 0
    for i in range(len(digits_list)):
        if digits_list[i] in vowel_digits:
            vowel_count += 1
            vowel_index = i
    if vowel_count == 0:
        print("{} does not contain a vowel".format(test_digits))
        return False,None

    # We know this must be the vowel
    if vowel_count == 1:
        digits_set[vowel_index] = True
        digits_list[vowel_index] = vowel_map[digits_list[vowel_index]]
        print("Setting one vowel to be a vowel")

    return True,"HERE"

# Removes acceptable non alphanumeric characters
# Converts characters to uppercase
def clean_input(input):
    cleaned = re.sub('[/().-]','',input.upper())
    return cleaned

# Makes sure there are only numeric characters in the input
def is_valid_input(input):
    regex = re.compile('[\W\D]')
    if regex.search(input):
        return False
    return True


if __name__ == "__main__":
    test = "1-(800)-123433"
    test_output = number_to_words(test)
    print("{} yields {}\n".format(test,test_output))

    test = "800-PAI)(--NT@ER"
    test_output = number_to_words(test)
    print("{} yields {}\n".format(test,test_output))

    test = "1-800-//DOPG /+"
    test_output = number_to_words(test)
    print("{} yields {}\n".format(test,test_output))

    test = "1-800-WILL 'as fd 3'"
    test_output = number_to_words(test)
    print("{} yields {}\n".format(test,test_output))

    test = "17-354412"
    test_output = number_to_words(test)
    print("{} yields {}\n".format(test,test_output))

    test = "947867542"
    test_output = number_to_words(test)
    print("{} yields {}\n".format(test,test_output))

    test = "25640946"
    test_output = number_to_words(test)
    print("{} yields {}\n".format(test,test_output))

    test = "366833657"
    test_output = number_to_words(test)
    print("{} yields {}\n".format(test,test_output))

    test = "56183549-0367"
    test_output = number_to_words(test)
    print("{} yields {}\n".format(test,test_output))
