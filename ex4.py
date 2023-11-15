
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

def max(number_list):
    max = number_list[0]
    for number in number_list:
        if number > max: max = number
    print("max: " + str(max))
    return max

def min(number_list):
    min = number_list[0]
    for number in number_list:
        if number < min: min = number
    print("min: " + str(min))
    return min

def main():
    number_list = [1, 45, 35, 92, 41, 20, 36, 57, 28, 65]
    mean(number_list)
    max(number_list)
    min(number_list)



if __name__ == "__main__":
    main()