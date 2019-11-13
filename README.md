# Pickle Robotics Coding Challenge

### Overview:
This repository contains all of the source code required to complete the challenge provided by Pickle Robotics.

### Requirements:
* Python 3.7.5
* pyenchant 2.0.0
* python-constraint 1.4.0

### Installation:
If you use conda/miniconda environments:
* `git clone https://Willluer@bitbucket.org/Willluer/pickle_challenge.git`
* `cd pickle_challenge`
* `conda install requirements.txt`
* pip install pyenchant

If you do not use conda/miniconda environments:
* `pip install python-constraint`
* `pip install pyenchant`


### Usage:
NOTE: If you are using conda, ensure the appropriate conda environment is activated with the following command `conda activate pickle`

##### number_to_words:
`python number_to_words.py [-h] [--number NUMBER] [--language {american_english,australian_english,british_english,german,french}] [--min-word-size {1,2,3,4,5,6,7,8,9,10,11}]`
<br>
<br>
Example usage: `python number_to_words.py --number 1800PAINTER --language american_english --min-word-size 7`

##### words_to_number:
`python words_to_number.py [-h] [--number NUMBER]`
<br>
<br>
Example usage: `python number_to_words.py --number 1800PAINTER`

##### all_wordifications:
`python all_wordifications.py [-h] [--number NUMBER] [--language {american_english,australian_english,british_english,german,french}] [--min-word-size {1,2,3,4,5,6,7,8,9,10,11}]`
<br><br>
Example usage: `python number_to_words.py --number 18007246837 --language american_english --min-word-size 7`

### Assumptions and Design Decisions:
1. Characters/letters conform to the ITU E.161 standard (standard telephone keypad)
1. All words are verified to be valid using PyEnchant which has built in dictionaries in German, French, and three variations of English.
1. The prompt for words_to_number says to do the reverse of number_to_words. However, I do not verify whether a string of letters composes a valid word. This way, the program can be used to convert phone numbers with acronyms as well as valid words. The program effectively maps each alpha character to its corresponding number on a standard telphone keypad.
1. In searching for a solution to number_to_words, I begin looking for words at the end of the number sequence. This is based off a heuristic in which words are more likely to be at the end of telephone numbers due to country and area codes at the beginning of telephone numbers.
1. By default I used the american_english dictionary and a minimum word size of 3. These can be changed via the command line arguments specified in the Usage section.
1. I modeled the words_to_number as a constraint satisfaction problem and implemented it using the python-constraint library. This searches for a valid word and uses the heuristic that there must be a minimum of one vowel in the solution to prune branches that would not lead to a valid solution.
1. words_to_number effectively maps letters to their respective numbers conforming to the standard telephone keypad
1. all_wordifications works by first using a CSP solver to find all possible words for all possible number substrings that are atleast the minimum word size in length. After doing so, a recursive program is run to stitch together all possible solutions of words and numbers.
1. The programs will accept as input any string with 10 or 11 numeric (or alphanumeric in words_to_number) characters that contain the following nonalphanumeric characters: / ( ) . - +
  * This means that +1-(888)-867-5309, 1.888.867.5309, and +21.91--6()42.+196 are all technically a valid input.
