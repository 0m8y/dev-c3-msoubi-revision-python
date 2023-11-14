import re

def simple_calcul(func, position, calcul_list):
    calcul_list[position] = func(calcul_list[position - 1], calcul_list[position + 1])
    calcul_list.pop(position - 1)
    calcul_list.pop(position + 1)
    return calcul_list

def calculator(calcul):
    iterator = 0
    for element in calcul :
        if element == "*" :
            calculator(simple_calcul(multiple, iterator, calcul))
        if element == "/" :
            calculator(simple_calcul(divide, iterator, calcul))
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