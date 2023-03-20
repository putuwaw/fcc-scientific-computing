def arithmetic_arranger(problems, result=False):
    arranged_problems = ""
    if len(problems) > 5:
        return "Error: Too many problems."
    else:
        temp = []
        for i in problems:
            prob = i.split(" ")
            if prob[1] != "+" and prob[1] != "-":
                return "Error: Operator must be '+' or '-'."
            elif not str.isdigit(prob[0]) or not str.isdigit(prob[2]):
                return "Error: Numbers must only contain digits."
            elif len(prob[0]) > 4 or len(prob[2]) > 4:
                return "Error: Numbers cannot be more than four digits."
            else:
                temp.append(i.split(" "))
        for i in range(4):
            if (i == 3 and not result):
                break
            if i > 0:
                arranged_problems = arranged_problems + "\n"
            for j in range(len(problems)):
                if (i == 0):
                    if len(temp[j][0]) == max(len(temp[j][0]), len(temp[j][2])):
                        strOperand = ""
                    else:
                        strOperand = abs(len(temp[j][0]) - len(temp[j][2])) * " "
                    arranged_problems = arranged_problems + "  " + strOperand + temp[j][0] + "    "
                elif (i == 1):
                    if len(temp[j][2]) == max(len(temp[j][0]), len(temp[j][2])):
                        strOperand = ""
                    else:
                        strOperand = abs(len(temp[j][0]) - len(temp[j][2])) * " "
                    arranged_problems = arranged_problems + temp[j][1] + " " + strOperand + temp[j][2] + "    "
                elif (i == 2):
                    strOperand = max(len(temp[j][0]), len(temp[j][2])) * "-"
                    arranged_problems = arranged_problems + "--" + strOperand + "    "
                elif i == 3:
                    calc = 0
                    if (temp[j][1] == "+"):
                        calc = int(temp[j][0]) + int(temp[j][2])
                    else:
                        calc = int(temp[j][0]) - int(temp[j][2])
                    strOperand = (max(len(temp[j][0]), len(temp[j][2])) - len(str(calc)) + 1) * " "
                    arranged_problems = arranged_problems + " " + strOperand + str(calc) + "    "
                if (j == len(problems) - 1):
                    arranged_problems = arranged_problems[:-4]    
    return arranged_problems
