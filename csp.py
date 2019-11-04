from constraint import *
import enchant

class CspSolver:
    def __init__(self):
        self.letter_map = {"0":[],\
                      "1":[],\
                      "2":["A","B","C"],\
                      "3":["D","E","F"],\
                      "4":["G","H","I"],\
                      "5":["J","K","L"],\
                      "6":["M","N","O"],\
                      "7":["P","Q","R","S"],\
                      "8":["T","U","V"],\
                      "9":["W","X","Y","Z"]}

    def find_all_words(self,number):
        return self.create_problem(number).getSolutions()

    def find_word(self,number):
        return self.create_problem(number).getSolution()

    def create_problem(self,number):
        problem = Problem()
        variables = []
        n_count = {}

        for d in number:
            if d not in n_count:
                n_count[d] = 0
            else:
                n_count[d] += 1

            current_var = d+"-{}".format(n_count[d])
            variables.append(current_var)
            problem.addVariable(current_var,self.letter_map[d])
        problem.addConstraint(SomeInSetConstraint(["A","E","I","O","U"]))
        problem.addConstraint(FunctionConstraint(self.is_solution),variables)
        return problem

    def is_solution(self,*word):
        word = "".join(list(word)) # Converts to string
        is_valid = enchant.Dict("en_US").check(word)
        # if is_valid:
            # print("{} is valid? {}".format(word,is_valid))
        return is_valid

    def construct_str(self,result_dict,number):
        result_str = ""
        n_count = {}
        for i in range(10):
            n_count[str(i)] = 0

        print(n_count)
        for d in number:
            result_str+=result_dict["{}-{}".format(d,n_count[d])]
            n_count[d] += 1
        return result_str


if __name__ == "__main__":
    csp_solver = CspSolver()
    n = "724"
    word = csp_solver.find_word(n)
    word_str = csp_solver.construct_str(word,n)
    print(word_str)

    words = csp_solver.find_all_words(n)
    words_str = []
    for word in words:
        words_str.append(csp_solver.construct_str(word,n))
    print(words_str)
