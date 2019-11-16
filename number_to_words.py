import re
from csp import CspSolver
import argparse
import utils

class NumberToWords:
    def __init__(self,language="american_english",min_word_size=3,config="config.json",print_search_progress=False):

        self.digit_map = utils.get_digit_map(file=config)
        self.char_map = utils.reverse_dict(self.digit_map)
        allowed_languages = utils.get_language_map(file=config)
        self.csp_solver = CspSolver(config=config,language=allowed_languages[language],print_search_progress=print_search_progress)

        self.min_word_size = min_word_size

    def number_to_words(self,number):
        # Clean input (remove any non alphanumeric characters and make uppercase)
        number = utils.clean_input(number)

        # Check input
        if not utils.is_valid_input(number,regex="[\W\D]"):
            return None,None

        # returns a string word
        word,digits = self.find_word(number)

        if word:
            number = utils.rreplace(number,digits,word,1)
            return word, number
        else:
            return None, None

    # Iterate through backwards
    # naive heuristic of words are more likely to be at the back of a number than the front
    def generate_next_number(self,number):
        for i in range(0,len(number)):
            for j in range(i+self.min_word_size,len(number)+1):
                if i == 0:
                    yield(number[-j:])
                else:
                    yield(number[-j:-i])

    def find_word(self,number):
        for current_digit in self.generate_next_number(number):
            word = self.is_valid_word(current_digit)
            if word:
                return word,current_digit
        return None,0


    def is_valid_word(self,test_digits):
        digits_list = list(test_digits) # lists are easier than strings to work with

        # May not contain a 0 or 1
        if any(d in digits_list for d in ["0","1"]):
            # print("{} contains a 0 or 1".format(test_digits))
            return None

        # Make sure word contains a vowel
        vowel_digits = ["2","3","4","6","8","9"]
        contains_vowel = False
        for digit in test_digits:
            if digit in vowel_digits:
                contains_vowel = True

        if not contains_vowel:
            # print("{} does not contain a vowel".format(test_digits))
            return None

        return self.csp_solver.find_word(test_digits) # None if no word exists, the word if it does


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--number","-n", help="Phone number to look for words within. Must contain 10 or 11 digits and must be only digits and the following characters: /()\+.-", \
                        required=True,default=None)
    parser.add_argument("--language", "-l", help="Language to use.", \
                        default="american_english", choices=["american_english","australian_english", "british_english", "german","french"])
    parser.add_argument("--min-word-size", "-m", help="Minimum sized word to find. Must be an int.", \
                        type=int,default=3,choices=range(1,12))
    parser.add_argument("--print-search-progress", help="Print the search progress of the CSP (just for debugging purposes to make sure code's not stuck)", \
                        action='store_true')

    args = parser.parse_args()

    number_to_words = NumberToWords(language=args.language,\
                                    min_word_size=args.min_word_size, \
                                    print_search_progress=args.print_search_progress)


    word, digits_with_word = number_to_words.number_to_words(args.number)
    if word:
        print("{} yields {}\n".format(args.number,digits_with_word))
    else:
        print("No words found")
