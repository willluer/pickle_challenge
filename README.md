# Pickle Robotics Coding Challenge

## Overview:
This repository contains all of the source code required to complete the challenge provided by Pickle Robotics.

## Requirements:  
 * python 3.7.5  
 * pyenchant 2.0.0  
 * python-constraint 1.4.0  

## Installation:
If you use conda/miniconda environments:  
* `git clone https://Willluer@bitbucket.org/Willluer/pickle_challenge.git`  
* `cd pickle_challenge`  
* `conda env create -f environment.yml`  

If you do not use conda/miniconda environments, install the required packages via pip.

## Usage:
NOTE: If you are using conda, ensure the appropriate conda environment is activated with the following command: `conda activate pickle`

#### number_to_words:
`python number_to_words.py [-h] [--number NUMBER] [--language {american_english,australian_english,british_english,german,french}] [--min-word-size {1,2,3,4,5,6,7,8,9,10,11}]`  

Example: `python number_to_words.py --number 1800PAINTER --language american_english --min-word-size 7`

#### words_to_number:
`python words_to_number.py [-h] [--number NUMBER]`  

Example: `python words_to_number.py --number 1800PAINTER`

#### all_wordifications:
`python all_wordifications.py [-h] [--number NUMBER] [--language {american_english,australian_english,british_english,german,french}] [--min-word-size {1,2,3,4,5,6,7,8,9,10,11}]`  

Example: `python all_wordifications.py --number 18007246837 --language american_english --min-word-size 7`


### Assumptions:
1. Characters/letters conform to the ITU E.161 standard (standard telephone keypad).
1. Desired usage is as command line program.
1. A valid input is any string with 10 or 11 numeric (or alphanumeric in words_to_number) characters that contain the following nonalphanumeric characters: / ( ) . - +
  * This means that +1-(888)-867-5309, 1.888.867.5309, and +21.91--6()42.+196 are all technically a valid input.
1. All words are verified to be valid using PyEnchant which has built in dictionaries in German, French, and three variations of English.
1. By default I used the american_english dictionary and a minimum word size of 3. These can be changed via the command line arguments specified in the Usage section.

### How It Works:
#### number_to_words
1. Make sure input is valid
2. Generate all possible substrings one by one
3. Check if CSP solver finds a valid word in the current substring
4. If valid word is found, end program
5. If valid word is not found, move to next substring and repeat from Step 3

#### words_to_number
1. Make sure input is valid
2. For each alpha character in input string, replace it with its corresponding digit from a standard telephone keypad
3. Reformat string with dashes
4. Return result to user
5. NOTE: The prompt for words_to_number says to do the reverse of number_to_words. However, I do not verify whether a string of letters composes a valid word. This way, the program can be used to convert phone numbers with acronyms that would not be recognized by a word lookup.

#### all_wordifications
1. Make sure input is valid
2. Generate all possible substrings one by one
3. Check if CSP solver finds a valid word for the current substring
4. Repeat step 3 until all substrings have been searched
4. If valid word(s) are found, run a recursive program to stitch together all possible combinations of letters and numbers.
5. Example:
* Input: 96123  
* CSP Output: {'96': ['YO'], '23': ['CE', 'BE', 'AF', 'AD']}  
* Recursive program output: [96123,961AD,961BE,961AF,YO123,YO1AF,YO1BE,YO1AD,961CE,YO1CE]  

### Heuristics
1. In searching for a solution to number_to_words, I begin looking for words at the end of the number sequence. This is based off a heuristic in which words are more likely to be at the end of telephone numbers due to country and area codes being at the beginning of telephone numbers.
1. For the CSP, I use a constraint that solutions cannot contain a 0 or a 1 since they do not map to any alpha characters and that a solution must have at least one vowel (or 'Y'). These constraints allow for pruning of branches in the search tree that do not lead to any valid solutions.
1. I implemented a dynamic programming approach called memoization to speed up the recursive program responsible for stitching together all possible solutions.
