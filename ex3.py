import re

def main():
    calcul_input = input("Entrez votre calcul: ")
    pattern = re.compile(r"(-?[1-9]+|[+-/*])")
    calcul_regex = re.findall(pattern, calcul_input)

    if calcul_regex:
        print(calcul_regex[0])
    else:
        print("Calcul invalide")

if __name__ == "__main__":
    main()