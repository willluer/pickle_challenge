import re

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

def words_to_number(number):
    # Clean input (remove any non alphanumeric characters and make uppercase)
    number = clean_input(number)

    # Check input
    if not is_valid_input(number):
        return "Input phone number must have 10 or 11 digits (xxx-xxx-xxxx or x-xxx-xxx-xxxx) and only accepts the following non alphanumeric characters /().- "

    # Substitute letters with digits
    for i in range(len(number)):
        currentChar = number[i]
        if currentChar.isalpha():
            number = number[0:i] + char_to_number(currentChar) + number[i+1:]

    # Add dashes back to number
    output = number_corrected_format(number)

    return output

def clean_input(input):
    # print("Input {}".format(input))
    cleaned = re.sub('[/().-]','',input.upper())
    # print("Cleaned {}".format(cleaned))
    return cleaned

# TO-DO
def is_valid_input(input):
    regex = re.compile('[\W]')
    if regex.search(input):
        return False
    return True

def char_to_number(letter):
    for number,letters in letter_map.items():
        if letter in letters:
            return number


def number_corrected_format(number):
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
