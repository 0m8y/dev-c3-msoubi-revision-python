def factorial(number):
    result = 1

    if number == 0:
        return 0
    for i in range(1, number + 1):
        result = i * result
    return result

def main():
    while True:
        number = input("Entrez un nombre (\"stop\" pour arrêter le processus) : ")
        if number == "stop":
            break
        elif number.isdigit():
            print("Le factoriel de " + number + " est : " + str(factorial(int(number))))
        else:
            print("Nombre invalide")

if __name__ == "__main__":
    main()