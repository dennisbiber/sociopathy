

def divide(x, y, zeroVariable = 1, exponentVariable = 1):
    expList = exponentVariable
    if y == 0:
        variable = zeroVariable
        if type(x) != str:
            addon = "**"
        stringThing = f"{variable}"
        for num in range(x):
            stringThing = "(" + stringThing + f"{addon}{expList[num]})"
        return eval(stringThing)

    elif y != 0:
        return x/y


def main():
    x = 0.145
    print([x] * int(3.45))
    print(divide(2, 0, zeroVariable = 0.145, exponentVariable = [3.25, 0.5]))

if __name__ == "__main__":
    main()