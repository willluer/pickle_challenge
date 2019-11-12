import re
import utils
import argparse

class WordsToNumber:
    def __init__(self,config="config.json"):
        self.digit_map = utils.get_digit_map(file=config)
        self.char_map = utils.reverse_dict(self.digit_map)

    def words_to_number(self,number):
        # Clean input (remove any acceptable non alphanumeric characters and make uppercase)
        number = utils.clean_input(number)

        # Make sure input is valid
        if not utils.is_valid_input(number,regex="[\W]"):
            return None

        # Substitute letters with digits
        for i in range(len(number)):
            currentChar = number[i]
            if currentChar.isalpha():
                number = number[0:i] + self.char_map[currentChar] + number[i+1:]

        # Add dashes back to number
        output = self.number_corrected_format(number)

        return output

    # Prepare number for printing
    def number_corrected_format(self,number):
        if len(number) == 10:
            return number[:3]+"-"+number[3:6]+"-"+number[6:]
        else:
            return number[0]+"-"+number[1:4]+"-"+number[4:7]+"-"+number[7:]



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--number","-n", help="Phone number to look for words within. Must contain 10 or 11 digits and must be only digits and the following characters: /()\+.-", \
                        required=False,default=None)

    args = parser.parse_args()

    words_to_number = WordsToNumber()

    if args.number:
        output = words_to_number.words_to_number(args.number)
        print("{} yields {}\n".format(args.number,output))
    else:
        test = "1-(800)-1234323"
        output = words_to_number.words_to_number(test)
        print("{} yields {}\n".format(test,output))

        test = "1-(800)-PAI/NT.ER"
        test_output = words_to_number.words_to_number(test)
        print("{} yields {}\n".format(test,test_output))

        test = "800-PAI)(--NT@ER"
        test_output = words_to_number.words_to_number(test)
        print("{} yields {}\n".format(test,test_output))
        #
        test = "1-800-//DOPG /+"
        test_output = words_to_number.words_to_number(test)
        print("{} yields {}\n".format(test,test_output))
        #
        test = "1-800-WILL 'as fd 3'"
        test_output = words_to_number.words_to_number(test)
        print("{} yields {}\n".format(test,test_output))
        #
        test = "SDFH++++AD3S9NH"
        test_output = words_to_number.words_to_number(test)
        print("{} yields {}\n".format(test,test_output))
