import re

def arithmetic_arranger(problems, solution=False): 
    row1 = ""
    row2 = ""
    row3 = ""
    row4 = ""
    
    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        problem_elements = re.search('(.*)\s(\S)\s(.*)', problem)
        
        first_num = problem_elements.group(1)
        operator = problem_elements.group(2)
        second_num = problem_elements.group(3)
        
        if operator != "+" and operator != "-":
            return "Error: Operator must be '+' or '-'."
        
        if first_num.isdecimal() == False or second_num.isdecimal() == False:
            return "Error: Numbers must only contain digits."
        
        first_num_length = len(str(first_num))
        second_num_length = len(str(second_num))
        
        if first_num_length > 4 or second_num_length > 4:
            return "Error: Numbers cannot be more than four digits."
        
        max_spaces = max(first_num_length, second_num_length) + 2
        first_row_space = " " * (max_spaces - first_num_length)
        second_row_space = " " * ((max_spaces - 1) - second_num_length)
        indent = "    " 
    
        row1 += (first_row_space + first_num + indent)
        row2 += (operator + second_row_space + second_num + indent)
        row3 += (("-" * max_spaces) + indent)
        
        if solution == True:
            expression = first_num + operator + second_num
            answer = str(eval(expression))
            answer_length = len(answer)
            answer_space = " " * (max_spaces - answer_length)
            row4 += (answer_space + answer + indent) 

    if solution == True:
        arranged_problems = (row1.rstrip(" ")) + '\n' + (row2.rstrip(" ")) + '\n' + (row3.rstrip(" ")) + '\n' + (row4.rstrip(" "))
        return arranged_problems
    else:
        arranged_problems = (row1.rstrip(" ")) + '\n' + (row2.rstrip(" ")) + '\n' + (row3.rstrip(" "))
        return arranged_problems
     
print(arithmetic_arranger(testlist, True))