from number_to_words import NumberToWords
import argparse
import utils

class AllWordifications(NumberToWords):
    def __init__(self,language="american_english",min_word_size=3,config="config.json",print_search_progress=False):
        super().__init__(language,min_word_size,config,print_search_progress)
        self.memos = set()

    def all_wordifications(self,number):
        # Clean input (remove any non alphanumeric characters and make uppercase)
        number = utils.clean_input(number)

        # Check input
        if not utils.is_valid_input(number,regex="[\W\D]"):
            return None

        # returns a dict of {"#####":["WORD1","WORD2"]...}
        solutions = self.find_words(number)

        if solutions:
            numbers = self.create_all_wordifications(number,solutions)
            return numbers
        else:
            # print("No words found")
            return None

    def create_all_wordifications(self,number,solutions):
        self.digit_arr = list(solutions.keys())
        self.soln_arr = list(solutions.values())

        solutions = set(self.wordification_helper_recursive(i=0,j=0,current_number=number,nth_repl=1))
        solutions.add(number)
        return solutions


    # Recursive program to stitch together all possible solutions
    def wordification_helper_recursive(self,i,j,current_number,nth_repl):
        # digits_to_replace = digit_arr[i]
        # word_to_replace_with = soln_arr[i][j]

        # Memoization
        if (current_number,i,j,nth_repl) in self.memos:
            return []
        self.memos.add((current_number,i,j,nth_repl))

        # Base case
        if i >= len(self.soln_arr):
            return []

        # Move to next digit
        elif j >= len(self.soln_arr[i]):
            return self.wordification_helper_recursive(i+1,0,current_number,1)

        # Check if replaced all instances
        elif nth_repl > current_number.count(self.digit_arr[i]) + 1:
            return []

        # If digit_to_replace not in the number
        elif self.digit_arr[i] not in current_number:
            return self.wordification_helper_recursive(i+1,0,current_number,1)

        # if digit_to_replace is in number
        elif self.digit_arr[i] in current_number:
            # Replace nth instance of digit
            new_number = utils.nth_substr_repl(current_number,self.digit_arr[i],self.soln_arr[i][j],nth_repl)

            # If the same digit string is still in the new number (repeated digits)
            if self.digit_arr[i] in new_number:

                # Still untouched repeating digits that need to be replaced
                if new_number.rfind(self.digit_arr[i]) > new_number.rfind(self.soln_arr[i][j]):
                    # Found number
                    # Next digit string with new number
                    # Next option for current digit
                    # Next instance of repeated digit in new number
                    # Next instance of same digit
                    return [new_number] + \
                            self.wordification_helper_recursive(i+1,0,new_number,1) + \
                            self.wordification_helper_recursive(i+1,0,current_number,1) + \
                            self.wordification_helper_recursive(i,j+1,new_number,1) + \
                            self.wordification_helper_recursive(i,j+1,current_number,1) + \
                            self.wordification_helper_recursive(i,j,new_number,1) + \
                            self.wordification_helper_recursive(i,j,current_number,nth_repl+1)

                # All repeating digits have been touched, move to next digit
                else:
                    # Found number
                    # Next digit string with new number
                    # Next digit string with current number
                    # Next option for current digit on new number
                    # Next option for current digit on current number
                    return [new_number] + \
                        self.wordification_helper_recursive(i+1,0,new_number,1) + \
                        self.wordification_helper_recursive(i+1,0,current_number,1) + \
                        self.wordification_helper_recursive(i,j+1,new_number,1) + \
                        self.wordification_helper_recursive(i,j+1,current_number,1)

            else:
                # Found number
                # Next digit string with current number
                # Next option for current digit on current number
                return [new_number] + \
                        self.wordification_helper_recursive(i+1,0,new_number,1) + \
                        self.wordification_helper_recursive(i+1,0,current_number,1) + \
                        self.wordification_helper_recursive(i,j+1,current_number,1)

        else:
            return []

    # Gets dictionary of solutions from CSP solver
    def get_valid_words(self,test_digits):
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

        # print("test_digits: {}".format(test_digits))
        return self.csp_solver.find_all_words(test_digits) # None if no word exists, the word if it does

    def find_words(self,number):
        solutions = {}
        for current_digit in self.generate_next_number(number):
            words = self.get_valid_words(current_digit)
            if words:
                # print(solutions)
                for word in words:
                    if current_digit in solutions:
                        solutions[current_digit].append(word)
                    else:
                        solutions[current_digit] = [word]
        return solutions

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

    all_wordifications = AllWordifications(language=args.language,\
                                           min_word_size=args.min_word_size,\
                                           print_search_progress=args.print_search_progress)


    words = all_wordifications.all_wordifications(args.number)

    if words:
        print("All Wordifications: ")
        print("==========================")
        for i,word in enumerate(words):
            print("{}. {}".format(i,word))
    else:
        print("No words were found in {}".format(args.number))
