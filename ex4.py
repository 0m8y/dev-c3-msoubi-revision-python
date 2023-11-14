
def mean(number_list):
    print("mean: (", end="")
    result = 0
    isFirst = True
    for number in number_list:
        if not isFirst:
            print(" + ", end="")
        print(number, end="")
        result += number
        isFirst = False
    result /= len(number_list)
    print(") / " + str(len(number_list)) + " = " + str(result))
    return result

def main():
    number_list = [1, 45, 35, 92, 41, 20, 36, 57, 28, 65]
    mean(number_list)
    



if __name__ == "__main__":
    main()