from constraint import *
import enchant
import utils

class CspSolver:
    def __init__(self,language="en_US",config="config.json"):
        self.digit_map = utils.get_digit_map(file=config)
        self.language = language
        print(self.language)


    def find_all_words(self,number):
        return self.create_problem(number).getSolutions()

    def find_word(self,number):
        soln = self.create_problem(number).getSolution()
        if soln:
            return self.construct_str(soln,number)
        else:
            return None

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
            problem.addVariable(current_var,self.digit_map[d])
        problem.addConstraint(SomeInSetConstraint(["A","E","I","O","U"]))
        problem.addConstraint(FunctionConstraint(self.is_solution),variables)
        return problem

    def is_solution(self,*word):
        word = "".join(list(word)) # Converts to string
        is_valid = enchant.Dict(self.language).check(word)
        # if is_valid:
            # print("{} is valid? {}".format(word,is_valid))
        return is_valid

    def construct_str(self,result_dict,number):
        result_str = ""
        n_count = {}
        for i in range(10):
            n_count[str(i)] = 0

        for d in number:
            result_str+=result_dict["{}-{}".format(d,n_count[d])]
            n_count[d] += 1
        return result_str


if __name__ == "__main__":
    csp_solver = CspSolver()
    n = "433"
    word = csp_solver.find_word(n)
    print(word)
    # word_str = csp_solver.construct_str(word,n)
    # print(word_str)

    # words = csp_solver.find_all_words(n)
    # words_str = []
    # for word in words:
    #     words_str.append(csp_solver.construct_str(word,n))
    # print(words_str)
