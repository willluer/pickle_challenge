# Pickle Robotics Coding Challenge

### Overview:
This repository contains all of the source code required to complete the challenge provided by Pickle Robotics.

### Requirements:
* Python 3.7.5
* pyenchant 2.0.0
* python-constraint 1.4.0

### Installation:
If you use conda/miniconda environments:
* `git clone <repo-link-here>`
* `cd pickle`
* `conda install requirements.txt`
* pip install pyenchant

If you do not use conda/miniconda environments:
* `pip install python-constraint`
* `pip install pyenchant`


### Usage:
Ensure the appropriate conda environment is activated with the following command `conda activate pickle`

##### number_to_words():
python number_to_words.py [--number -n] []
Approach:
number_to_words:
  finding a word with minimum three letter size
  English word as defined by the pyenchant module (Alternative dictionaries can be specified via command line argument)
  Start searching for words at the end of the word
  Return first one found

word_to_numbers:
