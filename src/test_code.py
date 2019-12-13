from number_to_words import NumberToWords
from words_to_number import WordsToNumber
from all_wordifications import AllWordifications
import random
import time
import argparse
import utils

# Simulataneously test number_to_words and words_to_number
# Generates random number, finds a word, replaces word in number, converts back to all numbers
# If original number and word that has been transformed by n2w and w2n don't match
# then it outputs the erroroneous numbers to a file
def test_number_to_words(n,language,min_word_size,print_search_progress):
    n2w = NumberToWords(language=language,min_word_size=min_word_size,print_search_progress=print_search_progress)
    w2n = WordsToNumber()
    error_file = "error_n2w.txt"
    word,digits = n2w.number_to_words(n)

    # If solution found
    if digits:
        original = w2n.words_to_number(digits).replace("-","")

        # If mismatch (BAD)
        if n != original:
            with open(error_file,"a") as file:
                file.write("{},{},{},{},{}\n".format(n,digits,original,language,min_word_size))

# Similar to above but tests every solution found by all_wordifications
def test_all_wordifications(n,language,min_word_size,print_search_progress):
    w2n = WordsToNumber()
    aw = AllWordifications(language=language,min_word_size=min_word_size,print_search_progress=print_search_progress)
    error_file = "error_aw.txt"
    words = aw.all_wordifications(n)
    # If solutions found
    if words:
        for word in words:
            original = w2n.words_to_number(word).replace("-","")

            # If mismatch (BAD)
            if n != original:
                with open(error_file,"a") as file:
                    file.write("{},{},{},{},{}\n".format(n,word,original,language,min_word_size))

# Generate random number of 10 or 11 digits
# Not generating numbers with 5,8,or 9 since these numbers have uncommon letters and increase processing time
def gen_rand_number():
    n = ""
    for i in random.choice([range(10),range(11)]):
        n += str(random.choice([0,1,2,3,4,6,7]))
    return n


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--number-of-tests","-n", help="Number of tests to do for each iteration", \
                        required=False,default=1,type=int)
    parser.add_argument("--test-all-wordifications", help="True/False to test AllWordifications (be careful, can take awhile)",\
                        action='store_true')
    parser.add_argument("--test-number-to-words", help="True/False to test NumberToWords", \
                        action='store_true')
    parser.add_argument("--min-word-size", help="Minimum sized word to find. Must be an int.", \
                        type=int,default=3,choices=range(1,12))
    parser.add_argument("--max-min-word-size", help="Largest minimum word size to find. Must be an int.", \
                        type=int,default=3,choices=range(1,12))
    parser.add_argument("--print-search-progress", help="Print the search progress of the CSP (just for debugging purposes to make sure code's not stuck)", \
                        action='store_true')
    args = parser.parse_args()

    allowed_languages = utils.get_language_map(file="config.json").keys()
    parameter_combinations = [[i, j] for i in range(args.min_word_size,args.max_min_word_size+1) for j in allowed_languages]

    full_start = time.time()

    # For every combination of min_word_size and language
    for min_word_size,language in parameter_combinations:
        print("Beginning tests for min_word_size={} and language={}".format(min_word_size,language))

        for i in range(args.number_of_tests):
            random_number = gen_rand_number()
            print("Testing number: {}".format(random_number))

            # NumberToWords
            if args.test_number_to_words:
                start = time.time()
                test_number_to_words(random_number,language,min_word_size,args.print_search_progress)
                runtime = time.time() - start
                print("N2W took {} seconds\n".format(round(runtime,2)))

            # AllWordifications
            if args.test_all_wordifications:
                start = time.time()
                test_all_wordifications(random_number,language,min_word_size,args.print_search_progress)
                runtime = time.time() - start
                print("AW took {} seconds\n".format(round(runtime,2)))

    full_runtime = time.time() - full_start
    print("Took {} seconds to complete all tests".format(full_runtime))
