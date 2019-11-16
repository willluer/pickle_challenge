# Pickle Robotics Coding Challenge

## Overview:
This repository contains all of the source code required to complete the challenge provided by Pickle Robotics.

## Requirements:  
 * python 3.7.5  
 * pyenchant 2.0.0  
 * python-constraint 1.4.0  

## Installation:
If you use conda/miniconda environments:  
`git clone https://Willluer@bitbucket.org/Willluer/pickle_challenge.git`  
`cd pickle_challenge`  
`conda env create -f environment.yml`  

If you do not use conda/miniconda environments, install the required packages via pip.

## Usage:
NOTE: If you are using conda, ensure the appropriate conda environment is activated with the following command: `conda activate pickle`

#### number_to_words:
`python number_to_words.py [-h]`  
`[--number NUMBER]`  
`[--language {american_english,australian_english,british_english,german,french}]`   
`[--min-word-size {1,2,3,4,5,6,7,8,9,10,11}]`  
`[--print-search-progress]`  

Ex) To run number_to_words on the number 18007246837 in American English with a minimum word size of 5  
**INPUT:** `python number_to_words.py --number 1800742553 --language german --min-word-size 5`  
**OUTPUT:** `1800742553 yields 18007HALLE`  

#### words_to_number:
`python words_to_number.py [-h] [--number NUMBER]`  

Ex) To run words_to_number on the number 1800PAINTER  
**INPUT:** `python words_to_number.py --number 1800PAINTER`  
**OUTPUT:** `1800PAINTER yields 1-800-724-6837`  

#### all_wordifications:
`python all_wordifications.py [-h]`  
`[--number NUMBER]`  
`[--language {american_english,australian_english,british_english,german,french}]`  
`[--min-word-size {1,2,3,4,5,6,7,8,9,10,11}]`  
`[--print-search-progress]`  

Ex) To run all_wordifications on the number 18007246837 in American English with a minimum word size of 3  
**INPUT:** `python all_wordifications.py --number 18007216837 --language american_english --min-word-size 3`  
**OUTPUT:**  
`All Wordifications:`  
`==========================`  
`0. 1800721MUD7`  
`1. 1800721OVER`  
`2. 18007216837`  
`3. 1800721OTES`  
`4. 1800721MUDS`  

### Assumptions:
1. Characters/letters conform to the ITU E.161 standard (standard telephone keypad).
1. Desired usage is as command line program.
1. A valid input is any string with 10 or 11 numeric (or alphanumeric in words_to_number) characters. Input may contain the following nonalphanumeric characters: / ( ) . - +  
**NOTE:** This means that +1-(888)-867-5309, 1.888.867.5309, and +21.91--6()42.+196 are all technically a valid input.
1. All words are verified to be valid using PyEnchant which has built in dictionaries in German, French, and three variations of English.
1. By default I used the american_english dictionary and a minimum word size of 3. These can be changed via the command line arguments specified in the Usage section.

### How It Works:
#### number_to_words
1. Make sure input is valid
1. Generate all possible substrings one by one
1. Check if CSP solver finds a valid word in the current substring
1. If valid word is found, end program
1. If valid word is not found, move to next substring and repeat from Step 3

#### words_to_number
1. Make sure input is valid
1. For each alpha character in input string, replace it with its corresponding digit from a standard telephone keypad
1. Reformat string with dashes
1. Return result to user
1. NOTE: The prompt for words_to_number says to do the reverse of number_to_words. However, I do not verify whether a string of letters composes a valid word. This way, the program can be used to convert phone numbers with acronyms that would not be recognized by a word lookup.

#### all_wordifications
1. Make sure input is valid
1. Generate all possible substrings one by one
1. Check if CSP solver finds a valid word for the current substring
1. Repeat step 3 until all substrings have been searched
1. If valid word(s) are found, run a recursive program to stitch together all possible combinations of letters and numbers.
1. Example:
* Input: 96123  
* CSP Output from step 4: {'96': ['YO'], '23': ['CE', 'BE', 'AF', 'AD']}  
* Recursive program output: [96123,961AD,961BE,961AF,YO123,YO1AF,YO1BE,YO1AD,961CE,YO1CE]  

### Heuristics
1. In searching for a solution to number_to_words, I begin looking for words at the end of the number sequence. This is based off a heuristic in which words are more likely to be at the end of telephone numbers due to country and area codes being at the beginning of telephone numbers.
1. For the CSP, I use a constraint that solutions cannot contain a 0 or a 1 since they do not map to any alpha characters and that a solution must have at least one vowel (or 'Y'). These constraints allow for pruning of branches in the search tree that do not lead to any valid solutions.
1. I implemented a dynamic programming approach called memoization to speed up the recursive program responsible for stitching together all possible solutions.

### Testing
`test_code.py [-h] [--number-of-tests NUMBER_OF_TESTS]`  
                    `[--test-all-wordifications] [--test-number-to-words]`  
                    `[--min-word-size {1,2,3,4,5,6,7,8,9,10,11}]`  
                    `[--max-min-word-size {1,2,3,4,5,6,7,8,9,10,11}]`  
                    `[--print-search-progress]`  

Ex) To test number_to_words for all languages with minimum word sizes between 3 and 4:  
**INPUT:**`python test_code.py --test-number-to-words --min-word-size 3 --max-min-word-size 4`  
**OUTPUT:**
1. test_code.py contains code that will test number_to_words and all_wordifications by making use of words_to_number
1. It will test number_to_words and/or all_wordifications for every language and with every minimum word size in the range of [min_word_size,max_min_word_size]
1. The *--number-of-tests* parameter corresponds to how many numbers to generate and test for each language and min_word_size combination. It is recommended to keep this very small.
1. It works by randomly generating a phone number, finding a word (or all wordificiations) from the phone number and then testing whether words_to_number finds the original randomly generated number
1. If the generated number and original number are different, the number and paramters that led to the error are printed to a txt file  

**NOTE**: Due to the number of combinations of languages and minimum word sizes, this code base may produce more tests than a user anticipates so use with caution  
**NOTE**: the *print_search_progress* parameter is an interesting way of visualizing the search state of the CSP. Sometimes, it can take a long time for the CSP to find a solution, so this will help understand why.  
