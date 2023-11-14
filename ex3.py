import re
def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        print("Division par 0 impossible.")
        exit(84)
    return num1 / num2

def addition(num1, num2):
    return num1 + num2

def substraction(num1, num2):
    return num1 - num2

def simple_calcul(func, position, calcul_list):
    calcul_list[position] = str(func(int(calcul_list[position - 1]), int(calcul_list[position + 1])))
    calcul_list.pop(position - 1)
    calcul_list.pop(position + 1)
    return calcul_list

def calculator(calcul):
    iterator = 0
    for element in calcul :
        if element == "*" :
            calculator(simple_calcul(multiplication, iterator, calcul))
        if element == "/" :
            calculator(simple_calcul(division, iterator, calcul))
        iterator += 1
    iterator = 0
    for element in calcul :
        if element == "+" :
            calculator(simple_calcul(addition, iterator, calcul))
        if element == "-" :
            calculator(simple_calcul(substraction, iterator, calcul))
        iterator += 1

    print("result is " + calcul[0])

def main():
    calcul_input = input("Entrez votre calcul: ")
    pattern = re.compile(r"(-?[1-9]+|[+-/*])")
    calcul_regex = re.findall(pattern, calcul_input)

    if calcul_regex:
        calculator(calcul_regex[0])
    else:
        print("Calcul invalide")
        exit(84)

if __name__ == "__main__":
    main()