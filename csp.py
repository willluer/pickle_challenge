from constraint import *
import enchant

letter_map = {"0":[],\
              "1":[],\
              "2":["A","B","C"],\
              "3":["D"],\
              "4":["G","H","I"],\
              "5":["J","K","L"],\
              "6":["M","N","O"],\
              "7":["P","Q","R","S"],\
              "8":["T","U","V"],\
              "9":["W","X","Y","Z"]}

number = "364"
problem = Problem()

def is_solution(*word):
    word = list(word)
    # print("word: {}".format(word))
    # print("type of word: {}".format(type(word)))

    word = "".join(word) # Converts to string
    return enchant.Dict("en_US").check(word)

for d in number:
    problem.addVariable(d,letter_map[d])

problem.addConstraint(FunctionConstraint(is_solution),list(number))
# problem.addConstraint(InSetConstraint(["A","E","I","O","U"]))
sols = problem.getSolution()
print(sols)
