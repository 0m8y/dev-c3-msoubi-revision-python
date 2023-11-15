
def main():
    while True:
        number = input("Entrez un nombre (\"stop\" pour arrêter le processus) : ")
        if number == "stop":
            break
        elif number.isdigit():
            factorial(number)
        else:
            print("Nombre invalide")

if __name__ == "__main__":
    main()