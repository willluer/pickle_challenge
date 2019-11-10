import re
import utils

class WordsToNumber():
    def __init__(self):
        self.digit_map = utils.get_digit_map(file=config)
        self.char_map = utils.construct_char_map(self.digit_map)

    def words_to_number(self,number):
        # Clean input (remove any acceptable non alphanumeric characters and make uppercase)
        number = utils.clean_input(number)

        # Make sure input is valid
        if not self.is_valid_input(number):
            return None

        # Substitute letters with digits
        for i in range(len(number)):
            currentChar = number[i]
            if currentChar.isalpha():
                number = number[0:i] + char_to_number(currentChar) + number[i+1:]

        # Add dashes back to number
        output = number_corrected_format(number)

        return output

    # Makes sure there are only alphanumeric characters in the input
    def is_valid_input(self,input):
        regex = re.compile('[\W]')
        if regex.search(input):
            print("Input phone number only accepts the following non alphanumeric characters /().-+")
            return False
        return True

    # Dict lookup
    def char_to_number(self,letter):
        for number,letters in letter_map.items():
            if letter in letters:
                return number

    # Prepare number for printing
    def number_corrected_format(self,number):
        if len(number) == 10:
            return number[:3]+"-"+number[3:6]+"-"+number[6:]
        else:
            return number[0]+"-"+number[1:4]+"-"+number[4:7]+"-"+number[7:]



if __name__ == "__main__":
    test = "1-(800)-PAI/NT.ER"
    test_output = words_to_number(test)
    print("{} yields {}\n".format(test,test_output))

    test = "800-PAI)(--NT@ER"
    test_output = words_to_number(test)
    print("{} yields {}\n".format(test,test_output))

    test = "1-800-//DOPG /+"
    test_output = words_to_number(test)
    print("{} yields {}\n".format(test,test_output))

    test = "1-800-WILL 'as fd 3'"
    test_output = words_to_number(test)
    print("{} yields {}\n".format(test,test_output))

    test = "WILL-PAINTER"
    test_output = words_to_number(test)
    print("{} yields {}\n".format(test,test_output))
